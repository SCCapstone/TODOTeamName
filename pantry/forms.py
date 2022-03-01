from django import forms

from .models import *


class PantryAddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50)

    class Meta:
        model = pantryItems
        widgets = {
            'expiration': forms.DateInput(attrs={'type': 'date'})
        }
        fields = ['name', 'expiration']

