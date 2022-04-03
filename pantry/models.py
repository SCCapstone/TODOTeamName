from django.conf import settings
from django.db import models
from grocery.models import foodIngredient

class pantryItems(models.Model):
    name = models.ForeignKey(foodIngredient, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    expiration = models.DateField(default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + str(self.quantity) +  ") (expires " + str(self.expiration) + ")"
