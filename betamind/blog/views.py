from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.forms.models import modelformset_factory
from .models import Mood, Post, Comment
from core.models import User
from .forms import PostForm


@login_required
def blog(request):
    """
    Blog index page
    """
    posts = Post.objects.all()
    moods = Mood.objects.all()

    return render(request, 'blog.html', {'posts': posts, 'moods': moods})


@login_required
def create_post(request):
    """
    A method to let users create a new blog post
    """
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return Post.objects.create(post=post, user=request.user)
            return redirect(reverse('blog'))
        else:
            print(form.errors)
            return render(request, 'create_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/edit_post.html', {
        'form': PostForm(instance=post),
        'moods': Mood.objects.all(),
        'post': post,
    })


# @login_required
# def delete_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.delete()
#     return redirect('blog_index')
