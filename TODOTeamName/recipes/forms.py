from django import forms

from .models import *


class AddRecipeForm(forms.ModelForm):
    recipe_name = forms.CharField(max_length=50)
    recipe_ingredients = models.TextField(max_length=200)
    recipe_directions = models.TextField(max_length=200)
    estimated_time = models.IntegerField()

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_ingredients', 'recipe_directions', 'estimated_time']

