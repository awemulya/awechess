from __future__ import unicode_literals

from django.db import models


class FileHistory(models.Model):
    checksum = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)


class Player(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return '%s' % (self.name)


class GameData(models.Model):
    event = models.CharField(max_length=256)
    site = models.CharField(max_length=256)
    date = models.DateField(null=True)
    round = models.FloatField(null=True)
    white = models.ForeignKey(Player, related_name='white')
    black = models.ForeignKey(Player, related_name='black')
    result = models.CharField(max_length=10)
    white_elo = models.IntegerField()
    black_elo = models.IntegerField()
    eco = models.CharField(max_length=10)
    event_date = models.DateField(null=True)

    def __str__(self):
        return '%s -vs %s ' % (self.white.name, self.black.name)



class Move(models.Model):
    game = models.ForeignKey(GameData, related_name='moves')
    move_no = models.IntegerField()
    move = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % (self.move)

