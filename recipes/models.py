from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class allergies(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    #author = models.ManyToManyField(User, related_name='recipe_list')
    recipe_name = models.CharField(max_length=200)
    recipe_ingredients = models.TextField(max_length=100)
    recipe_directions = models.TextField(max_length=100)
    estimated_time = models.IntegerField()
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name
    #allergens_in_item = models.ManyToManyField(
    #    allergies, related_name='recipes_with_allergens')
    # TODO- allergy flags?
