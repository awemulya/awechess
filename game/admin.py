from django.contrib import admin

from .models import Player, GameData, Move

admin.site.register(Player)
admin.site.register(GameData)
admin.site.register(Move)
