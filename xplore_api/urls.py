from django.contrib import admin
from django.urls import path, include
from games_api import urls
from rest_framework import routers
from users_API import views as user_views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'groups', user_views.GroupViewSet)

urlpatterns = [
    path('api/', include(urls)),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='api_token_auth'),  # generating token if correct username and password combination has been picked 
    path('logout/', user_views.logout)
]
