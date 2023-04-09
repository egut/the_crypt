from django.urls import path

from . import views

urlpatterns = [
    path('<int:game_id>/', views.index_view, name='chat-index'),
    path('<int:game_id>/<str:room_name>/', views.room_view, name='chat-room'),
]
