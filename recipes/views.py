from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
import requests
import json
from cal.models import ScheduledRecipe
from account.models import *
from .models import *

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/informationBulk"


headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "4b462de572msh59ab5fee0c2b937p1a5096jsn62e9e0262449"
}

global recipe

@login_required
def recipes(request):
    """main recipe view, shows all user recipes and take input for each button"""
    recipes = Recipe.objects.filter(user=request.user)
    global recipe
    if request.method == 'POST':
        if request.POST.get('edit')!=None:
            i = int(request.POST.get("edit"))
            recipe = {'recipe':recipes[i-1]}
            return redirect("/recipes/editRecipe")
        if request.POST.get('delete')!=None:
            i=int(request.POST.get('delete'))
            recipes[i-1].delete()
        if request.POST.get('sched')!=None:
            i = int(request.POST.get("sched"))
            recipe = {'recipe':recipes[i-1]}
            return redirect("/recipes/scheduleRecipe")
    return render(request, 'recipesMain.html', {'recipe_page': 'active', 'recipes': recipes})

@login_required
def rsearch(request):
    """recipe search page, takes user input and returns top 5 results based on the query. each recipe also has a save function"""
    if request.method == "POST": 
        ingredients = request.POST.get("search")
        profile=Profile.objects.get(user=request.user)  #gets user profile for allergies
        querystring = {"query":ingredients,"offset":"0","number":"5", "excludeIngredients":profile.allergy_list} #default parameters for the search
        response ={'list': json.loads(requests.request("GET", url, headers=headers, params=querystring).text)} #gets first set of results
        id=""
        nutinfo=[]
        for i in response['list']['results']: #condenses result ids to pull in-depth data
            id=id+str(i['id'])+","
            info ="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+str(i['id'])+"/nutritionWidget.json"
            res = json.loads(requests.request("GET", info, headers=headers).text)
            nutinfo.append(res)
        ressearch = {"ids":str(id)}
        temp = json.loads(requests.request("GET", url2, headers=headers, params=ressearch).text) #pulls in-depth data
        if 'code' in temp or len(temp)==0: #checks that results exist, no errors no empty lists
            messages.error(request, "Sorry, one of the search parameters couldn't be found, try a different search")
            return render(request, "apisearch.html", {'ingredients':ingredients})
        else:
            align(temp, nutinfo) #combines nutrition information and recipe into one object
            context = {'list': temp,'ingredients':ingredients}  
        if request.POST.get('save')!=None:  #gets the index of the appropriate recipe to save
            i = int(request.POST.get('save'))-1
            recipe = saverecipeapi(context['list'][i])
            srecipe=Recipe.objects.create(recipe_name=recipe['title'], recipe_ingredients=recipe['ingredients'], recipe_directions=recipe['steps'], recipe_notes=recipe['notes'], estimated_time=int(recipe['maketime']), user=request.user)
            srecipe.save() #saves recipe
            messages.success(request, recipe['title'] + " was saved to recipes!")
        context['recipe_page'] = 'active'
        return render(request, "apisearch.html",  context)

    else:
        return render(request, "apisearch.html", {'recipe_page': 'active'})

@login_required
def rcreate(request):
    """takes user input and saves it as a recipe object"""
    if request.method == "POST":

        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        etc=request.POST.get("etc")
        srecipe=Recipe.objects.create(recipe_name=title, recipe_ingredients=ingredients, recipe_directions=steps, recipe_notes=etc, estimated_time=int(maketime), user=request.user)
        srecipe.save()
        messages.success(request, "Recipe added!")
        return redirect("/recipes/recipeMain")
    else:
        return render(request, 'recipecreation.html', {'recipe_page': 'active'})

@login_required
def rview(request, recipe_id):
    """view for individual recipe, shows all information and takes button options"""
    context = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        global recipe
        if request.POST.get("sched")=="sched":
            recipe={'recipe':context}
            return redirect("/recipes/scheduleRecipe")
        if request.POST.get("edit")=="edit":
            recipe={'recipe':context}
            return redirect("/recipes/editRecipe")
        if request.POST.get("delete")=="delete":
            context.delete()
            return redirect("/recipes/recipeMain")
    return render(request, 'view.html', {'recipe':context})

@login_required
def redit(request):
    """opens edit recipe page, takes input like rcreate, but puts forward preexisting informaition as default values to edit"""
    global recipe
    if request.method == "POST":
        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        etc=request.POST.get("etc")
        srecipe=Recipe.objects.create(recipe_name=title, recipe_ingredients=ingredients, recipe_directions=steps, recipe_notes=etc, estimated_time=int(maketime), user=request.user)
        srecipe.save()
        recipe['recipe'].delete()
        return redirect('/recipes/recipeMain')
    else:
        return render(request, 'redit.html', {'recipe_page': 'active', 'recipe':recipe['recipe']})

@login_required
def sched(request):
    """view to schedule a recipe, takes a date format for the calendar"""
    global recipe
    temp=recipe['recipe']
    if(request.method=="POST"):
        schedrec=ScheduledRecipe.objects.create(scheduled_date=request.POST.get("date"), user=request.user, recipe=temp)
        schedrec.save()
        messages.success(request, "Success! Your recipe was scheduled for "+str(request.POST.get("date"))+"!")
        return render(request, 'sched.html', {'recipe_page': 'active','rec':temp})
    else:
        return render(request, 'sched.html', {'recipe_page': 'active','rec':temp})


def saverecipeapi(recipe):
    """helper function to reformat API data into usable form for Recipe object. for ease of translation"""

    title = recipe['title']
    maketime = recipe['readyInMinutes']
    ingredients = ""
    if len(recipe['extendedIngredients'])!=0:
        for i in recipe['extendedIngredients']:
            ingredients = ingredients+" "+i['original']+"\n"
    else:
        ingredients = "ingredients not found in recipe"
    steps = ""
    if len(recipe['analyzedInstructions'])!=0:
        for s in recipe['analyzedInstructions'][0]['steps']:
            steps = steps+" "+str(s['number'])+": "+s['step']+"\n"
    else:
        steps = "instructions not found in recipe \n"
    etc=""
    if len(recipe['nutrition'])!=0:
        for i in recipe['nutrition']['bad']:
            etc = etc+" "+i['title']+": "+str(i['amount'])+" "+str(i['percentOfDailyNeeds'])+"\n"
        for i in recipe['nutrition']['good']:
            etc = etc+" "+i['title']+": "+str(i['amount'])+" "+str(i['percentOfDailyNeeds'])+"\n"
    else:
        etc = "nutritional information not found in recipe"
    creator = recipe['sourceUrl']
    ret = {"title":title, "maketime":maketime, "ingredients":ingredients, "steps":steps, "notes":etc, "creator":creator}
    return ret

def align(temp, info):
    """helper function to align nutritional information with the appropriate recipe"""
    i=0
    for t in temp:
        t['nutrition'] = info[i]
        i=i+1
