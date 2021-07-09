from . import views
from django.urls import path

urlpatterns = [
    path("game", views.game, name="index"),
    path("leaderboard", views.leaderboard_view, name="leaderboard"),
]
