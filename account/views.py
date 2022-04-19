from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from grocery.models import foodIngredient
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            permission = Permission.objects.get(name = 'Can add food ingredient')
            user = User.objects.get(username= username)
            user.user_permissions.add(permission)
            return redirect('account:login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'register_page': 'active', 'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('account:profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'account/profile.html', {'profile_page': 'active', 'p_form': p_form})
