from django.shortcuts import render

def firstView(request):
    return render(request, 'FIRST.html')

def monitoringView(request):
    return render(request, 'MONITORING.html')

def createReportView(request):
    return render(request, 'CREATE_REPORT.html')

def flightRegistrationView(request):
    return render(request, 'FLIGHT_REGISTRATION.html')