from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer, GameRecommendationsSerializer, GamesResultsSerializer, FiltersResultsSerializer
from .models import Game
from .rapid_api_helper import get_json
from rest_framework import status
import json
import datetime
import os
from django.conf import settings
from django.http import JsonResponse

class GetNewTrendingGames(APIView):
    def get(self, request):
        toDate = datetime.datetime.now().date()
        fromDate = toDate - datetime.timedelta(days=365)
        query = f'dates={fromDate},{toDate}&ordering=-rating&page_size=10'
        games = get_json('games', query)['results']
        
        return Response(get_game_serialized_result(games, True))

class GetGame(APIView):
    def get(self, request, id):
        endpoint = f'games/{id}'
        game = get_json(endpoint)
       
        return Response(get_game_serialized_result(game))

class GetPlatforms(APIView):
    def get(self, request):
        result = get_json('platforms/lists/parents')
        return Response(get_filter_serialized_result(result))

class GetStores(APIView):
    def get(self, request):
        result = get_json('stores')
        return Response(get_filter_serialized_result(result))

class GetGenres(APIView):
    def get(self, request):
        result = get_json('genres')
        return Response(get_filter_serialized_result(result))

class SearchGames(APIView):
    def get(self, request):
        page_number = int(request.GET.get('page', 1))
        page_size = 10
        static_params = f'page_size={page_size}'

        query_string = ''
        query_params = list(request.GET.dict().items())

        for param in query_params:
            param_name = param[0]
            param_value = param[1]

            if not param_value or param_name == 'page' or param_name == 'page_size':
                continue

            query_string += f'&{param_name}={param_value}'

        result = get_json('games', f'page={page_number}&{static_params}{query_string}')
        games_results_serializer = GamesResultsSerializer(data=result)
        games_results_serializer.is_valid()

        scheme = request.is_secure() and 'https' or 'http'
        host = f'{request.get_host()}'
        endpoint = f'games/search'
        url = f'{scheme}://{host}/{endpoint}?page='
        additional_params = f'{static_params}{query_string}'
        
        next_url = None
        if result and result['count'] > page_size * page_number:
            next_url = f'{url}{page_number + 1}&{additional_params}'

        previous_url = None
        if page_number > 1:
            previous_url = f'{url}{page_number - 1}&{additional_params}'

        games_results_serializer.validated_data['next'] = next_url
        games_results_serializer.validated_data['previous'] = previous_url

        return Response(games_results_serializer.validated_data)

class GetRecommendations(APIView):
    def get(self, request, id):
        endpoint = f'games/{id}'
        game = get_json(endpoint)        
        serializer = GameRecommendationsSerializer(data=game, many=False)
        serializer.is_valid()
        try:
            date = datetime.datetime.strptime(serializer.validated_data['released'], '%Y-%m-%d')
            date = ((datetime.datetime.today().year - date.year) * 12 + (datetime.datetime.today().month - date.month))/10
            metacritic = serializer.validated_data['metacritic']/10 if serializer.validated_data['metacritic'] else 6
            genres = serializer.validated_data['genres']
            predictions = predict([metacritic, genres, date],5)
            response = []
            for prediction in predictions:
                game = get_json('games?search='+prediction)
                game = game['results'][0]
                response.append(GameSerializer(instance=game).data)
            return JsonResponse(response, safe=False)
        except:
            return Response(data={"detail": "No game with such ID exists"}, 
            status=status.HTTP_404_NOT_FOUND)

def get_filter_serialized_result(json):
    serializer = FiltersResultsSerializer(data=json)
    serializer.is_valid()
    
    return serializer.validated_data 

def get_game_serialized_result(json, many=False):
    serializer = GameSerializer(data=json, many=many)
    serializer.is_valid()
    
    return serializer.validated_data 

def predict(input, nr_predictions):
    data = settings.RECOMMENDATIONS_DATA
    knn = settings.KNN_MODEL
    predictions = list()
    counter = 1
    while len(predictions) < nr_predictions:
        for x in input[1]:
            input_for_pred = [input[0], x['id'], input[2]]
            distances, indices = knn.kneighbors([input_for_pred],  n_neighbors=counter)
            if indices[0][counter-1] not in predictions and len(predictions) < nr_predictions:
                predictions.append(indices[0][counter-1])
            counter = counter + 1
    return [data.values[x, 0] for x in predictions]