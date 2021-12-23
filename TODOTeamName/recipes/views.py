from django.shortcuts import render
import requests 
import json 

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "4b462de572msh59ab5fee0c2b937p1a5096jsn62e9e0262449"
}

def recipes(request):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
    querystring = {"number":"3"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return render(request, 'recipes/recipesMain.html', {'list' : json.loads(response.text)})