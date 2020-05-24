from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer, GameRecommendationsSerializer
from .models import Game
from .rapid_api_helper import get_json
import json
import datetime

class GetNewTrendingGames(APIView):
    def get(self, request):
        toDate = datetime.datetime.now().date()
        fromDate = toDate - datetime.timedelta(days=365)
        query = f'dates={fromDate},{toDate}&ordering=-rating&page_size=10'
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