from django import forms

from .models import *


class PantryAddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    expiration = forms.DateField()
    userid = forms.CharField(max_length=150, widget = forms.HiddenInput(), required = False)

    class Meta:
        model = pantryItems
        fields = ['name', 'expiration', 'userid']

