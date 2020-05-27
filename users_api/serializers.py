from django.contrib.auth.models import User
from .models import Wishlist, Game, Favorites, Friends
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(  # Required for retrieving Users based on Username rather than id
        view_name='user-detail',
        lookup_field='username'
    )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Wishlist.objects.create(user=user)
        Favorites.objects.create(user=user)
        Friends.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'groups']

class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'name', 'poster_url']


class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    games = GameSerializer(default=None,required=False, many=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Wishlist
        fields = ['user','games']


class FavoritesSerializer(serializers.HyperlinkedModelSerializer):
    games = GameSerializer(default=None,required=False, many=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Favorites
        fields = ['user','games']

class FriendsSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    friends = UserSerializer(default=None, required=False, many=True)
    class Meta:
        model = Friends
        fields = ['user', 'friends']