from django.contrib import admin
from django.urls import path, include
from games_api import urls as games_api_urls
from users_api import urls as users_api_urls
from . import settings 
urlpatterns = [
    path('games/', include(games_api_urls)),
    path('users/', include(users_api_urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)