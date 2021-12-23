from datetime import date 
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import generic 

from .models import * 
from .utils import *

class CalendarView(generic.ListView):
    model = ScheduledRecipe
    template_name = 'cal/calendar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        d = date.today()

        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

        # TODO: Allow for entering a date
    def return_date(requested_date):
        True
