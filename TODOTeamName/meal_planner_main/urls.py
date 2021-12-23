from django.urls import path

from . import views

app_name = 'meal_planner_main'
urlpatterns = [
    path('', views.homePage, name = 'home'),
]