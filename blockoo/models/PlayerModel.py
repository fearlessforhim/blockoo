from django.db import models

class PlayerModel(models.Model):
    color = models.CharField(max_length=6)
    remainingPieces = models.TextField()