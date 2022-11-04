from traceback import print_tb
import json
from django.shortcuts import HttpResponse, render, get_object_or_404
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "Dashboard.html")


def flightInfo(request):
    return render(request, "flight-info.html")


def chooseReport(request):
    return render(request, "choose-report.html")


def generalReport(request):
    return render(request, "general-report.html")


def specificReport(request):
    return render(request, "specific-report.html")


def routesAndFlights(request):
    return render(request, "routes-and-flights.html")


def routesRecords(request):
    if request.method == "POST":
        data = request.POST
        flightCode = data["flightCode"]
        if Route.objects.filter(flightCode=flightCode).exists():
            redirectPath = "routes-records/info/" + flightCode + "/"
            response = {"success": True, "id": flightCode, "redirectPath": redirectPath}
            return HttpResponse(json.dumps(response))
        else:
            response = {"success": False, "id": flightCode, "redirectPath": None}
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
    return render(request, "flights-records.html")


def flightRecordInfo(request):
    return render(request, "flight-record-info.html")


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

    return render(request, "flight-registration.html", context)
