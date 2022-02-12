from django.shortcuts import render
import requests
import json

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/informationBulk"

recipe = {}

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "4b462de572msh59ab5fee0c2b937p1a5096jsn62e9e0262449"
}

def recipes(request):
#    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
    querystring = {"number": "3"}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    print(response.text)
    return render(request, 'recipesMain.html', {'list': json.loads(response.text)})

def rsearch(request):
    if request.method == "POST":
        ingredients = request.POST.get("search")
        querystring = {"query":ingredients,"offset":"0","number":"1"}
        response ={'list': json.loads(requests.request("GET", url, headers=headers, params=querystring).text)}
        id=""
        for i in response['list']['results']:
            id=id+str(i['id'])+","
        ressearch = {"ids":str(id)}
        context = {'list': json.loads(requests.request("GET", url2, headers=headers, params=ressearch).text)}
        return render(request, "apisearch.html", context)        #TODO figure out the save function

    else:
        return render(request, "apisearch.html")

def rcreate(request):
    if request.method == "POST":
        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        recipe = {"title":title, "maketime":maketime, "ingredients":ingredients, "steps":steps, "creator":"me"} #TODO insert username
        return render(request, 'prove.html', recipe) # TODO redirect back to my recipes
    else:
        return render(request, 'recipecreation.html')

def rview(request):
    return render (request, 'recipeview.html' ,user.recipes)

def redit(request):
    if request.method == "POST":
        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        if recipe['creator']!="me":
           creator = creator+"\n edited by "+"me" #TODO insert username
        recipe = {"title":title, "maketime":maketime, "ingredients":ingredients, "steps":steps, "creator":creator}
        return render(request, 'prove.html', recipe)
    else:
        return render(request, 'redit.html', recipe)

def saverecipeapi(recipe):
    title = recipe['title']
    maketime = str(recipe['readyInMinutes'])+" minutes"
    ingredients = ""
    for i in recipe['extendedIngredients']:
        ingredients = ingredients+" "+i['original']
    steps = ""
    for s in recipe['analyzedInstructions'][0]['steps']:
        steps = steps+" "+str(s['number'])+": "+s['step']
    creator = recipe['sourceUrl']
    ret = {"title":title, "maketime":maketime, "ingredients":ingredients, "steps":steps, "creator":creator}
    return ret

