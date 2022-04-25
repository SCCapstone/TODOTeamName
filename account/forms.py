from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    """form for user to create an account"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    """form for user to add information to their profile"""
    name = forms.CharField(max_length=50)
    allergy_list = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ['name', 'allergy_list']
