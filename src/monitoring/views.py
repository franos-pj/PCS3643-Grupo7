from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm
from monitoring.models import User


def index(request):

    loginForm = UserLoginForm(request.POST or None, request.FILES or None)

    if (request.method == 'POST'):
        # Create a form instance and populate it with data from the request (binding):
        user = User.objects.get(username=loginForm.data['username'])
        if (user.password == loginForm.data['password']):
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('report/general'))

    else:

        context = {
            'loginForm': loginForm,
        }
        return render(request, "index.html", context=context)


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
