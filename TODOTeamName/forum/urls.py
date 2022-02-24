from django.urls import path

from . import views
from forum.views import *


app_name = 'forum'
urlpatterns = [
    path('', frontpage, name='healthForumMain'),
    path('post/', valid_post, name = 'valid_post'),
    path('<slug:slug>/', post_detail, name = 'post_detail'),
]
