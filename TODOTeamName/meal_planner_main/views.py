from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse(request, 'homePage.html')

def groceryListView(request):
	return render(request, 'groceryListMain.html')
