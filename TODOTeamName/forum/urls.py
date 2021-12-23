from django.urls import path 

from . import views 

#TODO - fix forum posts and add these urls
app_name = 'forum'
urlpatterns = [
    path('', views.frontpage, name = 'forumMain'),
    # path('post/new/', views.post, name = 'post'),
    # path('post/<slug:slug>/view/', views.post, name = 'post'),
    # path('post/<slug:slug>/edit', views.post, name = 'post'),
    # path('post/<slug:slug>/comment', views.post, name = 'post'),
]