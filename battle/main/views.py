from django.shortcuts import render
from .models import Submission

# Create your views here.
def index(req):
    return render(req, "index.html")

def leaderboard_view(req):
    objs = Submission.objects.all()
    return render(req, 'leaderboard.html', {'lst': objs})