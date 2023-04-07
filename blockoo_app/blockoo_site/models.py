from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class BoardState(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    activePlayerInGameId = models.IntegerField(null=True)
    boardState = models.TextField(null=True)
    gameIsOver = models.BooleanField(null=False, default=False)

    def save(self, *args, **kwargs):
        super(BoardState, self).save(*args, **kwargs)

class Piece(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=5)

    def save(self, *args, **kwargs):
        super(Piece, self).save(*args, **kwargs)

class Player(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    inGameId = models.IntegerField(null=True)
    color = models.CharField(max_length=10, null=True)
    board = models.ForeignKey(BoardState, on_delete=models.DO_NOTHING)
    isFinished = models.BooleanField(null=False, default=False)

    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)

class PlayerPiece(models.Model):
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    piece = models.ForeignKey(Piece, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        super(PlayerPiece, self).save(*args, **kwargs)


