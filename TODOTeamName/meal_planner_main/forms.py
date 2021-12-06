from django import forms
from django.db import models
from .models import *

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = GroceryList
        fields = "__all__"

class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ['name', 'email', 'body']

class PantryAddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    expiration = forms.DateField()

    class Meta:
        model = pantryItems 
        fields = ['name', 'expiration']

class GroceryAddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        model = groceryItems
        fields = ['name', 'quantity']