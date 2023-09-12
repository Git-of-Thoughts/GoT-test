from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Pin(models.Model):
    image = models.ImageField(upload_to='pins/')
    description = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followee = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
