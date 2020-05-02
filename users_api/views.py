# from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.response import Response
from users_api.serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited. Also covers for the logout
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]
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
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
