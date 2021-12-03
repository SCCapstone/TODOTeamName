"""todo_team_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from meal_planner_main import views
from meal_planner_main.views import frontpage



app_name = 'meal_planner_main'
urlpatterns = [
    path('', views.default, name = 'default'),
    path('home/', views.homePage, name = 'home'),
    path('createAccount/', views.createAccount, name = 'createAccount'),
    path('login/', views.login, name = 'login'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('forum/', views.frontpage, name = 'forum'),
    path('post/', views.forumPost, name = 'fpost'),
    #path('<slug:slug>/',post_detail, name ='post_detail'),
    path('groceries/', views.groceryListView, name = 'groceries'),
    path('pantry/', views.pantry, name = 'pantry'),
    path('recipes/', views.recipes, name = 'recipes'),
    path('admin/', admin.site.urls),
    path('addGroceryItem/', views.groceryListView, name = 'gadd'),
    path('deleteGroceryItem/', views.remove, name="deleteGI"),
    #url(r'^homePage/$', views.homePage, name='index'),
    #url(r'^calendar/$', views.CalendarView.as_view(), name='calendar')
]

