from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/crear', views.crear, name='crear'),
  
]
