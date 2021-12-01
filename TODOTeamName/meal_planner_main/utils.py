from datetime import datetime,timedelta
from calendar import HTMLCalendar
from .models import ScheduledRecipe

class Calendar(HTMLCalendar):
    def __init__(self, year = None, month = None):
            self.year = year
            self.month = month
            super(Calendar,self).__init__()

    def formatday(self, day, events):
        food_by_day = events.filter(schedued_date = day)
        d = ''
        for event in food_by_day:
            d = f'<li> {event.title}</li>'
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'
    def formatweek(self, theweek, events):
        w = ''
        for d, weekday in theweek:
            w += self.formatday(d,events)
        return f'<tr> {w} </tr>'
    def formatmonth(self, theyear, themonth, withyear=True):
        events = ScheduledRecipe.objects.filter(start_date__year=self.year, start_date__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
