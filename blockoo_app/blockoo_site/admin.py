from django.contrib import admin
from blockoo_site.models import BoardState
from blockoo_site.models import Piece
from blockoo_site.models import Player
from blockoo_site.models import PlayerPiece

admin.site.register(BoardState)
admin.site.register(Piece)
admin.site.register(Player)
admin.site.register(PlayerPiece)