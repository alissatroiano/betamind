from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('getResponse', views.getResponse, name='getResponse'),
   
]
