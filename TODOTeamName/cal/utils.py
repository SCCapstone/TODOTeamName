from calendar import HTMLCalendar
from .models import ScheduledRecipe


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, scheduled_recipes):
        food_by_day = scheduled_recipes.filter(scheduled_date__day=day)
        d = ''
        for scheduled_recipe in food_by_day:
            d += scheduled_recipe.get_html_url
        if day != 0:
            return f"<td>{day}<ul>{d}</ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, scheduled_recipes):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, scheduled_recipes)
        return f'<tr>{week}</tr>'

    def formatmonth(self, withyear=True):
        scheduled_recipes = ScheduledRecipe.objects.filter(
            scheduled_date__year=self.year, scheduled_date__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, scheduled_recipes)}\n'
        return cal
