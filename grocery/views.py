from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dal import autocomplete

from .models import *
from .forms import *
from pantry.models import pantryItems


@login_required
def groceryListMain(request):
    all_grocery_items = groceryItems.objects.filter(user=request.user)
    if request.method == 'POST':
        form = GroceryItemsForm(request.POST)
        #if request.POST.get('edit')!=None:
        #    i = int(request.POST.get("edit"))
        #    return redirect("/grocery/editGroceryItem")
        #elif request.POST.get('delete')!=None:
        #    i=int(request.POST.get('delete'))
        #    all_grocery_items[i-1].delete()
        if form.is_valid():
            if not groceryItems.objects.filter(user = request.user, item_name = form.instance.item_name):
                form.instance.user = request.user
                form.save()
            else:
                item = groceryItems.objects.get(user = request.user, item_name = form.instance.item_name)
                item.quantity = item.quantity + form.instance.quantity
                item.save()
            return redirect('grocery:groceryMain')
    else:
        form = GroceryItemsForm()
    return render(request, 'grocery/groceryListMain.html', {'grocery_page': 'active', 'all_grocery_items': all_grocery_items, 'form': form})

def editdelete(request):
    all_grocery_items = groceryItems.objects.filter(user=request.user)
    if request.method == 'POST':
        if request.POST.get('edit')!=None:
            i = int(request.POST.get("edit"))
            return redirect("/grocery/editGroceryItem")
        elif request.POST.get('delete')!=None:
            i=int(request.POST.get('delete'))
            all_grocery_items[i-1].delete()
        elif request.POST.get('sendtopantry')!=None:
            i = int(request.POST.get('sendtopantry'))
            g = all_grocery_items[i-1]
            if not pantryItems.objects.filter(user = request.user, name = g.item_name):
                p = pantryItems.objects.create(name = g.item_name, quantity = g.quantity, user = g.user)
            else:
                item = pantryItems.objects.get(user = request.user, name = g.item_name)
                item.quantity = item.quantity + g.quantity
                item.save()
            
    return redirect('grocery:groceryMain')


#@login_required
#def groceryListMain(request):
#    all_grocery_items = groceryItems.objects.filter(user=request.user)
#
#    if request.method == 'POST':
#        if request.POST.get('edit')!=None:
#            i = int(request.POST.get("edit"))
#            return redirect("/grocery/editGroceryItem")
#        elif request.POST.get('delete')!=None:
#            i=int(request.POST.get('delete'))
#            all_grocery_items[i-1].delete()
#        else: 
#            form = GroceryAddItemForm(request.POST)
#            if form.is_valid():
#                form.instance.user = request.user
#                form.save()
#                return redirect('grocery:groceryMain')
#
#    else:
#        form = GroceryAddItemForm()
#    return render(request, 'grocery/groceryListMain.html', {'all_grocery_items': all_grocery_items, 'form': form})

class IngredientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor ! 
        if not self.request.user.is_authenticated:
            return foodIngredient.objects.none()

        qs = foodIngredient.objects.all()
    
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

# def remove(request,item_id):
#     item = GroceryList.objects.get(id = item_id)
#     item.delete()
#     messages.info(request, "item removed successfully")
#     return redirect('grocery:groceryMain')
