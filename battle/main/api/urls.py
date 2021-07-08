from django.urls import path
from . import views

urlpatterns = [
    path("submit", views.SubmitGameView.as_view()),
    path("all", views.GetAllSubmissionsView.as_view()),
]
