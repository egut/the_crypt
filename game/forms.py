"""
    Game forms that will be used.
"""

from django.forms import ModelForm
from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["name", "profile"]
