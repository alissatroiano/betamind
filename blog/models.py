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

class Category(models.Model):

    class Meta: 
        verbose_name_plural = "Categories" 

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40, unique=True) 
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    parent = models.ForeignKey('self',blank=True, null=True, on_delete=models.SET_NULL, related_name='children')
    
    def __str__(self):
        return (self.name)

    def get_friendly_name(self):
        return self.friendly_name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return "/categories/%s/" % self.slug


class Post(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    status = models.CharField(choices=STATUS, default=0)
    mood = models.CharField(max_length=254, choices=MOOD, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, )
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)


class Comment(models.Model):
    comment_sender = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_comments')
    post = models.ForeignKey(Post, on_delete= models.CASCADE,related_name='blog_comments')
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
