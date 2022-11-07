from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm


def index(request):

    loginForm = UserLoginForm(request.POST or None, request.FILES or None)

    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            userGroup = Group.objects.get(user=user).name
            if (userGroup in ["Pilots", "Airlines", "ControlTower"]):
                return HttpResponseRedirect(reverse('dashboard'))
            elif (userGroup == "Operators"):
                return HttpResponseRedirect(reverse('routesAndFlights'))
            elif (userGroup == "Managers"):
                return HttpResponseRedirect(reverse('chooseReport'))

        else:
            context = {
                'success': False,
                'loginForm': loginForm,
            }

    else:
        logout(request)

        context = {
            'success': None,
            'loginForm': loginForm,
        }

    return render(request, "index.html", context=context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name
                  in ['Pilots', 'Airlines', 'ControlTower'])
def dashboard(request):
    print(request.user.get_username())
    return render(request, 'dashboard.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name
                  in ['Pilots', 'Airlines', 'ControlTower'])
def flightInfo(request):
    return render(request, 'flight-info.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Managers')
def chooseReport(request):
    return render(request, 'choose-report.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Managers')
def generalReport(request):
    return render(request, 'general-report.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Managers')
def specificReport(request):
    return render(request, 'specific-report.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routesAndFlights(request):
    return render(request, 'routes-and-flights.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routesRecords(request):
    return render(request, 'routes-records.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routeInfo(request):
    return render(request, 'route-info.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routeRegistration(request):
    return render(request, 'route-registration.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def flightsRecords(request):
    return render(request, 'flights-records.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def flightRecordInfo(request):
    return render(request, 'flight-record-info.html')


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def flightRegistration(request):
    return render(request, 'flight-registration.html')
