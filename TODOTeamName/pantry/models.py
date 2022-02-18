from django.conf import settings
from django.db import models


class pantryItems(models.Model):
    name = models.TextField(max_length=50)
    expiration = models.DateField(default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (expires " + str(self.expiration) + ")"
