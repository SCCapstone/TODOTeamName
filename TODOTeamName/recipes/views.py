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
        context = {'list': json.loads(requests.request("GET", url2, headers=headers, params=ressearch).text),'ingredients':ingredients}
        if request.POST.get('save')!=None:
            i = int(request.POST.get('save'))-1
            recipe = saverecipeapi(context['list'][i])
            return render(request, 'prove.html', recipe) #TODO tie to save user not prove.html 
        return render(request, "apisearch.html",  context)

    else:
        return render(request, "apisearch.html")

def rcreate(request):
    if request.method == "POST":
        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        recipe = {"title":title, "maketime":maketime, "ingredients":ingredients, "steps":steps, "creator":request.user.username} #TODO insert username
        #TODO save to user
        return render(request, 'prove.html', recipe) # TODO redirect back to my recipes
    else:
        return render(request, 'recipecreation.html')

def rview(request):
    return render (request, 'recipeview.html', user.recipes)

def redit(request):
    recipe = {"title":"make it", "maketime":"3 years", "ingredients":"test123", "steps":"test test test", "creator":"me"}
    if request.method == "POST":
        title = request.POST.get("title")
        maketime = request.POST.get("maketime")
        ingredients = request.POST.get("ingredients")
        steps = request.POST.get("steps")
        if recipe['creator']!=request.user.username:
           creator = recipe['creator']+"\n edited by "+request.user.username #TODO insert username
        else:
            creator = recipe['creator']
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

