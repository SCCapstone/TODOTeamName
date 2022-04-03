from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from dal import autocomplete


from .models import *
from .forms import *
from pantry.models import pantryItems


@login_required
def groceryListMain(request):
    all_grocery_items = groceryItems.objects.filter(user=request.user)
    global groceryitem
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
    global groceryitem
    if request.method == 'POST':
        if request.POST.get('edit')!=None:
            i = int(request.POST.get("edit"))
            groceryitem = all_grocery_items[i-1]
            return redirect('grocery:edit', id = groceryitem.item_name.id)
            #return redirect("/grocery/editGroceryItem")
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

@login_required
def edit(request, id=None, template_name='grocery/edit.html'):
    if id:
        groceryitem = get_object_or_404(groceryItems, item_name = foodIngredient.objects.get(id = id), user = request.user)
        if groceryitem.user != request.user:
            return HttpResponseForbidden()
    else:
        groceryitem = groceryItem(user=request.user)
    
    form = GroceryItemsForm(request.POST or None, instance=groceryitem)
    if request.POST and form.is_valid():
        if form.instance.item_name == foodIngredient.objects.get(id=id):
            form.save()
        elif not groceryItems.objects.filter(user = request.user, item_name = form.instance.item_name):
                form.instance.user = request.user
                form.save()
        else:
                item = groceryItems.objects.get(user = request.user, item_name = form.instance.item_name)
                item.quantity = item.quantity + form.instance.quantity
                item.save()
                groceryItems.objects.filter(user=request.user, item_name = foodIngredient.objects.get(id=id)).delete()


        # Save was successful, so redirect to another page
        redirect_url = reverse('grocery:groceryMain')
        return redirect(redirect_url)

    return render(request, template_name, {
        'form': form
    })

#def editGroceryItem(request):
#    global groceryitem
#    item = groceryitem
#    if request.method == "POST":
#        quantity = request.POST.get("quantity")
#        item.quantity = quantity
#        item.save()
#        return redirect('grocery:groceryMain')
#    else:
#        return render(request, 'grocery/gedit.html', {'grocery_page': 'active', 'groceryitem':item})

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
