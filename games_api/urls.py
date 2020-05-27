from django.urls import path, include
from . import views

urlpatterns = [
    path('trending', views.GetNewTrendingGames.as_view()),
    path('<int:id>', views.GetGame.as_view()),
    path('search', views.SearchGames.as_view()),
    path('platforms', views.GetPlatforms.as_view()),
    path('stores', views.GetStores.as_view()),
    path('genres', views.GetGenres.as_view()),
    path('recommendations/<int:id>', views.GetRecommendations.as_view())
]