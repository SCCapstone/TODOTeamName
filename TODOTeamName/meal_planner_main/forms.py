from django import forms
from .models import *

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = GroceryList
        fields = "__all__"

class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ['name', 'email', 'body']