from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.recipes, name='recipesMain'),
    path('search', views.rsearch, name='rsearch'),
    path('createRecipe', views.rcreate, name='rcreate'),
    path('make', views.make, name='make'),
    path('viewRecipe', views.rview, name='rview',),
    path('editRecipe', views.redit, name='redit'),
]
