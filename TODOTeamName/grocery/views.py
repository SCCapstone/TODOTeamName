from django.contrib import messages 
from django.shortcuts import render, redirect

from .models import * 
from .forms import * 

# TODO - make option to remove  items
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

# def remove(request,item_id):
#     item = GroceryList.objects.get(id = item_id)
#     item.delete()
#     messages.info(request, "item removed successfully")
#     return redirect('grocery:groceryMain')