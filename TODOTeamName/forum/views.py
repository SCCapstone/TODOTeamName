from django.shortcuts import render, redirect

from .models import *
from .forms import *


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'forum/healthForumMain.html', {'posts': posts})

# TODO - fix forum posts

# def post_detail(request, slug):
#     post = Post.objects.get(slug = slug)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit =False)
#             comment.post = post
#             comment.save()

#             return redirect('forum:healthForumPost_detail.html',slug = post.slug)
#     else:
#         form = CommentForm()
#     return render(request, 'meal_planner_main/homePage_detail.html') #, {'post': post, 'form': form})
