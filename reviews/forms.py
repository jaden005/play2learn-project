from django.forms import ModelForm, Textarea

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
        widgets = {
            'comment': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            )
        }
        help_texts = {
            'comment': 'No cursing please.'
        }