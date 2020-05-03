from django.urls import path, include
from . import views

urlpatterns = [
    path('games/new/trending', views.GetNewTrendingGames.as_view()),
    path('games/<int:id>', views.GetGame.as_view()),
    path('recommendations/<int:id>', views.GetRecommendations.as_view())
]