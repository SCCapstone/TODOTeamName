from django.conf import settings
from django.db import models


class Post(models.Model):
    """Makes a post tuple"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    image = models.ImageField('Image (Optional)', blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_added']


# TODO : Seperate page for Image Posts

class ImagePost(models.Model):
    """Makes an image post tuple"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    "Makes a comment tuple"
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField(max_length=1500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
