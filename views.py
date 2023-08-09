from django.shortcuts import render
from .game import Game

def game_view(request):
    game = Game(10, 10)
    context = {
        'game': game,
    }
    return render(request, 'game.html', context)
