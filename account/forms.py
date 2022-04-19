from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    allergy_list = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ['name', 'allergy_list']
