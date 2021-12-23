from django.db import models

class pantryItems(models.Model):
    name = models.TextField(max_length=50)
    expiration = models.DateField(default="")
    def __str__(self):
        return self.name + " (expires " + str(self.expiration) + ")"