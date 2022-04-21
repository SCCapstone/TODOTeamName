from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'intro', 'body']


class ImagePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
    class Meta:
        model = ImagePost
        fields = ['title', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
