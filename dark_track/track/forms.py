from django import forms
from django.forms import ClearableFileInput

from .models import TractorTrack


class TractorTrackForm(forms.ModelForm):
    class Meta:
        model = TractorTrack
        fields = ['file', ]
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }
