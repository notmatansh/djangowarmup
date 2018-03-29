from django.db import models


class User(models.Model):
    name = models.CharField(unique=True, max_length=100)
    score = models.IntegerField(default=0)


class Game(models.Model):
    current_player = models.ForeignKey(User, related_name='pending_turns', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_play = models.DateTimeField(auto_now=True)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=100, blank=True)
    player = models.ForeignKey(User, related_name='moves', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='moves', on_delete=models.CASCADE)
