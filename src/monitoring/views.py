from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from datetime import datetime, timedelta
import json
from django.shortcuts import HttpResponse, render, get_object_or_404
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, F, Q, ExpressionWrapper, DurationField
from django.http import HttpResponseRedirect
from django.urls import reverse

statusDeparturePermissionTree = {
    "Airlines": {"não iniciado": ["embarcando", "cancelado"],
                 "embarcando": ["programado", "cancelado"]},
    "Pilots": {"taxiando": ["pronto", "cancelado"],
               "autorizado": ["em voo", "cancelado"]},
    "ControlTower": {"programado": ["taxiando", "cancelado"],
                     "pronto": ["autorizado", "cancelado"],
                     "em voo": ["decolagem finalizada"]},
}

statusArrivalPermissionTree = {
    "ControlTower": {"não iniciado": ["em voo"],
                     "em voo": ["aterrisado"]},
}


def index(request):

    loginForm = UserLoginForm(request.POST or None, request.FILES or None)

    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request=request, username=username, password=password)

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
                'failure': True,
                'loginForm': loginForm,
            }

    else:
        logout(request)

        context = {
            'failure': None,
            'loginForm': loginForm,
        }

    return render(request, "index.html", context=context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name
                  in ['Pilots', 'Airlines', 'ControlTower'])
def dashboard(request):
    context = {}
    flightList = Flight.objects.all().exclude(status='cancelado').exclude(
        status='aterrissado').exclude(status='decolagem finalizada').order_by('-scheduledDate')
    context['flightList'] = flightList
    return render(request, "dashboard.html", context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name
                  in ['Pilots', 'Airlines', 'ControlTower'])
def flightInfo(request, flightId):
    context = {}
    userGroup = Group.objects.get(user=request.user).name
    timeInputDisabled = True
    flight = get_object_or_404(Flight, flightId=flightId)
    flightCurrentStatus = flight.status
    if (flightCurrentStatus is None):
        flightCurrentStatus = 'não iniciado'
    try:
        if (flight.route.arrivalAirport == "FLL"):
            optionStatus = statusArrivalPermissionTree[userGroup][flightCurrentStatus]
        else:
            optionStatus = statusDeparturePermissionTree[userGroup][flightCurrentStatus]
    except:
        context['error'] = {
            'code': '403',
            'errorMsg': " Acesso ao voo bloqueado.",
            'description': "Você não possui permissão para atualizar, no momento, o voo " + flight.route.flightCode + '[' + str(flight.scheduledDate) + ']',
        }
        return render(request, "error-page.html", context)
    if (userGroup == 'ControlTower' and (flightCurrentStatus == 'em voo')):
        timeInputDisabled = False
    if request.method == "POST":
        error = False
        error_msg = '<p>Os seguintes campos não estão presentes</p>'
        updateDate = request.POST
        realTimeUpdate = updateDate['realTime']
        realDateUpdate = updateDate['realDate']
        statusUpdate = updateDate['status']
        if (statusUpdate in ['decolagem finalizada', 'aterrissado']):

            if (len(realTimeUpdate) > 0):
                realTimeUpdateObj = datetime.datetime.strptime(
                    realTimeUpdate, '%H:%M').time()
            else:
                error = True
                error_msg = error_msg + '<p>Horário Real</p>'
            if (len(realDateUpdate) > 0):
                realDateUpdateObj = datetime.datetime.strptime(
                    realDateUpdate, '%Y-%m-%d').date()
                if (flight.scheduledDate < realDateUpdateObj):
                    flight.realDate = realDateUpdateObj
                    flight.realTime = realTimeUpdateObj
                elif (flight.scheduledDate == realDateUpdateObj and realTimeUpdateObj >= flight.route.scheduledTime):
                    flight.realDate = realDateUpdateObj
                    flight.realTime = realTimeUpdateObj
                else:
                    error = True
                    error_msg = '<p>Entrada inválida: Momento real deve ser posterior à previsão</p>'
            else:
                error = True
                error_msg = error_msg + '<p>Data Real</p>'

        if (statusUpdate != flightCurrentStatus):
            flight.status = statusUpdate
        else:
            error = True
            error_msg = '<p>Não houve atualização de status</p>'

        if (not error):
            response = {
                'success': True,
                'id': flight.route.flightCode + ' [' + str(flight.scheduledDate) + ']',
                'error_msg': None
            }
            flight.save()
        else:
            response = {
                'success': False,
                'id': flight.route.flightCode + ' [' + str(flight.scheduledDate) + ']',
                'error_msg': error_msg + '</li>'
            }
        return HttpResponse(json.dumps(response))
    context['flight'] = flight
    context['optionStatus'] = optionStatus
    context['flightCurrentStatus'] = flightCurrentStatus
    context['timeInputDisabled'] = timeInputDisabled
    return render(request, "flight-info.html", context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Managers')
def chooseReport(request):
    if request.method == "POST":
        data = request.POST
        start_date = data["start_date"]
        end_date = data["end_date"]
        start_date_obj = datetime.datetime.strptime(
            start_date, '%Y-%m-%d').date()
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        queryset = Flight.objects.filter(
            scheduledDate__range=[start_date_obj, end_date_obj])
        queryset = queryset.filter(status='aterrissado') | queryset.filter(
            status='cancelado').order_by('realDate')
        if queryset.exists():
            response = {"success": True}
            return HttpResponse(json.dumps(response))
        else:
            response = {"success": False}
            return HttpResponse(json.dumps(response))
    else:
        return render(request, "choose-report.html")


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Managers')
def specificReport(request, startDate, endDate):
    context = {}
    start_date_obj = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
    end_date_obj = datetime.datetime.strptime(endDate, '%Y-%m-%d').date()
    queryset = Flight.objects.filter(
        scheduledDate__range=[start_date_obj, end_date_obj])
    data = queryset.filter(status='aterrissado') | queryset.filter(
        status='cancelado').order_by('scheduledDate')
    context['data'] = list(data)
    return render(request, "specific-report.html", context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Managers')
def generalReport(request, startDate, endDate):
    context = {}
    start_date_obj = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
    end_date_obj = datetime.datetime.strptime(endDate, '%Y-%m-%d').date()
    queryset_all = Flight.objects.filter(
        scheduledDate__range=[start_date_obj, end_date_obj])
    queryset_all = queryset_all.filter(
        status='aterrissado') | queryset_all.filter(status='cancelado')
    queryset_all = queryset_all.annotate(difDate=ExpressionWrapper(F('realDate') - F('scheduledDate'), output_field=DurationField()),
                                         difTime=ExpressionWrapper(
                                             F('realTime') - F('route__scheduledTime'), output_field=DurationField())
                                         )
    data = queryset_all.values('route__airline').annotate(
        numFlights=Count('flightId'),
        numFlightsCancelled=Count('flightId', filter=Q(status='cancelado')),
        numFlightsDeparture=Count(
            'flightId', filter=Q(route__departureAirport="FLL")),
        numFlightsDelayed=Count('flightId', filter=(
            Q(difDate__gt=timedelta(seconds=0)) | Q(difTime__gt=timedelta(seconds=0))))
    ).order_by('route__airline')
    context['data'] = list(data)
    return render(request, "general-report.html", context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routesAndFlights(request):
    return render(request, "routes-and-flights.html")


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routesRecords(request):
    if request.method == "POST":
        data = request.POST
        flightCode = data["flightCode"]
        if Route.objects.filter(flightCode=flightCode).exists():
            redirectPath = "routes-records/info/" + flightCode + "/"
            response = {"success": True, "id": flightCode,
                        "redirectPath": redirectPath}
            return HttpResponse(json.dumps(response))
        else:
            response = {"success": False,
                        "id": flightCode, "redirectPath": None}
            return HttpResponse(json.dumps(response))
    else:
        return render(request, "routes-records.html")


@csrf_exempt
@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routeInfo(request, flightCode):
    context = {}
    route = get_object_or_404(Route, pk=flightCode)
    form = RouteForm(request.POST or None, instance=route)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            response = {
                "id": form.cleaned_data["flightCode"],
                "success": True,
                "error": None,
            }
            return HttpResponse(json.dumps(response))
        else:
            response = {
                "id": form.cleaned_data["flightCode"],
                "success": False,
                "error": form.errors.as_json(),
            }
            return HttpResponse(json.dumps(response))

    elif request.method == "DELETE":
        deletion = route.delete()
        response = {"id": flightCode, "success": True}
        return HttpResponse(json.dumps(response))

    context["route"] = route
    context["id"] = flightCode
    context["form"] = form
    return render(request, "route-info.html", context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def routeRegistration(request):
    context = {}

    # create object of form
    form = RouteForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        response = {
            "id": form.cleaned_data["flightCode"],
            "success": True,
            "error": None,
        }

        return HttpResponse(json.dumps(response))
    elif request.method == "POST":

        response = {
            "id": form.data["flightCode"],
            "success": False,
            "error": form.errors.as_json(),
        }

        return HttpResponse(json.dumps(response))

    context["form"] = form

    return render(request, "route-registration.html", context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def flightsRecords(request):
    if request.method == "POST":
        data = request.POST
        route = data["route"]
        scheduledDate = data["scheduledDate"]
        if Flight.objects.filter(route=route, scheduledDate=scheduledDate).exists():
            redirectPath = (
                "flights-records/flights-record-info/"
                + route
                + "/"
                + scheduledDate
                + "/"
            )
            response = {
                "success": True,
                "id": route + ' [' + scheduledDate + ']',
                "redirectPath": redirectPath,
            }
            return HttpResponse(json.dumps(response))
        else:
            response = {
                "success": False,
                "id": route + ' [' + scheduledDate + ']',
                "redirectPath": None,
            }
            return HttpResponse(json.dumps(response))
    else:
        return render(request, "flights-records.html")


@csrf_exempt
@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def flightRecordInfo(request, route, scheduledDate):
    context = {}
    flight = get_object_or_404(
        Flight, route=route, scheduledDate=scheduledDate)
    
    flightCurrentStatus = flight.status
    scheduledDateDisabled = True
    if (flightCurrentStatus is None):
        scheduledDateDisabled = False
    
    form = FlightForm(request.POST or None, instance=flight)
    if request.method == "POST":
        
        if form.is_valid():
            data = request.POST
            route = data["route"]
            scheduledDate = data["scheduledDate"]
            if (Flight.objects.filter(route=route, scheduledDate=scheduledDate).exists()):
                response = {
                    "id": form.data["route"] + ' [' + form.data["scheduledDate"] + ']',
                    "success": False,
                    "error_msg": "Voo informado já existe"
                }
                return HttpResponse(json.dumps(response))
            else:
                form.save()
                data = request.POST
                redirectPath = (
                    "/routes-and-flights/flights-records/flights-record-info/"
                    + route
                    + "/"
                    + data["scheduledDate"]
                    + "/"
                )
                print(redirectPath)
                response = {
                    "id": route + ' [' + scheduledDate + ']',
                    "redirectPath": redirectPath,
                    "success": True,
                    "error": None,
                }
                return HttpResponse(json.dumps(response))
        else:
            response = {
                "id": route + ' [' + scheduledDate + ']',
                "success": False,
                "error": form.errors.as_json(),
                "error_msg": ""
            }
            return HttpResponse(json.dumps(response))

    elif request.method == "DELETE":
        deletion = flight.delete()
        response = {
            "route": route,
            "scheduledDate": scheduledDate,
            "success": True,
        }
        return HttpResponse(json.dumps(response))

    context["scheduledDateDisabled"] = scheduledDateDisabled
    context["flight"] = flight
    context["route"] = route
    context["scheduledDate"] = scheduledDate
    context["form"] = form
    return render(request, "flight-record-info.html", context)


@login_required
@user_passes_test(lambda user: Group.objects.get(user=user).name == 'Operators')
def flightRegistration(request):

    context = {}

    # create object of form
    form = FlightForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        data = request.POST
        route = data["route"]
        scheduledDate = data["scheduledDate"]
        if (Flight.objects.filter(route=route, scheduledDate=scheduledDate).exists()):
            response = {
                "id": form.data["route"] + ' [' + form.data["scheduledDate"] + ']',
                "success": False,
                "error_msg": "Voo informado já existe"
            }
        else:
            form.save()
            response = {
                "id": form.data["route"] + ' [' + form.data["scheduledDate"] + ']',
                "success": True,
                "error": None,
            }
        return HttpResponse(json.dumps(response))
    elif request.method == "POST":
        response = {
            "id": form.data["route"] + ' [' + form.data["scheduledDate"] + ']',
            "success": False,
            "error": form.errors.as_json(),
            "error_msg": ""
        }
        return HttpResponse(json.dumps(response))

    context["form"] = form

    return render(request, "flight-registration.html", context)
