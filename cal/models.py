from django.conf import settings
from django.db import models
from django.urls import reverse
from recipes.models import Recipe 


class ScheduledRecipe(models.Model):
    scheduled_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    @property
    def get_html_url(self):
        url = reverse('cal:scheduled_recipe_edit', args=(self.id,))
        return f'<a href="{ url }">{ self.recipe }</a>'

    @property 
    def get_delete_url(self):
        url = reverse('cal:scheduled_recipe_delete', args=(self.id,))
        return f'<a href="{ url }"><button type="button" class="btn-close" aria-label="Close"></button></a>'