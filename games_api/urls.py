from django.urls import path, include
from . import views

urlpatterns = [
    path('new/trending', views.GetNewTrendingGames.as_view()),
    path('<int:id>', views.GetGame.as_view()),
    path('recommendations/<int:id>', views.GetRecommendations.as_view())
]