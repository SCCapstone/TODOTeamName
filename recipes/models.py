from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class allergies(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    """Recipe object, keeps track of recipe related data"""
    recipe_name = models.CharField(max_length=200)
    recipe_ingredients = models.TextField(max_length=100)
    recipe_directions = models.TextField(max_length=100)
    recipe_notes = models.TextField(max_length=100, default="")
    estimated_time = models.IntegerField()
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name
