from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    slug = serializers.CharField(max_length=50)

class StoresSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    url = serializers.CharField(max_length=2048, required=False)
    store = StoreSerializer(required=False)

class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    background_image = serializers.CharField(max_length=2048)
    released = serializers.CharField(max_length=20)
    rating = serializers.FloatField()
    stores = StoresSerializer(many=True, required=False)