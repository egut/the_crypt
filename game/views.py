"""
This describe all the views in the game
"""
from django.shortcuts import render, redirect
from django.contrib import auth

from .models import Game, Player
from .forms import PlayerForm

def index(request):

    return render(request, 'index.html', {
        'games': Game.objects.all(),
    })


def join(request, game_id):
    this_game = Game.objects.get(id=game_id)
    if request.method == "POST":
        pass

    else:
        form = PlayerForm()

    return render(request, 'join.html', {
        'game': this_game,
        'form': form
    })


def game(request, game_id):
    this_game = Game.objects.get(id=game_id)
    player = Player.objects.filter(
        game=this_game)
    if player:
        return render(request, 'game.html', {
            'game': this_game,
            'player': player
        })

    return redirect(join, game_id=game_id)
