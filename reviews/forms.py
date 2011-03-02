from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from reviews.models import Review


class ReviewForm(ModelForm):
    """
    The Review add/edit form.
    """
    score = forms.IntegerField(label=_('Rating'), required=True, max_value=5)
    content = forms.CharField(label=_('Review'), required=True, help_text='', widget=forms.Textarea)
        
    class Meta:
        model = Review
        fields = (
            'score',
            'content',
        )