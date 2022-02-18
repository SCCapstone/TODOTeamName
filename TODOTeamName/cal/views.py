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

        # TODO: Allow for entering a date
    def return_date(requested_date):
        True


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


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
