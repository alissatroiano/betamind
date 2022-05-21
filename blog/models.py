from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
import uuid

from django.utils import timezone

from datetime import datetime
now = timezone.now

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

MOOD = (
    (0, "Happy"),
    (1, "Sad"),
    (2, "Angry"),
    (3, "Surprised"),
    (4, "Scared"),
    (5, "Disgusted"),
    (6, "Anxious"),
    (7, "Bored"),
    (8, "Tired"),
    (9, "Depressed"),
    (10, "Frustrated"),
)

class Mood(models.Model): 
    """
    Moods to categorize different types of blog posts
    """
    mood = models.IntegerField(choices=MOOD, default=0)
    unique_id = models.UUIDField(default=uuid.uuid4, max_length=100, unique=True, primary_key=True)
    slug = models.SlugField(max_length=40, unique=True) 
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.mood)

    def get_friendly_name(self):
        return self.friendly_name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return "/mood/%s/" % self.slug


class Post(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    post_sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    mood = models.ForeignKey(
        'Mood', null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.created_at.year, self.created_at.month, self.slug)


class Comment(models.Model):
    comment_sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,related_name='comment_sender')
    post = models.ForeignKey(Post, on_delete= models.CASCADE,related_name='blog_post')
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
