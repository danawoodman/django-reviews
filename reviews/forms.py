from django import forms
from django.forms import ModelForm

from reviews.models import Review


class ReviewForm(ModelForm):
    """
    The Review add/edit form.
    """
    score = forms.IntegerField(required=True, max_value=5)
    content = forms.CharField(required=True, help_text='', widget=forms.Textarea)
        
    class Meta:
        model = Review
        fields = (
            'score',
            'content',
        )