from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
import requests
import json
from cal.models import ScheduledRecipe

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/informationBulk"


headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "4b462de572msh59ab5fee0c2b937p1a5096jsn62e9e0262449"
}

global recipe

@login_required
def recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    global recipe
    if request.method == 'POST':
        if request.POST.get('edit')!=None:
            #global recipe
            i = int(request.POST.get("edit"))
            recipe = {'recipe':recipes[i-1]}
            return redirect("/recipes/editRecipe")
        if request.POST.get('delete')!=None:
            i=int(request.POST.get('delete'))
            recipes[i-1].delete()
        if request.POST.get('sched')!=None:
           # global recipe
            i = int(request.POST.get("sched"))
            recipe = {'recipe':recipes[i-1]}
            return redirect("/recipes/scheduleRecipe")
    return render(request, 'recipesMain.html', {'recipe_page': 'active', 'recipes': recipes})

@login_required
def make(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('recipes:make')
        else:
            form = AddRecipeForm() 
    else: 
        form = AddRecipeForm()
        recipes = Recipe.objects.filter(user=request.user)
        return render(request, 'recipesAdd.html', {'recipe_page': 'active', 'recipes': recipes, 'form': form})

@login_required
def rsearch(request):
    if request.method == "POST": 
        ingredients = request.POST.get("search")
        querystring = {"query":ingredients,"offset":"0","number":"3"}
        response ={'list': json.loads(requests.request("GET", url, headers=headers, params=querystring).text)}
        id=""
        nutinfo=[]
        for i in response['list']['results']:
            id=id+str(i['id'])+","
            info ="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+str(i['id'])+"/nutritionWidget.json"
            res = json.loads(requests.request("GET", info, headers=headers).text)
            nutinfo.append(res)
        ressearch = {"ids":str(id)}
        temp = json.loads(requests.request("GET", url2, headers=headers, params=ressearch).text)
        align(temp, nutinfo)
        context = {'list': temp,'ingredients':ingredients}
        if request.POST.get('save')!=None:
            i = int(request.POST.get('save'))-1
            recipe = saverecipeapi(context['list'][i])
            srecipe=Recipe.objects.create(recipe_name=recipe['title'], recipe_ingredients=recipe['ingredients'], recipe_directions=recipe['steps'], estimated_time=int(recipe['maketime']), user=request.user)
            srecipe.save()
        context['recipe_page'] = 'active'
        return render(request, "apisearch.html",  context)

    else:
        return render(request, "apisearch.html", {'recipe_page': 'active'})

@login_required
def rcreate(request):
    if request.method == "POST":

        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        recipe = {"title":title, "maketime":maketime, "ingredients":ingredients, "steps":steps, "creator":request.user.username}
        srecipe=Recipe.objects.create(recipe_name=title, recipe_ingredients=ingredients, recipe_directions=steps, estimated_time=int(maketime), user=request.user)
        srecipe.save()
        return redirect("/recipes/recipeMain")
    else:
        return render(request, 'recipecreation.html', {'recipe_page': 'active'})

# doesnt work:
@login_required
def rview(request):
    return render (request, 'recipeview.html', user.recipes)

@login_required
def redit(request):
    global recipe
    if request.method == "POST":
        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
       # if recipe['creator']!=request.user.username:
        #   creator = recipe['creator']+"\n edited by "+request.user.username 
        #else:
         #   creator = recipe['creator']
        srecipe=Recipe.objects.create(recipe_name=title, recipe_ingredients=ingredients, recipe_directions=steps, estimated_time=int(maketime), user=request.user)
        srecipe.save()
        recipe['recipe'].delete()
        return redirect('/recipes/recipeMain')
    else:
        return render(request, 'redit.html', {'recipe_page': 'active', 'recipe':recipe['recipe']})

@login_required
def sched(request):
    global recipe
    temp=recipe['recipe']#{'recipe_name':recipe['recipe']['recipe_name'],'recipe_ingredients':recipe['recipe'].recipe_ingredients, 'recipe_directions':recipe['recipe'].recipe_directions, 'estimated_time':recipe['recipe'].estimated_time, 'date_added':recipe['recipe'].date_added, 'user':recipe['recipe'].user}
    #recipe['recipe'].delete()
    if(request.method=="POST"):
        schedrec=ScheduledRecipe.objects.create(scheduled_date=request.POST.get("date"), user=request.user, recipe=temp)
        schedrec.save()
        return render(request, 'sched.html', {'recipe_page': 'active','rec':temp})
    else:
        return render(request, 'sched.html', {'recipe_page': 'active','rec':temp})


def saverecipeapi(recipe):
    title = recipe['title']
    maketime = recipe['readyInMinutes']#str(recipe['readyInMinutes'])+" minutes"
    ingredients = ""
    for i in recipe['extendedIngredients']:
        ingredients = ingredients+" "+i['original']+"\n"
    steps = ""
    for s in recipe['analyzedInstructions'][0]['steps']:
        steps = steps+" "+str(s['number'])+": "+s['step']+"\n"
    creator = recipe['sourceUrl']
    ret = {"title":title, "maketime":maketime, "ingredients":ingredients, "steps":steps, "creator":creator}
    return ret

def align(temp, info):
    i=0
    for t in temp:
        t['nutrition'] = info[i]
        i=i+1