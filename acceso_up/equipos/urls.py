from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('equipos', views.equipos, name='equipos'),
    path('equipos/bitacora', views.bitacora, name='bitacora'),
    path('equipos/monitoreo', views.monitoreo, name='monitoreo'),
    path('reportes', views.reportes, name='reportes')
]
