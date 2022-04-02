from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *
from .forms import *


@login_required
def groceryListMain(request):
    if request.method == 'POST':
        form = GroceryAddItemForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('grocery:groceryMain')
    else:
        form = GroceryAddItemForm()
    all_grocery_items = groceryItems.objects.filter(user=request.user)
    return render(request, 'grocery/groceryListMain.html', {'all_grocery_items': all_grocery_items, 'form': form})

@login_required
def groceryListMain(request):
    all_grocery_items = groceryItems.objects.filter(user=request.user)
    if request.method == 'POST':
        if request.POST.get('edit')!=None:
            i = int(request.POST.get("edit"))
            return redirect("/grocery/editGroceryItem")
        if request.POST.get('delete')!=None:
            i=int(request.POST.get('delete'))
            all_grocery_items[i-1].delete()
    return render(request, 'grocery/groceryListMain.html', {'all_grocery_items': all_grocery_items})

# def remove(request,item_id):
#     item = GroceryList.objects.get(id = item_id)
#     item.delete()
#     messages.info(request, "item removed successfully")
#     return redirect('grocery:groceryMain')
