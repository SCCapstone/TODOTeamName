from django.urls import path
from django.conf.urls import url

from . import views
from .views import IngredientAutocomplete

app_name = 'grocery'
urlpatterns = [
    #path('groceryMain', views.groceryListMain, name='groceryMain'),
    # path('addGroceryItem/', views.groceryListView, name = 'gadd'),
    # path('deleteGroceryItem/', views.remove, name="deleteGI"),
    #path('editGroceryItem/', views.edit, name="editGI"),


    #path('viewGroceryItem', views.)
    path('', views.groceryListMain, name='groceryMain'),
    path('editdelete', views.editdelete, name='groceryEditDelete'),
    #path('editGroceryItem', views.editGroceryItem, name='gedit'),
    #path('groceryEdit/', views.GroceryListView.as_view(), name='groceryEdit'),
    url(
        r'^ingredient-autocomplete/$',
        IngredientAutocomplete.as_view(create_field='name'),
        name='ingredient-autocomplete',
    ),
    path('edit/<int:id>/', views.edit, name='edit')
]
