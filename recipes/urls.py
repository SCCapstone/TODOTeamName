from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('recipeMain', views.recipes, name='recipesMain'),
    path('search', views.rsearch, name='rsearch'),
    path('createRecipe', views.rcreate, name='rcreate'),
    path('viewRecipe/<int:recipe_id>', views.rview, name='rview',),
    path('editRecipe', views.redit, name='redit'),
    path('scheduleRecipe', views.sched, name='sched'),
]
