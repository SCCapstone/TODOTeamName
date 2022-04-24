from django.forms import ModelForm, DateInput, ModelChoiceField

from .models import Recipe, ScheduledRecipe


class ScheduledRecipeForm(ModelForm):
    """A ModelForm to schedule a recipe on a specified date."""

    recipe = ModelChoiceField(queryset=Recipe.objects.none())

    class Meta:
        model = ScheduledRecipe
        widgets = {
            'scheduled_date': DateInput(attrs={'type': 'date'}),
        }
        fields = ['recipe', 'scheduled_date']
