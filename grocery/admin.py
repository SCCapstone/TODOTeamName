from django.contrib import admin
from .models import *

admin.site.register(groceryItems)
admin.site.register(GroceryList)
admin.site.register(foodIngredient)
