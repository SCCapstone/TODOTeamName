from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class foodIngredient(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class groceryItems(models.Model):
    item_name = models.ForeignKey(foodIngredient, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name.name + " (" + str(self.quantity) + ")"


class GroceryList(models.Model):
    item_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    calories = models.IntegerField()
    item_id = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.item_name

