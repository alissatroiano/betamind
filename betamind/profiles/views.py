from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from .models import UserProfile


class ProfileView(TemplateView):

    template_name = "profiles/profile.html"
    
