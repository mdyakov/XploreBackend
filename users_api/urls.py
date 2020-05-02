from django.urls import path, include
from rest_framework import routers
from users_api import views as user_views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'', user_views.UserViewSet, basename='user')

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),  # generating token if correct username and password combination has been picked 
    path('', include(router.urls)),
]