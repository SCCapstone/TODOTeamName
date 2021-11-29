from django.db import models

# Create your models here.


class User(models.Model):
        Username = models.

class Recipe(models.Model):
        recipe_name = models.CharField(max_length=200)
        recipe_ingredients = 
        date_added = models.DateTimeField('date published')
        #TODO- add user to recipe?
        #TODO- allergy flags?

class forumPost(models.Model):
        #TODO-add user to database
        title = models.CharField(max_length=200)
        intro = models.CharField(max_length=200)
        date_added = models.DateTimeField('date published')

class groceryItems(models.Model):
        name = models.CharField(max_length=50)
