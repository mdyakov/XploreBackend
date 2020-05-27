# from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.response import Response
from users_api.serializers import UserSerializer, GameSerializer, WishlistSerializer, FavoritesSerializer, FriendsSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from .permissions import IsOwner
from .models import Game, Favorites, Wishlist, Friends


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited. Also covers for the logout
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [IsOwner]  # [permissions.IsAuthenticated, IsOwner]
    authentication_classes = (authentication.TokenAuthentication,)
    @action(detail=False, methods=['POST'], url_path='logout', url_name='logout')
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except(AttributeError, ObjectDoesNotExist):
            pass
        return Response(data={"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='me', url_name='me')
    def get_token_user(self, request):
        # print(request.user)
        serializer_context = {
            'request': request,
        }
        user = Token.objects.get(key=request.user.auth_token).user
        print(user)
        return JsonResponse(UserSerializer(instance=user, context=serializer_context).data, safe=False)

    @action(detail=True, methods=['GET', 'POST', 'DELETE'], url_path='wishlist', url_name='wishlist')
    def wishlist(self, request, username=None):
        token_user = User.objects.get(username=request.user.username)
        friends_list = Friends.objects.get(user=token_user)
        user = User.objects.get(username=username)
        if request.user.username != username:
            return Response(data={"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        elif user in friends_list.friends.all():
            wishlist = Wishlist.objects.get(user=user)
            return JsonResponse(WishlistSerializer(instance=wishlist, context=serializer_context).data, safe=False)
        
        wishlist = Wishlist.objects.get(user=user)
        serializer_context = {
            'request': request,
        }
        print(request.method)
        if request.method == 'POST':
            game, exists = Game.objects.get_or_create(id=request.data['id'],
                                                  name=request.data['name'],
                                                  poster_url=request.data['poster_url'])
            wishlist.games.add(game)
        elif request.method == 'DELETE':
            game = Game.objects.get(id=request.data['id'])
            wishlist.games.remove(game)
            wishlist.save()
        wishlist = Wishlist.objects.get(user=user)
        print(wishlist.games)
        return JsonResponse(WishlistSerializer(instance=wishlist, context=serializer_context).data, safe=False)

    @action(detail=True, methods=['GET', 'POST', 'DELETE'], url_path='favorites', url_name='favorites')
    def get_favorites(self, request, username=None):
        token_user = User.objects.get(username=request.user.username)
        friends_list = Friends.objects.get(user=token_user)
        user = User.objects.get(username=username)
        print("??",user not in friends_list.friends.all())
        if request.user.username != username:
            return Response(data={"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        elif user in friends_list.friends.all():
            favorites = Favorites.objects.get(user=user)
            return JsonResponse(FavoritesSerializer(instance=favorites, context=serializer_context).data, safe=False)  
        
        favorites = Favorites.objects.get(user=user)
        serializer_context = {
            'request': request,
        }
        print(request.method)
        if request.method == 'POST':
            game, exists = Game.objects.get_or_create(id=request.data['id'],
                                                  name=request.data['name'],
                                                  poster_url=request.data['poster_url'])
            print(game)
            favorites.games.add(game)
        elif request.method == 'DELETE':
            game = Game.objects.get(id=request.data['id'])
            favorites.games.remove(game)
            favorites.save()
        favorites = Favorites.objects.get(user=user)
        return JsonResponse(FavoritesSerializer(instance=favorites, context=serializer_context).data, safe=False)

    @action(detail=True, methods=['GET', 'POST', 'DELETE'], url_path='friends', url_name='friends')
    def get_friends(self, request, username=None):
        if request.user.username != username:
            return Response(data={"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.get(username=username)
        friends_list = Friends.objects.get(user=user)
        serializer_context = {
            'request': request,
        }
        if request.method == 'POST':
            friend = User.objects.get(username=request.data['username'])
            print(friend)
            friends_list.friends.add(friend)
        elif request.method == 'DELETE':
            friend = User.objects.get(username=request.data['username'])
            friends_list.friends.remove(friend)
            friends_list.save()
        
        return JsonResponse(FriendsSerializer(instance=friends_list, context=serializer_context).data, safe=False)


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    