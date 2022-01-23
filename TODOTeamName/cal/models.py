from django.db import models
from django.urls import reverse


class ScheduledRecipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # recipeId = models.CharField(max_length= 200)
    scheduled_date = models.DateField()

    @property
    def get_html_url(self):
        url = reverse('cal:scheduled_recipe_edit', args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'
