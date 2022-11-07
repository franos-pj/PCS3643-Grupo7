from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Route(models.Model):
    # Classe Rota

    flightCode = models.CharField(max_length=20, primary_key=True)
    airline = models.CharField(max_length=20, null=False)
    departureAirport = models.CharField(max_length=3, null=False)
    arrivalAirport = models.CharField(max_length=3, null=False)
    scheduledTime = models.TimeField(null=False)

    class Meta:
        db_table = 'rotas'


class Flight(models.Model):
    # Classe Voo

    flightId = models.BigAutoField(primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    scheduledDate = models.DateField(null=False)
    realDate = models.DateField(null=True)
    realTime = models.TimeField(null=True)
    status = models.CharField(max_length=20, null=True)

    class Meta:
        permissions = (
            ('can_change_scheduled_date_flight',
             'Can change scheduled date for flights'),
            ('can_change_real_date_flight', 'Can change real date for flights'),
            ('can_change_real_time_flight', 'Can change real time for flights'),
            ('can_change_status_as_airline_flight',
             'Can change flight status as airline'),
            ('can_change_status_as_tower_flight',
             'Can change flight status as control tower'),
            ('can_change_status_as_pilot_flight',
             'Can change flight status as pilot'),
        )
        db_table = 'voos'
