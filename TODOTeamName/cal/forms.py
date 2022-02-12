from django.forms import ModelForm, DateInput

from .models import *


class ScheduledRecipeForm(ModelForm):
    class Meta:
        model = ScheduledRecipe
        widgets = {
            'scheduled_date': DateInput(attrs={'type': 'date'}),
        }
        fields = ['title', 'description', 'scheduled_date']
