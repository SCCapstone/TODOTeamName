from calendar import HTMLCalendar, month_name
from .models import ScheduledRecipe
from django.urls import reverse
import datetime 


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
        self.setfirstweekday(6)

    def formatday(self, day, scheduled_recipes, active_user):
        food_by_day = scheduled_recipes.filter(scheduled_date__day=day).filter(user=active_user)
        d = ''
        for scheduled_recipe in food_by_day:
            d += f'<li>{ scheduled_recipe.get_html_url }</li>'
        if day != 0:
            url = reverse('cal:calDay') + f'?day={ self.year }-{ self.month }-{ day }'
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
        food_by_day = list(filter(lambda x:
        (x.scheduled_date.day == date.day), scheduled_recipes))
        d = ''
        for scheduled_recipe in food_by_day:
            d += f'<li>{ scheduled_recipe.get_html_url }</li>'
        url = reverse('cal:calDay') + f'?day={ self.year }-{ date.month }-{ date.day }'
        return f'<td><a class="btn btn-light btn-sm date" href="{ url }">{ date.month }-{ date.day }</a><ul>{ d }</ul></td>'
    
    def formatweek(self, active_user):
        scheduled_recipes = list(filter(lambda x: 
            (x.user == active_user) and 
            (x.scheduled_date.year == self.year) and 
            (x.scheduled_date.isocalendar()[1] == self.week), 
            ScheduledRecipe.objects.all()))
        cal = f'<table class="calendar" border="0" cellpadding="0" cellspacing="0">\n'
        cal += f'{ self.year } Week { self.week }\n'
        cal += f'{ self.formatweekheader() }\n'
        cal += f'<tr>'
        start_date = datetime.date.fromisocalendar(self.year, self.week, 1)
        end_date = start_date + datetime.timedelta(days=6.9)
        current_date = start_date 
        while current_date <= end_date:
            cal += self.formatday(current_date, scheduled_recipes)
            current_date += datetime.timedelta(days=1)
        cal += f'</tr>'
        return cal 


class DayCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None, day=None):
        self.year = year 
        self.month = month 
        self.day = day 
        super(DayCalendar, self).__init__()
    
    def formatday(self, active_user):
        scheduled_recipes = list(filter(lambda x: 
            (x.user == active_user) and 
            (x.scheduled_date.year == self.year) and 
            (x.scheduled_date.month == self.month) and
            (x.scheduled_date.day == self.day),
            ScheduledRecipe.objects.all()))
        cal = f'<table class="calendar" border="0" cellpadding="0" cellspacing="0">\n'
        cal += f'<tr><td><span class="date">{ month_name[self.month] } { self.day }, { self.year }</span>\n'
        cal += f'<ul>'
        for scheduled_recipe in scheduled_recipes:
            cal += f'<li>{ scheduled_recipe.get_html_url }</li>'
        cal += f'</ul></td></tr>'
        return cal 
