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

def routesAndFlights(request):
    return render(request, 'routes-and-flights.html')

def routesRecords(request):
    return render(request, 'routes-records.html')

def routeInfo(request):
    return render(request, 'route-info.html')

def routeRegistration(request):
    return render(request, 'route-registration.html')

def flightsRecords(request):
    return render(request, 'flights-records.html')

def flightRecordInfo(request):
    return render(request, 'flight-record-info.html')

def flightRegistration(request):
    return render(request, 'flight-registration.html')