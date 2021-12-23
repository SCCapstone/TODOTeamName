from django.contrib import messages 
from django.shortcuts import render, redirect

from .models import * 
from .forms import * 

def groceryListMain(request):
    if request.method == 'POST':
        form = GroceryAddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grocery:groceryMain')
    else:
        form = GroceryAddItemForm()
    all_grocery_items = groceryItems.objects.all()
    return render(request, 'grocery/groceryListMain.html', {'all_grocery_items' : all_grocery_items, 'form': form})

# def groceryListMain(request):
#     item_list = GroceryList.objects.order_by("date")
#     if request.method == "POST":
#         form = GroceryListForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('grocerylist')
#     form = GroceryListForm()

#     page = {
#         "forms": form,
#         "list" : item_list,
#         "title": "Grocery List",
#     }
#     return render(request, 'todo_team_name/homePage.html')

# def remove(request,item_id):
#     item = GroceryList.objects.get(id = item_id)
#     item.delete()
#     messages.info(request, "item removed successfully")
#     return redirect('grocery:groceryMain')