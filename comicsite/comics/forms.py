from django import forms
from .models import Concept

class ConceptForm(forms.ModelForm):
    description = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),
            max_length=4000
            )
    characters = forms.CharField(
            widget=forms.NumberInput(),
            required=False
            )
    conversation = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),
            max_length=4000, required=False
            )
    class Meta:
        model = Concept
        fields = ['title', 'description', 'characters_no', 'conversation']
