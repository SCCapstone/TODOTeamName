from django.db import models

class ScheduledRecipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # recipeId = models.CharField(max_length= 200)
    scheduled_date = models.DateField()