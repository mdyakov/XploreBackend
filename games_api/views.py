from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer
from .models import Game
from .rapid_api_helper import get_json
import json
import datetime

class GetNewTrendingGames(APIView):
    def get(self, request):
        
        toDate = datetime.datetime.now().date()
        fromDate = toDate - datetime.timedelta(days=365)
        query = f'dates={fromDate},{toDate}&ordering=-rating&page_size=10'
        print(query)
        results = get_json('games', query)['results']
        #games = []

        # print(results)

        # for game_object in json.loads(json.dumps(results)):
        #     games.append(get_serialized_result(game_object, True))

        return Response(get_serialized_result(results, True))
       

class GetGame(APIView):
    def get(self, request, id):

        endpoint = f'games/{id}'
        game = get_json(endpoint)        
       
        return Response(get_serialized_result(game))


def get_serialized_result(json, many=False):
    # game = Game(json['id'], 
    #     json['name'], 
    #     json['background_image'], 
    #     json['released'], json['rating'],
    #     json['stores'])

    print(json)
    serializer = GameSerializer(data=json, many=True)
    serializer.is_valid()
    print(serializer.validated_data)
    return serializer.validated_data