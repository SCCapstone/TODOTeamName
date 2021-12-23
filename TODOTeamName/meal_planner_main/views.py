from django.shortcuts import render

def homePage(request):
    return render(request, 'meal_planner_main/homePage.html')