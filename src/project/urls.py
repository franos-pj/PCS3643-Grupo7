"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from monitoring import views

urlpatterns = [
    # Disabled admin site for the purpose of evaluation
    # path('admin/', admin.site.urls),
    path('', views.index, name='login'),
    path('monitoring/dashboard', views.dashboard, name='dashboard'),
    path('monitoring/flight-info', views.flightInfo, name='flight'),
    path('report', views.chooseReport, name='chooseReport'),
    path('report/general/<str:startDate>/<str:endDate>/', views.generalReport, name='generalReport'),
    path('report/specific/<str:startDate>/<str:endDate>/', views.specificReport, name='specificReport'),
    path('routes-and-flights', views.routesAndFlights, name='routesAndFlights'),
    path('routes-and-flights/routes-records', views.routesRecords, name='routesRecords'),
    path('routes-and-flights/routes-records/info/<str:flightCode>/', views.routeInfo, name='routeInfo'),
    path('routes-and-flights/routes-records/register', views.routeRegistration, name='routeRegistration'),
    path('routes-and-flights/flights-records', views.flightsRecords, name='flightsRecords'),
    path('routes-and-flights/flights-records/register', views.flightRegistration, name='flightRegistration'),
    path('routes-and-flights/flights-records/flights-record-info', views.flightRecordInfo, name='flightRecordInfo')
]
