from dal import autocomplete
from django import forms
from django.db import models

from .models import *

class GroceryItemsForm(forms.ModelForm):
    class Meta:
        model = groceryItems
        fields = ['item_name', 'quantity']
        widgets = {
                'item_name': autocomplete.ModelSelect2(url='grocery:ingredient-autocomplete'),
        }

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = GroceryList
        fields = "__all__"


class GroceryAddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        model = groceryItems
        fields = ['name', 'quantity']
