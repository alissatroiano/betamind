from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.forms.models import modelformset_factory
from .models import Mood, Post, Comment
from .forms import PostForm


# @login_required
# def select_mood(request):
#     """
#     Select mood to create a post
#     """
#     mood_form = MoodForm()
#     return render(request, 'blog/select_mood.html', {'mood_form': mood_form})


@login_required
def blog(request):
    """
    Blog index page
    """
    posts = Post.objects.all()
    moods = Mood.objects.all()

    return render(request, 'blog.html')


# @login_required
# def edit_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     return render(request, 'blog/edit_post.html', {
#         'form': PostForm(instance=post),
#         'moods': Mood.objects.all(),
#         'post': post,
#     })


# @login_required
# def delete_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.delete()
#     return redirect('blog_index')
