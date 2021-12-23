from django.urls import path 

from . import views 

app_name = 'grocery'
urlpatterns = [
    path('', views.groceryListMain, name = 'groceryMain'),
    # path('addGroceryItem/', views.groceryListView, name = 'gadd'),
    # path('deleteGroceryItem/', views.remove, name="deleteGI"),
]