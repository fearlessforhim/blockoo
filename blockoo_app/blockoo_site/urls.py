from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gameAction/<int:board_id>/getBoardState/', views.getBoardState, name='getBoardState'),
    path('gameAction/<int:board_id>/getPlayers/', views.getBoardPlayers, name='getBoardPlayers'),
    path('gameAction/<int:board_id>/placePiece/', views.placePiece, name='placePiece'),
    path('gameAction/<int:board_id>/gameReset/', views.gameReset, name='gameReset'),
    path('gameAction/<int:board_id>/finishPlayer/', views.finishPlayer, name='finishPlayer')

]