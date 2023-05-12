from django.shortcuts import render

def equipos(request):
    return render(request,'equipos.html')

def bitacora(request):
    return render(request,'bitacora.html')

def monitoreo(request):
    return render(request,'monitoreo.html')