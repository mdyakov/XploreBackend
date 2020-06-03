from django.contrib.auth.models import User
from .models import Wishlist, Game, Favorites, Friends, ProfilePicture
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
        ProfilePicture.objects.create(user=user)
        return user
    def to_representation(self, obj):
        ret = super(UserSerializer, self).to_representation(obj)
        ret.pop('password')
        return ret 

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'groups']


class ProfilePictureSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    def to_representation(self, obj):
        ret = super(ProfilePictureSerializer, self).to_representation(obj)
        ret.pop('user')
        return ret
    class Meta:
        model = ProfilePicture
        fields = ('image', 'user')

class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'name', 'poster_url']


class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    games = GameSerializer(default=None,required=False, many=True)
    user = UserSerializer(read_only=True)
    def to_representation(self, obj):
        ret = super(WishlistSerializer, self).to_representation(obj)
        ret.pop('user')
        return ret 
    class Meta:
        model = Wishlist
        fields = ['user','games']


class FavoritesSerializer(serializers.HyperlinkedModelSerializer):
    games = GameSerializer(default=None,required=False, many=True)
    user = UserSerializer(read_only=True)
    def to_representation(self, obj):
        ret = super(FavoritesSerializer, self).to_representation(obj)
        ret.pop('user')
        return ret 
    class Meta:
        model = Favorites
        fields = ['user','games']

class FriendsSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    friends = UserSerializer(default=None, required=False, many=True)
    def to_representation(self, obj):
        ret = super(FriendsSerializer, self).to_representation(obj)
        ret.pop('user')
        return ret 
    class Meta:
        model = Friends
        fields = ['user', 'friends']