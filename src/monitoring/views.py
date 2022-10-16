from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'Dashboard.html')

def flightInfo(request):
    return render(request, 'Flight_info.html')