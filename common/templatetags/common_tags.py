from random import randint
from django import template

from reviews.models import Review

register = template.Library()
    
@register.inclusion_tag('common/review.html')
def featured_review():
    featured_reviews = Review.objects.filter(tag__slug='featured')
    
    count = featured_reviews.count()
    if count > 0:
        i = randint(0, count - 1)
        review = featured_reviews[i]
        return {'review': review}
    else:
        return {
            'review': {
                'comment': 'No featured reviews at the moment',
            }
        }