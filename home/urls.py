from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('team/', views.TeamView.as_view(), name="team"),
]