"""
Chat model
"""


from django.db import models
from game.models import Player, Game


class Room(models.Model):
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=Player, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=30,
        choices=[
        ('ANONYMOUS','Anonym chat'),
        ('FIGURE','Figure chat'),
        ('PLAYER','Player chat')])

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.type})'


class Message(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.player.name}: {self.content} [{self.timestamp}]'
