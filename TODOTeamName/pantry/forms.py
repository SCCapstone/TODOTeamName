from django import forms

from .models import *


class PantryAddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    expiration = forms.DateField()

    class Meta:
        model = pantryItems
        fields = ['name', 'expiration']
