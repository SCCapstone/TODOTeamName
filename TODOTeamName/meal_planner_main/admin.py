from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import *
from meal_planner_main.models import ScheduledRecipe

admin.site.register(ScheduledRecipe)
admin.site.register(GroceryList)
admin.site.register(Post)