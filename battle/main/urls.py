from . import views
from django.urls import path

urlpatterns = [
    path("game", views.game, name="game"),
    path("leaderboard", views.leaderboard_view, name="leaderboard"),
    path("how_to_play", views.how_to_play, name="howtoplay"),
    path("", views.index, name="index"),
]
