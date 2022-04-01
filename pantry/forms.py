from dal import autocomplete
from django import forms

from .models import *


class PantryAddItemForm(forms.ModelForm):
    class Meta:
        model = pantryItems
        fields = ['name', 'quantity', 'expiration']
        widgets = {
            'name': autocomplete.ModelSelect2(url='grocery:ingredient-autocomplete'),
            'expiration': forms.DateInput(attrs={'type': 'date'}),
        }

