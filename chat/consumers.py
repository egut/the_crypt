"""
Handle WS for chat messages
"""
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from game.models import Game, Player
from .models import Room, Message

class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.game = None
        self.room_group_name = None
        self.room = None
        self.player = None

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.game = Game.objects.get(
            id=self.scope['url_route']['kwargs']['game_id'])

        self.room_group_name = f'chat_{self.room_name}'
        self.room = Room.objects.get(
            name=self.room_name,
            game=self.game)
        self.user = self.scope['user']
        self.player = Player.objects.get(
            user = self.user,
            game = self.game)
        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        # send the user list to the newly joined user
        self.send(json.dumps({
            'type': 'player_list',
            'players': [player.name for player in self.room.online.all()],
        }))

        if self.user.is_authenticated:

            # send the join event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'player_join',
                    'player': self.player.name,
                }
            )
            self.room.online.add(self.player)


    def disconnect(self, close_code):
        del close_code
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        if self.user.is_authenticated:

            # send the leave event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'player_leave',
                    'user': self.player.name,
                }
            )
            self.room.online.remove(self.player)


    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if not self.user.is_authenticated:
            return

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'player': self.player.name,
                'message': message,
            }
        )
        Message.objects.create(player=self.player, room=self.room, content=message)

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

    def player_join(self, event):
        self.send(text_data=json.dumps(event))

    def player_leave(self, event):
        self.send(text_data=json.dumps(event))

