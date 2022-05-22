from django.db import models
from django.conf import settings
from django.utils.text import slugify

from django.contrib.auth.models import User
from django.utils import timezone

from datetime import datetime
now = timezone.now


class Mood(models.Model): 
    """
    Moods to categorize different types of blog posts
    """
    class Meta:
        verbose_name = "Mood"
        verbose_name_plural = "Moods"

    mood = models.CharField(max_length=254)

    def __str__(self):
        return self.mood


class Post(models.Model):
    title = models.CharField(max_length=254)
    post_sender = models.ForeignKey(User, on_delete= models.CASCADE)
    mood = models.ForeignKey(
        Mood, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_sender = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    create_post = models.DateTimeField(auto_now_add=True)
    edit_post = models.DateTimeField(auto_now_add=True)
    delete_post = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-create_post']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.pk