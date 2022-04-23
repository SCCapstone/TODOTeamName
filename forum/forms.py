from django import forms

from .models import *


class PostForm(forms.ModelForm):
    """Creates Post form"""
    class Meta:
        model = Post
        fields = ['title', 'image', 'intro', 'body']


class ImagePostForm(forms.ModelForm):
    """Creates Image Post form"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
    class Meta:
        model = ImagePost
        fields = ['title', 'image']


class CommentForm(forms.ModelForm):
    """Creates comment form in post detail view"""
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
