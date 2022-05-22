from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Mood, Post, Comment
from .forms import PostForm
from django.contrib.auth import get_user_model


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
    Render blog index page, and handle POST requests to
    add a blog to the page.
    """

    current_user = get_user_model().objects.get(username=request.user)

    if request.method == "POST":
        post_form = PostForm(request.POST or None)
        if post_form.is_valid():
            form = post_form.save(commit=False)
            form.post_sender = current_user
            form.save()
            success_msg = "Thanks for sharing with us."
            return JsonResponse({"success_msg": success_msg})
        else:
            return JsonResponse({"errors": post_form.errors.as_json()})

    posts = None
    if "mood_name" in request.GET:
        query_param = request.GET.get("mood_name")
        posts = Post.objects.filter(mood__name=query_param)
    else:
        posts = Post.objects.all()
    moods = Mood.objects.all()

    post_form = PostForm()

    context = {
        'posts': posts,
        'moods': moods,
        'post_form': post_form
    }

    return render(request, 'blog.html', context)


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
