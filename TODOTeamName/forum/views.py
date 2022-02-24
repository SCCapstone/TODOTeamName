from django.shortcuts import render, redirect

from .models import *
from .forms import *


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'forum/healthForumMain.html', {'posts': posts})


def valid_post(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.post = post
            post.save()

            return redirect('forum:healthForumMain')
    else:
        form = PostForm()
    return render(request, 'forum/healthForumPost.html', {'form': form})


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
