from rest_framework import serializers

class ClipSerializer(serializers.Serializer):
    clip = serializers.CharField(max_length=2048, required=False)

class RatingsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    count = serializers.IntegerField()
    percent = serializers.FloatField()

class GenresSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=50)

class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)

class StoresSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    url = serializers.CharField(max_length=2048, required=False)
    store = StoreSerializer(required=False)

class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=2048, required=False)
    background_image = serializers.CharField(max_length=2048)
    background_image_additional = serializers.CharField(max_length=2048, required=False)
    released = serializers.CharField(max_length=20)
    rating = serializers.FloatField()
    stores = StoresSerializer(many=True, required=False)
    genres = GenresSerializer(many=True, required=False)
    ratings = RatingsSerializer(many=True, required=False)
    rating = serializers.FloatField()
    clip = ClipSerializer(required=False, allow_null=True)

class GameRecommendationsSerializer(serializers.Serializer):
    metacritic = serializers.FloatField(allow_null=True)
    released = serializers.CharField(max_length=20)
    genres = GenresSerializer(many=True, required=False)
