from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='game_list'),
    path('<int:game_id>/', views.game, name='game_index'),
    path('<int:game_id>/join', views.join, name='game_join'),
]
