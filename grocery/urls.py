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
    url(
        r'^ingredient-autocomplete/$',
        IngredientAutocomplete.as_view(),
        name='ingredient-autocomplete',
    ),
]
