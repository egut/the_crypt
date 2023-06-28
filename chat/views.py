from django.shortcuts import render

from chat.models import Room
from game.models import Game, Player, Phalanx, Figure, FigureSet

def get_phalanx(user, game_id):
    player = Player.objects.get(user=user, game_id=game_id)
    return Figure.objects.filter(figure_set=player.figure_set).values_list('phalanx__name', flat=True)



def index_view(request, game_id):
    rooms = ['Anonym']
    rooms += get_phalanx(request.user, game_id)

    return render(request, 'chats.html', {
        'rooms': rooms,
        'game_id':game_id,
    })


def room_view(request, game_id, room_name):
    this_game = Game.objects.get(id=game_id)
    chat_room, created = Room.objects.get_or_create(
        game=this_game, name=room_name)

    return render(request, 'room.html', {
        'room': chat_room,
        'game': this_game,
    })
