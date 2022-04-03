from django.urls import path

from . import views

app_name = 'pantry'
urlpatterns = [
    path('', views.pantry, name='pantryMain'),
    # path('addPantryItem/', views.addPantryItem),
    #path('editPantryItem/', views.edit, name="editPI"),
    #path('deletePantryItem/', views.remove, name="deletePI"),
]
