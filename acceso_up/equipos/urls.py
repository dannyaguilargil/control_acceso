from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('equipos', views.equipos, name='equipos'),
  
]
