from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'cal'
urlpatterns = [
    path('', login_required(views.CalendarView.as_view()), name='calMain'),
    path('pdf', views.cal_pdf_view, name='calPdf'),
    path('weekview', login_required(views.WeekView.as_view()), name='calWeek'),
    path('dayview', login_required(views.DayView.as_view()), name='calDay'),
    path('scheduled_recipe/new/', views.scheduled_recipe,
         name='scheduled_recipe_new'),
    path('scheduled_recipe/edit/<int:scheduled_recipe_id>/',
         views.scheduled_recipe, name='scheduled_recipe_edit'),
    path('scheduled_recipe/delete/<int:pk>/',
         views.DeleteView.as_view(), name='scheduled_recipe_delete')
]
