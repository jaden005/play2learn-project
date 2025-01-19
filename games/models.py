from django.conf import settings
from django.db import models

from common.utils.text import unique_slug

class GameScore(models.Model):

    MATH = "MATH"
    ANAGRAM = "ANAGRAM"

    GAME_CHOICES = [
        {MATH, "Math Facts"},
        {ANAGRAM, "Anagram Hunt"}
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField(default=1, editable=True)
    max_number = models.IntegerField(
        default=1,
        editable=True,
        )
    operation = models.CharField(max_length=30, editable=True)
    end_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)