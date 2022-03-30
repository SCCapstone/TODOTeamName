from datetime import date, datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.safestring import mark_safe
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from io import BytesIO
from recipes.models import Recipe
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
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
        context['the_day'] = the_day(d)
        context['the_week'] = the_week(d)
        context['cal_page'] = 'active'
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
        context['the_day'] = the_day(d)
        context['the_month'] = the_month(d)
        context['the_week'] = the_week(d)
        context['cal_page'] = 'active'
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
        context['the_week'] = the_week(d)
        context['the_month'] = the_month(d)
        context['cal_page'] = 'active'
        return context 

class DeleteView(generic.DeleteView):
    model = ScheduledRecipe
    template_name = 'cal/delete_view.html'
    success_url = '/cal/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cal_page'] = 'active'
        return context 

class PdfPrint():
    def __init__(self, active_user, buffer):
        self.buffer = buffer
        self.pageSize = A4
        self.width, self.height = self.pageSize
        self.active_user = active_user

    def report(self, theweek):
        doc = SimpleDocTemplate(
            self.buffer,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72,
            pagesize=self.pageSize
        )
        styles = getSampleStyleSheet()
        t = Table(make_week_table(theweek, self.active_user))
        t.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
            ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ]))
        elements = []
        elements.append(Paragraph('Meal Plan ' + theweek, styles['Title']))
        elements.append(t)
        doc.build(elements)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf

def cal_pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    d = date.today().strftime('%Y-%m-%d')
    filename = 'Meal_Plan_' + d.__str__()  # TODO fix
    response['Content-Disposition'] = f'inline; filename="{filename}.pdf"'
    buffer = BytesIO()
    report = PdfPrint(request.user, buffer)
    path = request.get_full_path()
    week = path.split('week=', 1)[1]
    pdf = report.report(week)
    response.write(pdf)
    return response

def make_week_table(theweek, active_user):
    d = datetime.datetime.strptime(theweek + '-1', "%Y-%W-%w")
    year = d.year
    week = d.isocalendar()[1]
    scheduled_recipes = list(filter(lambda x: (x.user == active_user) and (x.scheduled_date.year == year) and (
        x.scheduled_date.isocalendar()[1] == week), ScheduledRecipe.objects.all()))
    start_date = datetime.date.fromisocalendar(year, week-1, 7)
    end_date = start_date + datetime.timedelta(days=6.9)
    current_date = start_date
    recipes = []
    while current_date <= end_date:
        string = ''
        food_by_day = list(
            filter(lambda x: (x.scheduled_date.day == current_date.day), scheduled_recipes))
        for scheduled_recipe in food_by_day:
            string += str(scheduled_recipe.recipe) + '\n'
        recipes.append(string)
        current_date += datetime.timedelta(days=1)
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return [weekdays, recipes]

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

def the_month(d):
    return 'month=' + str(d.year) + '-' + str(d.month)

def the_week(d):
    return 'week=' + str(d.year) + '-' + str(d.isocalendar()[1])

def the_day(d):
    return 'day=' + str(d.year) + '-' + str(d.month) + '-' + str(d.day)

@login_required
def scheduled_recipe(request, scheduled_recipe_id=None):
    instance = ScheduledRecipe()
    if scheduled_recipe_id:
        instance = get_object_or_404(ScheduledRecipe, pk=scheduled_recipe_id)
    else:
        instance = ScheduledRecipe()

    form = ScheduledRecipeForm(request.POST or None, instance=instance)
    form.fields['recipe'].queryset = Recipe.objects.all().filter(user=request.user)
    if request.POST and form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('cal:calMain'))

    return render(request, 'cal/scheduled_recipe.html', {'cal_page': 'active', 'form': form})
