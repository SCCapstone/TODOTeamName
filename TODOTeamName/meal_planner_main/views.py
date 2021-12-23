from django.shortcuts import render

def homePage(request):
    return render(request, 'todo_team_name/homePage.html')