import random
import math
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from itertools import chain

from .models import *
from .forms import *


def frontpage(request):
    posts = Post.objects.all()
    #imgpost = ImagePost.objects.all()
    #posts = sorted( chain(post, imgpost), key=lambda instance: instance.date_added)
    return render(request, 'forum/healthForumMain.html', {'posts': posts})


def valid_post(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            post = form.save(commit=False)
            form.instance.slug = get_random_string(8,'0123456789') #creates random slug
            post.post = post
            post.save()

            return redirect('forum:healthForumMain')
    else:
        form = PostForm()
    return render(request, 'forum/healthForumPost.html', {'form': form})


def valid_image_post(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            post = form.save(commit=False)
            form.instance.slug = get_random_string(8,'0123456789') #creates random slug
            post.post = post
            post.save()
            return redirect('forum:healthForumMain')
    else:
        form = ImagePostForm()
    return render(request, 'forum/healthForumImgPost.html', {'form': form})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('forum:post_detail', slug = post.slug)
    else:
        form = CommentForm()

    return render(request, 'forum/healthForumPost_detail.html', {'post': post, 'form': form})
