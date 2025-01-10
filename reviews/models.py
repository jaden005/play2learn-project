from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug

class Review(models.Model):
    comment = models.TextField(max_length=200)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('reviews:detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.comment