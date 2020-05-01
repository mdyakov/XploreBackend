# from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.response import Response
from users_API.serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.TokenAuthentication,)
    # def list(self, request):
    #     queryset = User.objects.all().order_by('-date_joined')
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    @action(detail=False, methods=['POST'])
    def logout(self, request):
        print("hi")
    # @action(detail=True, username='')
    # def retrieve(self, request, pk=None):
    #     # print(username)
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, username='maruf')
    #     user
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)


@api_view(('POST',))
def logout(request):
    authentication_classes = (authentication.TokenAuthentication,)
    print("hi")
    print(request.content_type)
    from rest_framework.authtoken.models import Token
    user = Token.objects.get(key='54e4435c4e43d223f8939fe276870c7848ca1fe8').user
    print(user.auth.token)
    try:
        request.user.auth_token.delete()
        print(request.user.auth_token)

    except(AttributeError, ObjectDoesNotExist):
        pass
    # logout(request)
    return Response(data={"success": "Successfully logged out."},
                    status=status.HTTP_200_OK)