from django.shortcuts import render
from .models import Submission

# Create your views here.
def game(req):
    return render(req, "index.html")


def leaderboard_view(req):
    objs = Submission.objects.all().order_by("-total")
    return render(req, "leaderboard.html", {"lst": objs})
