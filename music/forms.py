from django import forms

from .models import music

class musicForm(forms.ModelForm):
    class Meta:
        model=music
        fields=['title','artist']
