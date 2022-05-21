from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    # path('blog/select_mood', views.select_mood, name='select_mood'),
]