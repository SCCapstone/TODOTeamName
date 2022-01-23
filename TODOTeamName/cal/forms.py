from django.forms import ModelForm, DateInput

from .models import *


class ScheduledRecipeForm(ModelForm):
    class Meta:
        model = ScheduledRecipe
        widgets = {
            'scheduled_date': DateInput(attrs={'type': 'date'}),
        }
        fields = '__all__'
