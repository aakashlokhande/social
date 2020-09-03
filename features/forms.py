from django import forms
from .models import Suggestion


class SuggestionsForm(forms.ModelForm):

    class Meta:
        model=Suggestion
        fields=['suggestion','user']
        exclude=('user',)