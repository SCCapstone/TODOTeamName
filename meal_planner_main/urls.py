from django.urls import path, include

from . import views


app_name = 'meal_planner_main'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('forum/', include('forum.urls'), name = 'forum'),
]
