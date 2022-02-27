from pyexpat import model
from django.db import models

# Create your models here.

# leonard/models.py
class ArtPiece(models.Model):
    title = models.CharField(max_length=100)
    decription = models.CharField(max_length=500)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

    