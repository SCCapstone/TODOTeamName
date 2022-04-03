from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
def pantryeditdelete(request):
    all_pantry_items = pantryItems.objects.filter(user=request.user)
    if request.method == 'POST':
        if request.POST.get('edit')!=None:
            i = int(request.POST.get("edit"))
            pantryitem = all_pantry_items[i-1]
            return redirect('pantry:edit', id=pantryitem.name.id)
        if request.POST.get('delete')!=None:
            i=int(request.POST.get('delete'))
            all_pantry_items[i-1].delete()
    return redirect('pantry:pantryMain')
    #return render(request, 'pantry/pantryMain.html',{'all_pantry_items': all_pantry_items})    
        
@login_required                 
def edit(request, id=None, template_name='pantry/edit.html'):
    if id:
        pantryitem = get_object_or_404(pantryItems, name = foodIngredient.objects.get(id = id), user = request.user)
        if pantryitem.user != request.user:
            return HttpResponseForbidden()      
    else:
        pantryitem = pantryItems(user=request.user)
    
    form = PantryAddItemForm(request.POST or None, instance=pantryitem)                          
    if request.POST and form.is_valid():

        if form.instance.name == foodIngredient.objects.get(id=id):
            form.save()
        elif not pantryItems.objects.filter(user = request.user, name = form.instance.name):
                form.instance.user = request.user
                form.save()
        else:
                item = pantryItems.objects.get(user = request.user, name = form.instance.name)
                item.quantity = item.quantity + form.instance.quantity
                item.save()
                pantryItems.objects.filter(user=request.user, name = foodIngredient.objects.get(id=id)).delete()

        # Save was successful, so redirect to another page
        redirect_url = reverse('pantry:pantryMain')               
        return redirect(redirect_url)

    return render(request, template_name, {  
        'form': form                                 
    })   
        

# def addPantryItem(request):
#     name = request.POST.get('name',False)
#     expiration = request.POST.get('expiration',False)
#     new_item = pantryItems(name = name)
#     new_item.save()
#     return HttpResponseRedirect('/pantry/')
