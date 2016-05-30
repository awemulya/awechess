from __future__ import unicode_literals

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=256)


class GameData(models.Model):
    event = models.CharField(max_length=256)
    site = models.CharField(max_length=256)
    date = models.DateField()
    round = models.FloatField()
    white = models.ForeignKey(Player, related_name='white')
    black = models.ForeignKey(Player, related_name='black')
    result = models.CharField(max_length=10)
    white_elo = models.IntegerField()
    black_elo = models.IntegerField()
    eco = models.CharField(max_length=10)
    event_date = models.DateField()


class Moves(models.Model):
    game = models.ForeignKey(GameData, related_name='moves')
    move_no = models.IntegerField()
    white = models.CharField(max_length=10)
    black = models.CharField(max_length=10)