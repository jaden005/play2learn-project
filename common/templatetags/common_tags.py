from random import randint
from django import template

from reviews.models import Review

register = template.Library()
    
@register.inclusion_tag('common/review.html')
def featured_reviews():
    featured_reviews = Review.objects.filter(tag__slug='featured')
    return {'reviews': featured_reviews}