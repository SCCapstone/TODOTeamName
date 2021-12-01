from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.

class groceryItems(models.Model):
        name = models.CharField(max_length=50)
        quantity = models.PositiveSmallIntegerField(default=0)

class allergies(models.Model):
        name = models.CharField(max_length=100)

class siteUser(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        grocery_list = models.ManyToManyField(groceryItems, related_name='users_who_own')
        pantry_list = models.JSONField(null=True)
        allergy_list = models.ManyToManyField(allergies, related_name='allergic_users')
        #TODO - isaac - Add friends list
        #TODO - isaac - add Allergies


class Recipe(models.Model):
        author = models.ManyToManyField(siteUser, related_name='recipe_list')
        recipe_name = models.CharField(max_length=200)
        recipe_ingredients = models.JSONField(null=True) 
        date_added = models.DateTimeField('date published')
        allergens_in_item = models.ManyToManyField(allergies, related_name = 'recipes_with_allergens')
        #TODO- allergy flags?

class forumPost(models.Model):
        author = models.ForeignKey(siteUser, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        intro = models.CharField(max_length=200)
        date_added = models.DateTimeField('date published')
        slug = models.CharField(max_length=200)

class ScheduledRecipe(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        recipeId = models.CharField(max_length= 200)
        scheduled_date = models.DateField()
