from django.contrib import admin
from django.urls import path, include
from games_api import urls

urlpatterns = [
    path('api/', include(urls)),
    path('admin/', admin.site.urls)
]
