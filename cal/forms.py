from django.forms import ModelForm, DateInput, ModelChoiceField

from .models import *


class ScheduledRecipeForm(ModelForm):
    recipe = ModelChoiceField(queryset=Recipe.objects.none())
    class Meta:
        model = ScheduledRecipe
        widgets = {
            'scheduled_date': DateInput(attrs={'type': 'date'}),
        }
        fields = ['recipe', 'scheduled_date']
