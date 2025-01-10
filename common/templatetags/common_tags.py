import random
from django import template

from reviews.models import Review

register = template.Library()

@register.inclusion_tag('common/review.html')
def random_review():
    count = Review.objects.count()
    if count > 0:
        i = random.randint(0, count-1)
        review = Review.objects.all()[i]
        return {'review': review}
    else:
        return {
            'review': {
                'comment': 'No reviews at the moment',
            }
        }