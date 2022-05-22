from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<str:post_id>/', views.edit_post, name='edit_post'),
]