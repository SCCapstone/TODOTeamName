from datetime import date, datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.views import generic
from django.urls import reverse
import calendar

from .forms import *
from .models import *
from .utils import *


class CalendarView(generic.ListView):
    model = ScheduledRecipe
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        #cal.setUser(self.request.user)
        html_cal = cal.formatmonth(self.request.user, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


class WeekView(generic.ListView):
    model = ScheduledRecipe 
    template_name = 'cal/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date_week(self.request.GET.get('week', None))
        cal = WeekCalendar(d.year, d.isocalendar()[1])
        html_cal = cal.formatweek(self.request.user)
        context['calendar'] = mark_safe(html_cal)
        context['prev_week'] = prev_week(d)
        context['next_week'] = next_week(d)
        return context


class DayView(generic.ListView):
    model = ScheduledRecipe 
    template_name = 'cal/day.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date_day(self.request.GET.get('day', None))
        cal = DayCalendar(d.year, d.month, d.day)
        html_cal = cal.formatday(self.request.user)
        context['calendar'] = mark_safe(html_cal)
        context['prev_day'] = prev_day(d)
        context['next_day'] = next_day(d)
        return context 


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return date.today()

def get_date_week(req_week):
    if req_week:
        year, week = (int(x) for x in req_week.split('-'))
        d = date.fromisocalendar(year, week, day=1)
        return d 
    return date.today()

def get_date_day(req_day):
    if req_day:
        year, month, day = (int(x) for x in req_day.split('-'))
        return date(year, month, day)
    return date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def prev_week(d):
    prev_week = d - timedelta(days=7)
    return 'week=' + str(prev_week.year) + '-' + str(prev_week.isocalendar()[1])

def next_week(d):
    next_week = d + timedelta(days=7)
    return 'week=' + str(next_week.year) + '-' + str(next_week.isocalendar()[1])

def prev_day(d):
    prev_day = d - timedelta(days=1)
    return 'day=' + str(prev_day.year) + '-' + str(prev_day.month) + '-' + str(prev_day.day)

def next_day(d):
    next_day = d + timedelta(days=1)
    return 'day=' + str(next_day.year) + '-' + str(next_day.month) + '-' + str(next_day.day)

def scheduled_recipe(request, scheduled_recipe_id=None):
    instance = ScheduledRecipe()
    if scheduled_recipe_id:
        instance = get_object_or_404(ScheduledRecipe, pk=scheduled_recipe_id)
    else:
        instance = ScheduledRecipe()

    form = ScheduledRecipeForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('cal:calMain'))

    return render(request, 'cal/scheduled_recipe.html', {'form': form})
