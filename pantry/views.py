from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

@login_required
def pantry(request):
    if request.method == 'POST':
        form = PantryAddItemForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('pantry:pantryMain')
    else:
        form = PantryAddItemForm()
    all_pantry_items = pantryItems.objects.filter(user = request.user)
    return render(request, 'pantry/pantryMain.html', {'pantry_page': 'active', 'all_pantry_items': all_pantry_items, 'form': form})

@login_required
def pantry(request):
    all_pantry_items = pantryItems.objects.filter(user=request.user)
    if request.method == 'POST':
        if request.POST.get('edit')!=None:
            i = int(request.POST.get("edit"))
            return redirect("/pantry/editPantryItem")
        if request.POST.get('delete')!=None:
            i=int(request.POST.get('delete'))
            all_pantry_items[i-1].delete()
    return render(request, 'pantry/pantryMain.html',{'all_pantry_items': all_pantry_items})    
        
        
        

# def addPantryItem(request):
#     name = request.POST.get('name',False)
#     expiration = request.POST.get('expiration',False)
#     new_item = pantryItems(name = name)
#     new_item.save()
#     return HttpResponseRedirect('/pantry/')
