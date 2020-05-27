from rest_framework import serializers

class ClipSerializer(serializers.Serializer):
    clip = serializers.CharField(max_length=2048, required=False, allow_null=True)

class RatingsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50, allow_null=True)
    count = serializers.IntegerField(allow_null=True)
    percent = serializers.FloatField(allow_null=True)

class GenresSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=50, allow_null=True)

class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50, allow_null=True)

class StoresSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    url = serializers.CharField(max_length=2048, required=False, allow_null=True)
    store = StoreSerializer(required=False, allow_null=True)

class PlatformSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50, allow_null=True)

class PlatformsSerializer(serializers.Serializer):
    platform = PlatformSerializer(required=False, allow_null=True)

class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=250, allow_null=True)
    description = serializers.CharField(max_length=2048, required=False, allow_null=True)
    background_image = serializers.CharField(max_length=2048, allow_null=True)
    background_image_additional = serializers.CharField(max_length=2048, required=False, allow_null=True)
    released = serializers.CharField(max_length=20, allow_null=True)
    stores = StoresSerializer(many=True, required=False, allow_null=True)
    parent_platforms = PlatformsSerializer(many=True, required=False, allow_null=True)
    genres = GenresSerializer(many=True, required=False, allow_null=True)
    ratings = RatingsSerializer(many=True, required=False, allow_null=True)
    rating = serializers.FloatField(allow_null=True)
    clip = ClipSerializer(required=False, allow_null=True)

class GamesResultsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField(max_length=2048, allow_null=True)
    previous = serializers.CharField(max_length=2048, allow_null=True)
    results = GameSerializer(many=True, allow_null=True, required=False)

class FilterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=250, allow_null=True)

class FiltersResultsSerializer(serializers.Serializer):
    results = FilterSerializer(many=True, allow_null=True, required=False)

class GameRecommendationsSerializer(serializers.Serializer):
    metacritic = serializers.FloatField(allow_null=True)
    released = serializers.CharField(max_length=20, allow_null=True)
    genres = GenresSerializer(many=True, required=False, allow_null=True)
