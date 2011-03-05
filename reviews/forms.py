from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from reviews.models import ReviewedItem


class ReviewedItemForm(ModelForm):
    """
    The ReviewedItem add/edit form.
    """
    SCORE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    score = forms.ChoiceField(label=_('Rating'), required=True, 
        choices=SCORE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'star'}))
    content = forms.CharField(label=_('Review'), required=True, help_text='', widget=forms.Textarea)
        
    class Meta:
        model = ReviewedItem
        fields = (
            'score',
            'content',
        )