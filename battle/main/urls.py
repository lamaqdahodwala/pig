from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("leaderboard", views.leaderboard_view, name="leaderboard"),
]
