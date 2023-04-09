"""
This describe all the views in the game
"""
from django.shortcuts import render
from .models import Game

def index(request):

    return render(request, 'index.html', {
        'games': Game.objects.all(),
    })

def game(request,game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'game.html', {
        'game': game,
    })
