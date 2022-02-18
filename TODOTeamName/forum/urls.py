from django.urls import path

from . import views
from forum.views import frontpage, post_detail


app_name = 'forum'
urlpatterns = [
    path('', frontpage, name='healthForumMain'),
    path('<slug:slug>/', post_detail, name = 'post_detail'),
]
