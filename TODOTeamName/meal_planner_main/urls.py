from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.homePage, name = 'main-site'),
    #path('about/', views.about, name = 'site-about'),
]