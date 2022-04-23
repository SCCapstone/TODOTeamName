from django.contrib import admin
from .models import *

"""Creates admin objects for Django"""
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ImagePost)