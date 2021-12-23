from django.db import models


class groceryItems(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name + " (" + str(self.quantity) + ")"


class GroceryList(models.Model):
    item_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    calories = models.IntegerField()
    item_id = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.item_name
