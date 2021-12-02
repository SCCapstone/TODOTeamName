from django.shortcuts import render
from datetime import *
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar
from django.http import HttpResponse

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "4b462de572msh59ab5fee0c2b937p1a5096jsn62e9e0262449"
    }

# Create your views here.
def home(request):
	return render(request, 'todo_team_name/homePage.html')

def createAccount(request):
	return render(request, 'todo_team_name/accountCreation.html')

def login(request):
	return render(request, 'todo_team_name/accountLogin.html')

def calendar(request):
	return render(request, 'todo_team_name/calendar.html')

def groceryListView(request):
	return render(request, 'todo_team_name/groceryListMain.html')

def healthForum(request):
	return render(request, 'todo_team_name/healthForumMain.html')

def forumPost(request):
	return render(request, 'todo_team_name/healthForumPost_detail.html')

def pantry(request):
	return render(request, 'todo_team_name/pantryMain.html')

def recipes(request):
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
	querystring = {"number":"3"}
	response = requests.request("GET", url, headers=headers, params=querystring)
	return render(request, 'todo_team_name/recipesMain.html', {'list' : json.loads(response.text)})

class CalendarView(generic.ListView):
	model = ScheduledRecipe
	template_name = 'todo_team_name/calendar.html'

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