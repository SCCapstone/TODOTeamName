from django.db import models
from django.contrib.auth.models import User


class allergies(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    author = models.ManyToManyField(User, related_name='recipe_list')
    recipe_name = models.CharField(max_length=200)
    recipe_ingredients = models.JSONField(null=True)
    date_added = models.DateTimeField('date published')
    allergens_in_item = models.ManyToManyField(
        allergies, related_name='recipes_with_allergens')
    # TODO- allergy flags?
