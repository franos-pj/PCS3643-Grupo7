from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def flightInfo(request):
    return render(request, 'flight-info.html')

def chooseReport(request):
    return render(request, 'choose-report.html')

def generalReport(request):
    return render(request, 'general-report.html')

def specificReport(request):
    return render(request, 'specific-report.html')