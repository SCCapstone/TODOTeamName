from django.urls import path

from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calMain'),
    path('weekview', views.WeekView.as_view(), name='calWeek'),
    path('scheduled_recipe/new/', views.scheduled_recipe,
         name='scheduled_recipe_new'),
    path('scheduled_recipe/edit/<int:scheduled_recipe_id>/',
         views.scheduled_recipe, name='scheduled_recipe_edit'),
    path('scheduled_recipe/view/<int:scheduled_recipe_id>/',
         views.scheduled_recipe, name='scheduled_recipe_view'),
]
