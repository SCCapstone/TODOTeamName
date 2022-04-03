from django.urls import path

from . import views

app_name = 'pantry'
urlpatterns = [
    path('', views.pantry, name='pantryMain'),
    path('pantryeditdelete', views.pantryeditdelete,name='pantryEditDelete'), 
    path('edit/<int:id>/', views.edit, name='edit'),
    # path('addPantryItem/', views.addPantryItem),
    #path('editPantryItem/', views.edit, name="editPI"),
    #path('deletePantryItem/', views.remove, name="deletePI"),
]
