from django.shortcuts import render, redirect

from .forms import *
from .models import *


def pantry(request):
    if request.method == 'POST':
        form = PantryAddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pantry:pantryMain')
    else:
        form = PantryAddItemForm()
    all_pantry_items = pantryItems.objects.all()
    return render(request, 'pantry/pantryMain.html', {'all_pantry_items': all_pantry_items, 'form': form})

# def addPantryItem(request):
#     name = request.POST.get('name',False)
#     expiration = request.POST.get('expiration',False)
#     new_item = pantryItems(name = name)
#     new_item.save()
#     return HttpResponseRedirect('/pantry/')
