from datetime import datetime, timedelta
import json
from django.shortcuts import HttpResponse, render, get_object_or_404
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, F, Q, ExpressionWrapper, DurationField


def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "Dashboard.html")


def flightInfo(request):
    return render(request, "flight-info.html")


def chooseReport(request):
    if request.method == "POST":
        data = request.POST
        start_date = data["start_date"]
        end_date = data["end_date"]
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        queryset = Flight.objects.filter(scheduledDate__range=[start_date_obj,end_date_obj])
        queryset = queryset.filter(status='aterrissado') | queryset.filter(status='cancelado').order_by('realDate')
        print(list(queryset))
        if queryset.exists():
            response = {"success": True}
            return HttpResponse(json.dumps(response))
        else:
            response = {"success": False}
            return HttpResponse(json.dumps(response))
    else:
        return render(request, "choose-report.html")


def generalReport(request, startDate, endDate):
    context={}
    start_date_obj = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
    end_date_obj = datetime.datetime.strptime(endDate, '%Y-%m-%d').date()
    queryset_all = Flight.objects.filter(scheduledDate__range=[start_date_obj,end_date_obj])
    print('1 ->', queryset_all.values())
    print("")
    queryset_all = queryset_all.filter(status='aterrissado') | queryset_all.filter(status='cancelado')
    print('2 ->', queryset_all.values())
    print("")
    queryset_all = queryset_all.annotate(difDate=ExpressionWrapper(F('realDate') - F('scheduledDate'), output_field=DurationField()),
                                         difTime=ExpressionWrapper(F('realTime') - F('route__scheduledTime'), output_field=DurationField())
                                        )
    print('3 ->', list(queryset_all.values()))
    data = queryset_all.values('route__airline').annotate(
        numFlights=Count('flightId'), 
        numFlightsCancelled=Count('flightId', filter=Q(status='cancelado') ),
        numFlightsDeparture=Count('flightId', filter=Q(route__departureAirport="FLL")),
        numFlightsDelayed=Count('flightId', filter=(Q(difDate__gt=timedelta(seconds=0)) | Q(difTime__gt=timedelta(seconds=0))))
    ).order_by('route__airline')
    context['data'] = list(data)
    print(list(data))
    return render(request, "general-report.html", context)

def specificReport(request, startDate, endDate):
    context={}
    start_date_obj = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
    end_date_obj = datetime.datetime.strptime(endDate, '%Y-%m-%d').date()
    queryset = Flight.objects.filter(scheduledDate__range=[start_date_obj,end_date_obj])
    data = queryset.filter(status='aterrissado') | queryset.filter(status='cancelado').order_by('scheduledDate')
    context['data'] = list(data)
    print(list(queryset))
    return render(request, "specific-report.html", context)


def routesAndFlights(request):
    return render(request, "routes-and-flights.html")


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
def routeInfo(request, flightCode):
    context = {}
    print(request)
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
        print(deletion)
        response = {"id": flightCode, "success": True}
        return HttpResponse(json.dumps(response))

    context["route"] = route
    context["id"] = flightCode
    context["form"] = form
    return render(request, "route-info.html", context)


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
        print("form valid")
        print("myresponse", response)
        return HttpResponse(json.dumps(response))
    elif request.method == "POST":
        print("form invalid", form.data)
        response = {
            "id": form.data["flightCode"],
            "success": False,
            "error": form.errors.as_json(),
        }
        print("myresponse", response)
        return HttpResponse(json.dumps(response))

    context["form"] = form

    return render(request, "route-registration.html", context)


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
                "route": route,
                "scheduledDate": scheduledDate,
                "redirectPath": redirectPath,
            }
            return HttpResponse(json.dumps(response))
        else:
            response = {
                "success": False,
                "route": route,
                "scheduledDate": scheduledDate,
                "redirectPath": None,
            }
            return HttpResponse(json.dumps(response))
    else:
        return render(request, "flights-records.html")


@csrf_exempt
def flightRecordInfo(request, route, scheduledDate):
    context = {}
    print(request)
    flight = get_object_or_404(Flight, route=route, scheduledDate=scheduledDate)
    form = FlightForm(request.POST or None, instance=flight)

    print(flight)
    print(form)

    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         response = {
    #             "route": form.cleaned_data["route"],
    #             "scheduledDate": form.cleaned_data["scheduledDate"],
    #             "success": True,
    #             "error": None,
    #         }
    #         return HttpResponse(json.dumps(response))
    #     else:
    #         response = {
    #             "route": form.cleaned_data["route"],
    #             "scheduledDate": form.cleaned_data["scheduledDate"],
    #             "success": False,
    #             "error": form.errors.as_json(),
    #         }
    #         return HttpResponse(json.dumps(response))

    if request.method == "DELETE":
        deletion = flight.delete()
        print(deletion)
        response = {
            "route": route,
            "scheduledDate": scheduledDate,
            "success": True,
        }
        return HttpResponse(json.dumps(response))

    context["flight"] = flight
    context["route"] = route
    context["scheduledDate"] = scheduledDate
    context["form"] = form
    return render(request, "flight-record-info.html", context)


def flightRegistration(request):

    context = {}

    # create object of form
    form = FlightForm(request.POST or None, request.FILES or None)

    print(form)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        response = {
            "id": form.data["route"],
            "success": True,
            "error": None,
        }
        print("form valid")
        print("myresponse", response)
        return HttpResponse(json.dumps(response))
    elif request.method == "POST":
        print("form invalid", form.data)
        response = {
            "id": form.data["route"],
            "success": False,
            "error": form.errors.as_json(),
        }
        print("myresponse", response)
        return HttpResponse(json.dumps(response))

    context["form"] = form

    return render(request, "flight-registration.html", context)