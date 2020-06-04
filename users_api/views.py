# from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.response import Response
from users_api.serializers import UserSerializer, GameSerializer, WishlistSerializer, FavoritesSerializer, FriendsSerializer, ProfilePictureSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from .permissions import IsOwner
from .models import Game, Favorites, Wishlist, Friends, ProfilePicture
from rest_framework.exceptions import ParseError

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited. Also covers for the logout
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [IsOwner]  # [permissions.IsAuthenticated, IsOwner]
    authentication_classes = (authentication.TokenAuthentication,)
    
    def create(self, request, *args, **kwargs):
        super(UserViewSet, self).create(request, *args, **kwargs)
        return Response(data={"success": "Successfully created."},status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # super(UserViewSet, self).retrieve(request, *args, **kwargs)
        serializer_context = {
            'request': request,
        }
        try:
            user = User.objects.get(username=kwargs['username'])
        except:
            return Response( data={"detail": "Not found"},status=status.HTTP_404_NOT_FOUND)
        
        token_user = Token.objects.get(key=request.user.auth_token).user
        friends_list = Friends.objects.get(user=token_user)
        if not (token_user.username == user.username or user in friends_list.friends.all()):
            return Response(data={"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        
        wishlist = Wishlist.objects.get(user=user)
        favorites = Favorites.objects.get(user=user)
        friends = Friends.objects.get(user=user)
        profilePicture = ProfilePicture.objects.get(user=user)
        response = {}
        response['user'] = UserSerializer(instance=user, context=serializer_context).data
        response['favorites'] = FavoritesSerializer(instance=favorites, context=serializer_context).data
        response['wishlist'] = WishlistSerializer(instance=wishlist, context=serializer_context).data
        response['friends'] = FriendsSerializer(instance=friends, context=serializer_context).data
        response['profilePicture'] = ProfilePictureSerializer(instance=profilePicture, context=serializer_context).data
        return JsonResponse(response, safe=False)

    @action(detail=True, methods=['PATCH'], url_path='updatepass', url_name='updatepass')
    def update_password(self, request, username=None):
        user = User.objects.get(username=request.user.username)
        if request.user.username != username:
            return Response(data={"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        user.set_password(request.data['password'])
        user.save()
        return Response(data={"success": "Successfully changed password."},
                        status=status.HTTP_200_OK)
    @action(detail=True, methods=['PATCH'], url_path='profilepicture', url_name='profilepicture')
    def profile_picture(self, request, username=None):
        user = User.objects.get(username=request.user.username)
        if request.user.username != username:
            return Response(data={"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        profilePicture = ProfilePicture.objects.get(user=user)
        profilePicture.image = file
        profilePicture.save()
        return Response(data={"success": "Success!"},
                        status=status.HTTP_200_OK)

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
        wishlist = Wishlist.objects.get(user=user)
        favorites = Favorites.objects.get(user=user)
        friends = Friends.objects.get(user=user)
        profilePicture = ProfilePicture.objects.get(user=user)
        response = {}
        response['user'] = UserSerializer(instance=user, context=serializer_context).data
        response['favorites'] = FavoritesSerializer(instance=favorites, context=serializer_context).data
        response['wishlist'] = WishlistSerializer(instance=wishlist, context=serializer_context).data
        response['friends'] = FriendsSerializer(instance=friends, context=serializer_context).data
        response['profilePicture'] = ProfilePictureSerializer(instance=profilePicture, context=serializer_context).data
        return JsonResponse(response, safe=False)

    @action(detail=True, methods=['GET', 'POST', 'DELETE'], url_path='wishlist', url_name='wishlist')
    def wishlist(self, request, username=None):
        serializer_context = {
            'request': request,
        }
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
        serializer_context = {
            'request': request,
        }
        token_user = User.objects.get(username=request.user.username)
        friends_list = Friends.objects.get(user=token_user)
        user = User.objects.get(username=username)
        if request.user.username != username:
            return Response(data={"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        elif user in friends_list.friends.all():
            favorites = Favorites.objects.get(user=user)
            return JsonResponse(FavoritesSerializer(instance=favorites, context=serializer_context).data, safe=False)  
        
        favorites = Favorites.objects.get(user=user)
        serializer_context = {
            'request': request,
        }
        if request.method == 'POST':
            game, exists = Game.objects.get_or_create(id=request.data['id'],
                                                  name=request.data['name'],
                                                  poster_url=request.data['poster_url'])
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
            friends_list.friends.add(friend)
        elif request.method == 'DELETE':
            friend = User.objects.get(username=request.data['username'])
            friends_list.friends.remove(friend)
            friends_list.save()
        response =[]
        for friend in friends_list.friends.all():
            picture = ProfilePicture.objects.get(user=friend)
            cell = {}
            cell['user'] = UserSerializer(instance=user, context=serializer_context).data
            cell['picture'] = ProfilePictureSerializer(instance=picture, context=serializer_context).data
            response.append(cell)
            
        return JsonResponse(data=response, safe=False)


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    