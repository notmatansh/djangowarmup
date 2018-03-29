from django.shortcuts import render
from .models import Game


def get_games(request):
    for game in Game.objects.iterator():

