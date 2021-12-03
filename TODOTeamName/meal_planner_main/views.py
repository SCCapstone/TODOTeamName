from django.shortcuts import render, redirect
from datetime import *
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
from .forms import *
from .utils import Calendar
from django.http import HttpResponse
#from . import models
import requests
import json

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "4b462de572msh59ab5fee0c2b937p1a5096jsn62e9e0262449"
    }

# Create your views here.
def default(request):
        return redirect('createAccount')

def homePage(request):
        return render(request, 'todo_team_name/homePage.html')

def createAccount(request):
        if request.method == "POST":
                x_name = request.POST.get("name")
                uname = request.POST.get("uname")
                email = request.POST.get("email")
                password = request.POST.get("password")
                x_user = User.objects.create_user(uname, email, password)
                suser = siteUser.objects.create(user = x_user, name = x_name)
                return redirect('login')
        else:
                return render(request, 'todo_team_name/accountCreation.html')


def login(request):
        if request.method == "POST":
                uname = request.POST.get("uname")
                password = request.POST.get("password")
                #isValid = siteUser.objects.filter(user.username == uname, user.password == password).exists()
                isValid = authenticate(username=uname, password=password)
                if isValid is not None: #test if the account exists
                        return redirect('home')
                else: #there is no account
                        return render(request, 'todo_team_name/accountLogin.html')
        else:
                return render(request, 'todo_team_name/accountLogin.html')

def calendar(request):
        return render(request, 'todo_team_name/calendar.html')

# TODO: This should be obsolete. Review and delete
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
        print(response.text)
        return render(request, 'todo_team_name/recipesMain.html', {'list' : json.loads(response.text)})

def frontpage(request):
        posts = Post.objects.all()
        return render(request, 'meal_planner_main/homePage.html',{'posts': posts})

#def post_detail(request, slug):
#       post = Post.objects.get(slug = slug)
#       if request.method == 'POST':
#               form = CommentForm(request.POST)
#               if form.is_valid():
#                       comment = form.save(commit =False)
#                       comment.post = post
#                       comment.save()

#                       return redirect('post_detail',slug = post.slug)
#       else:
#               form = CommentForm()
#       return render(request, 'meal_planner_main/homePage_detail.html') #, {'post': post, 'form': form})

# TODO: Create generic List class (with remove/edit/add new) for both pantry and grocery to use
def groceryListMain(request):
        item_list = GroceryList.objects.order_by("date")
        if request.method == "POST":
                form = GroceryListForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('grocerylist')
        form = GroceryListForm()

        page = {
                        "forms": form,
                        "list" : item_list,
                        "title": "Grocery List",
        }
        return render(request, 'todo_team_name/homePage.html')

def remove(request,item_id):
        item = GroceryList.objects.get(id = item_id)
        item.delete()
        messages.info(request, "item removed successfully")
        return redirect('groceryListView')


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
