"""
This describe all the views in the game
"""
from django.shortcuts import render

def index(request):

    # Page from the theme
    return render(request, 'game/index.html')
