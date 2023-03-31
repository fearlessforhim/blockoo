from django.db import models

class BoardModel(models.Model):
    boardState = models.TextField()
    currentPlayer = models.IntegerField()


    def __str__(self):
        return self.boardState