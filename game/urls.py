from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.game, name='game-index'),
    path('<int:game_id>/join', views.join, name='game-join'),
]
