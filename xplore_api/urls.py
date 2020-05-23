from django.contrib import admin
from django.urls import path, include
from games_api import urls as games_api_urls
from users_api import urls as users_api_urls

urlpatterns = [
    path('games/', include(games_api_urls)),
    path('users/', include(users_api_urls)),
    path('admin/', admin.site.urls),
]
