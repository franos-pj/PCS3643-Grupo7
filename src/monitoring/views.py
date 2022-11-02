from traceback import print_tb
import json
from django.shortcuts import HttpResponse, render, get_object_or_404
from .forms import *
from .models import *

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'Dashboard.html')

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

def routeInfo(request, flightCode):
    context ={}
    route = get_object_or_404(Route, pk=flightCode)
    print(request.GET)
    context['route']= route
    return render(request, 'route-info.html', context)

def routeRegistration(request):
    context ={}

    # create object of form
    form = RouteForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        response = {
            'id': form.cleaned_data["flightCode"],
            'success': True,
            'error': None
            }
        print("form valid")
        print('myresponse', response)
        return HttpResponse(json.dumps(response))
    elif request.method == 'POST':
        print("form invalid", form.data)
        response = {
            'id': form.data["flightCode"],
            'success': False,
            'error': form.errors.as_json()
            }
        print('myresponse', response)
        return HttpResponse(json.dumps(response)) 

    context['form']= form
    print(context)

    return render(request, 'route-registration.html', context)

def flightsRecords(request):
    return render(request, 'flights-records.html')

def flightRecordInfo(request):
    return render(request, 'flight-record-info.html')

def flightRegistration(request):
    return render(request, 'flight-registration.html')