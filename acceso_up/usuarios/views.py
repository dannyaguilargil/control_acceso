from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def crear(request):
    return render(request,'crear.html')
