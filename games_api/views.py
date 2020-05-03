from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer
from .serializers import GameRecommendationsSerializer
from .models import Game
from .rapid_api_helper import get_json
import json
import datetime
import os
from django.conf import settings

class GetNewTrendingGames(APIView):
    def get(self, request):
        
        toDate = datetime.datetime.now().date()
        fromDate = toDate - datetime.timedelta(days=365)
        query = f'dates={fromDate},{toDate}&ordering=-rating&page_size=10'
        print(query)
        results = get_json('games', query)['results']
        
        return Response(get_serialized_result(results, True))
       

class GetGame(APIView):
    def get(self, request, id):

        endpoint = f'games/{id}'
        game = get_json(endpoint)        
       
        return Response(get_serialized_result(game))

class GetRecommendations(APIView):
    def get(self, request, id):
        endpoint = f'games/{id}'
        game = get_json(endpoint)        
        serializer = GameRecommendationsSerializer(data=game, many=False)
        serializer.is_valid()
        
        date = datetime.datetime.strptime(serializer.validated_data['released'], '%Y-%m-%d')
        date = ((datetime.datetime.today().year - date.year) * 12 + (datetime.datetime.today().month - date.month))/10
        metacritic = serializer.validated_data['metacritic']/10
        genres = serializer.validated_data['genres']
        prediction = predict([metacritic, genres, date],5)
        return Response(prediction)

def get_serialized_result(json, many=False):
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