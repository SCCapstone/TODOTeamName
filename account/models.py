from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    name = models.CharField(max_length=50, default="")
    allergy_list = models.CharField(max_length=100, default="")
    # TODO - add grocery list
    # TODO - add pantry list
    # TODO - add friends list
    # TODO - add forum posts list
    # TODO - add recipe list

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
