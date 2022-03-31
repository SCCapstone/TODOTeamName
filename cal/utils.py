from calendar import HTMLCalendar, month_name
from datetime import date, datetime, timedelta
from django.urls import reverse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

from .models import ScheduledRecipe


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
        self.setfirstweekday(6)

    def formatday(self, day, scheduled_recipes, active_user):
        food_by_day = scheduled_recipes.filter(
            scheduled_date__day=day).filter(user=active_user)
        d = ''
        for scheduled_recipe in food_by_day:
            d += f'<li><span class="recipe_url">{ scheduled_recipe.get_html_url }</span>{ scheduled_recipe.get_delete_url }</li>'
        if day != 0:
            url = reverse('cal:calDay') + \
                f'?day={ self.year }-{ self.month }-{ day }'
            return f'<td><a class="btn btn-light btn-sm date" href="{url}">{ day }</a><ul>{ d }</ul></td>'
        return '<td></td>'

    def formatweek(self, theweek, scheduled_recipes, active_user):
        week = ''
        for day, _ in theweek:
            week += self.formatday(day, scheduled_recipes, active_user)
        return f'<tr>{ week }</tr>'

    def formatmonth(self, active_user, withyear=True):
        scheduled_recipes = ScheduledRecipe.objects.filter(
            scheduled_date__year=self.year, scheduled_date__month=self.month)
        cal = f'<table class="calendar" border="0" cellpadding="0" cellspacing="0">\n'
        cal += f'{ self.formatmonthname(self.year, self.month, withyear=withyear) }\n'
        cal += f'{ self.formatweekheader() }\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{ self.formatweek(week, scheduled_recipes, active_user) }\n'
        cal += f'</table>'
        return cal

    def setUser(self, user):
        self.user = user


class WeekCalendar(HTMLCalendar):
    def __init__(self, year=None, week=None):
        self.year = year
        self.week = week
        super(WeekCalendar, self).__init__()
        self.setfirstweekday(6)

    def formatday(self, date, scheduled_recipes):
        food_by_day = list(
            filter(lambda x: (x.scheduled_date.day == date.day), scheduled_recipes))
        d = ''
        for scheduled_recipe in food_by_day:
            d += f'<li>{ scheduled_recipe.get_html_url } { scheduled_recipe.get_delete_url }</li>'
        url = reverse('cal:calDay') + \
            f'?day={ self.year }-{ date.month }-{ date.day }'
        return f'<td><a class="btn btn-light btn-sm date" href="{ url }">{ date.month }-{ date.day }</a><ul>{ d }</ul></td>'

    def formatweek(self, active_user):
        scheduled_recipes = list(filter(lambda x: (x.user == active_user) and (x.scheduled_date.year == self.year) and (
            x.scheduled_date.isocalendar()[1] == self.week), ScheduledRecipe.objects.all()))
        cal = f'<table class="calendar" border="0" cellpadding="0" cellspacing="0">\n'
        cal += f'<tr><th colspan="7">{ self.year } Week { self.week }</th></tr>'
        cal += f'{ self.formatweekheader() }\n'
        cal += f'<tr>'
        start_date = date.fromisocalendar(self.year, self.week-1, 7)
        end_date = start_date + timedelta(days=6.9)
        current_date = start_date
        while current_date <= end_date:
            cal += self.formatday(current_date, scheduled_recipes)
            current_date += timedelta(days=1)
        cal += f'</tr>'
        cal += f'</table>'
        return cal


class DayCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None, day=None):
        self.year = year
        self.month = month
        self.day = day
        super(DayCalendar, self).__init__()

    def formatday(self, active_user):
        # TODO add link to create a recipe
        scheduled_recipes = list(filter(lambda x: (x.user == active_user) and (x.scheduled_date.year == self.year) and (
            x.scheduled_date.month == self.month) and (x.scheduled_date.day == self.day), ScheduledRecipe.objects.all()))
        cal = f'<table class="calendar" border="0" cellpadding="0" cellspacing="0">\n'
        cal += f'<tr><th colspan="7">{ month_name[self.month] } { self.day }, { self.year }</th></tr>\n'
        cal += f'<tr><td colspan="7"><ul>'
        for scheduled_recipe in scheduled_recipes:
            cal += f'<li>{ scheduled_recipe.get_html_url } { scheduled_recipe.get_delete_url }</li>'
        cal += f'</ul></td></tr>'
        cal += f'</table>'
        return cal


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


def make_week_table(theweek, active_user):
    d = datetime.strptime(theweek + '-1', "%Y-%W-%w")
    year = d.year
    week = d.isocalendar()[1]
    scheduled_recipes = list(filter(lambda x: (x.user == active_user) and (x.scheduled_date.year == year) and (
        x.scheduled_date.isocalendar()[1] == week), ScheduledRecipe.objects.all()))
    start_date = date.fromisocalendar(year, week-1, 7)
    end_date = start_date + timedelta(days=6.9)
    current_date = start_date
    recipes = []
    while current_date <= end_date:
        string = ''
        food_by_day = list(
            filter(lambda x: (x.scheduled_date.day == current_date.day), scheduled_recipes))
        for scheduled_recipe in food_by_day:
            string += str(scheduled_recipe.recipe) + '\n'
        recipes.append(string)
        current_date += timedelta(days=1)
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return [weekdays, recipes]