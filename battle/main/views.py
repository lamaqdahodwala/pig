from django.shortcuts import render
from .models import Submission

# Create your views here.
def game(req):
    return render(req, "game.html")


def leaderboard_view(req):
    objs = Submission.objects.all().order_by("-total")
    return render(req, "leaderboard.html", {"lst": objs})


def index(req):
    return render(req, "index.html")


def how_to_play(req):
    return render(req, "how_to_play.html")
