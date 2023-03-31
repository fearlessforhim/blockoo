from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getBoardState/<int:board_id>', views.getBoardState, name='getBoardState'),
    path('getPlayers/<int:board_id>', views.getBoardPlayers, name='getBoardPlayers'),
    path('placePiece/<int:board_id>', views.placePiece, name='getBoardPlayers')

]