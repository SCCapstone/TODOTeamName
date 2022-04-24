from django.urls import path
""" Handles URL navigation for the webpage"""

from . import views
from forum.views import *


app_name = 'forum'
urlpatterns = [
    path('', frontpage, name='healthForumMain'),
    path('user/<uName>', profilepage, name='userPage'),
    path('following/', followingpage, name='followingPage'),
    path('post/', valid_post, name = 'valid_post'),
    path('imgpost/', valid_image_post, name = 'valid_image_post'),
    path('<slug:slug>/', post_detail, name = 'post_detail'),
    path('delete_imgpost', views.delete_imgpost, name='delete_imgpost'),
    path('delete_post', views.delete_post, name='delete_post'),
]
