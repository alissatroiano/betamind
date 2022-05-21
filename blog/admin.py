from django.contrib import admin
from django.conf import settings

from .models import Category, Post, Comment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'friendly_name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_sender', 'post', 'created_at', 'comment']
    list_filter = ['comment', 'comment_sender', 'post']
    search_fields = ['comment_sender', 'comment', 'created_at']