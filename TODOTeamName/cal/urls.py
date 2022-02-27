from django.urls import path

from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calMain'),
    path('weekview', views.WeekView.as_view(), name='calWeek'),
    path('dayview', views.DayView.as_view(), name='calDay'),
    path('scheduled_recipe/new/', views.scheduled_recipe,
        name='scheduled_recipe_new'),
    path('scheduled_recipe/edit/<int:scheduled_recipe_id>/',
        views.scheduled_recipe, name='scheduled_recipe_edit'),
    path('scheduled_recipe/delete/<int:pk>/',
        views.DeleteView.as_view(), name='scheduled_recipe_delete')
]
