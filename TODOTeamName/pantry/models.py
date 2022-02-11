from django.db import models


class pantryItems(models.Model):
    name = models.TextField(max_length=50)
    expiration = models.DateField(default="")
    userid = models.TextField(max_length=150)

    def __str__(self):
        return self.name + " (expires " + str(self.expiration) + ")"
