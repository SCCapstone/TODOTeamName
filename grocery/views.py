from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dal import autocomplete

from .models import *
from .forms import *

# TODO - make option to remove  items

@login_required
def groceryListMain(request):
    if request.method == 'POST':
        form = GroceryItemsForm(request.POST)
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
    all_grocery_items = groceryItems.objects.filter(user=request.user)
    return render(request, 'grocery/groceryListMain.html', {'grocery_page': 'active', 'all_grocery_items': all_grocery_items, 'form': form})

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
