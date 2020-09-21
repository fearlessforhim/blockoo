from django.db import models

class PieceModel(models.Model):
    key = models.CharField(max_length=4)

    def __str__(self):
        return self.key