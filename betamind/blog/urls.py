from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]