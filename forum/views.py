import random
import math
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from itertools import chain
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from account.models import Profile
from .models import *
from .forms import *


def frontpage(request):
    posts = Post.objects.all()
    #imgpost = ImagePost.objects.all()
    #posts = sorted( chain(post, imgpost), key=lambda instance: instance.date_added)
    return render(request, 'forum/healthForumFrontPage.html', {'forum_page': 'active', 'posts': posts})

#def profilepage(request, slug):
#    posts = Post.objects.filter(user = User.objects.get(pk=slug))
#    return render(request, 'forum/healthForumMain.html', {'posts': posts})


def profilepage(request, uName):
    following = False
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        the_user = User.objects.get(username=uName)
        following = the_user in profile.following.all()
        if request.method == 'POST':
            if following:
                profile.following.remove(the_user)
            else: 
                profile.following.add(the_user)
    
    posts = Post.objects.filter(user = User.objects.get(username=uName))
    return render(request, 'forum/UserFeed.html', {'forum_page': 'active', 'posts': posts, 'uName': uName, 'following': following})

@login_required
def followingpage(request):
    userProfile = Profile.objects.get(user = request.user)
    following = userProfile.following.all()
    posts = Post.objects.filter(user__in=following)
    return render(request, 'forum/healthForumFollowingPage.html', {'forum_page': 'active', 'posts': posts})

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
    return render(request, 'forum/healthForumPost.html', {'forum_page': 'active', 'form': form})


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
    return render(request, 'forum/healthForumImgPost.html', {'forum_page': 'active', 'form': form})


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

    return render(request, 'forum/healthForumPost_detail.html', {'forum_page': 'active', 'post': post, 'form': form})
