from typing import Any
from django.contrib import admin
from .models import GameScore

@admin.register(GameScore)                 
class GameScoreAdmin(admin.ModelAdmin):
    model = GameScore,
    list_display = ['id', 'user','game','score', 'max_number', 'operation', 'end_time', 'slug']