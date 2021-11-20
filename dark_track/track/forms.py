from django import forms
from django.forms import ClearableFileInput

from .models import Track


class TractorTrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['processing_area', ]
        widgets = {
            'processing_area': ClearableFileInput(attrs={'multiple': True}),
        }
