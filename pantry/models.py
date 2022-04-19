from django.conf import settings
from django.db import models
from grocery.models import foodIngredient
from django.core.validators import MaxValueValidator, MinValueValidator

class pantryItems(models.Model):
    name = models.ForeignKey(foodIngredient, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    expiration = models.DateField(default=None, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        if self.expiration == None:
            return self.name.name + " (" + str(self.quantity) +  ") (no expiration date)"
        return self.name.name + " (" + str(self.quantity) +  ") (expires " + str(self.expiration) + ")"
