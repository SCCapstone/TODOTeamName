import random
import math
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from itertools import chain
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from account.models import Profile
from .models import *
from .forms import *


def frontpage(request):
    """ Populates the front page with all posts """

    posts = Post.objects.all()
    imgposts = ImagePost.objects.all()

    return render(request, 'forum/healthForumFrontPage.html',
                  {'forum_page': 'active', 'posts': posts, 'imgposts': imgposts})


def profilepage(request, uName):
    """ Populates the users profile page

    Allows users to follow and unfollow friends

    Parameters
    ----------
    uName : str
        The username
    """

    following = False
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        the_user = User.objects.get(username=uName)
        following = the_user in profile.following.all()
        if request.method == 'POST':
            if following:
                messages.success(request, "Unfollowed " + str(the_user))
                profile.following.remove(the_user)
            else:
                messages.success(request, "Followed " + str(the_user))
                profile.following.add(the_user)
            # flip boolean so that if you follow someone, the page will then show "unfollow";
            # whereas if you unfollow someone, the page should show "follow" as an option:
            following = not following

    posts = Post.objects.filter(user=User.objects.get(username=uName))
    imgposts = ImagePost.objects.filter(user=User.objects.get(username=uName))
    return render(request, 'forum/UserFeed.html',
                  {'forum_page': 'active', 'posts': posts, 'uName': uName, 'following': following,
                   'imgposts': imgposts})


@login_required
def followingpage(request):
    """ Populates the following page with all people the user is following.
        They must be logged in.
    """
    userProfile = Profile.objects.get(user=request.user)
    following = userProfile.following.all()
    posts = Post.objects.filter(user__in=following)
    imgposts = ImagePost.objects.filter(user__in=following)
    return render(request, 'forum/healthForumFollowingPage.html',
                  {'forum_page': 'active', 'posts': posts, 'imgposts': imgposts})


def valid_post(request):
    "Checks if a post is valid before saving it"
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            post = form.save(commit=False)
            form.instance.slug = get_random_string(8, '0123456789')
            post.post = post
            post.save()

            return redirect('forum:healthForumMain')
    else:
        form = PostForm()
    return render(request, 'forum/healthForumPost.html', {'forum_page': 'active', 'form': form})


def valid_image_post(request):
    """ Ensures that the image post is valid before savig"""
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            post = form.save(commit=False)
            form.instance.slug = get_random_string(8, '0123456789')  # creates random slug
            post.post = post
            post.save()
            return redirect('forum:healthForumMain')
    else:
        form = ImagePostForm()
    return render(request, 'forum/healthForumImgPost.html', {'forum_page': 'active', 'form': form})


def post_detail(request, slug):
    """ Populates the post detail page and ensures all comments are valid"""
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            if request.user is not None:
                form.instance.name = request.user
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('forum:post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'forum/healthForumPost_detail.html', {'forum_page': 'active', 'post': post, 'form': form})


def delete_imgpost(request):
    """ Deletes the image post """
    all_image_posts = ImagePost.objects.filter(user=request.user)
    if request.method == 'POST':
        if request.POST.get('delete_imgpost') != None:
            i = int(request.POST.get('delete_imgpost'))
            imgpost = all_image_posts.filter(slug=i)
            imgpost.delete()
            messages.success(request, "Image post deleted.")
    return redirect('forum:healthForumMain')


def delete_post(request):
    """ Deletes the post """
    all_posts = Post.objects.filter(user=request.user)
    if request.method == 'POST':
        if request.POST.get('delete_post') != None:
            i = int(request.POST.get('delete_post'))
            post = all_posts.filter(slug=i)
            post.delete()
            messages.success(request, "Forum post deleted.")
    return redirect('forum:healthForumMain')
