from django.db import models

# Classe Rota
class Route(models.Model):
    flightCode = models.CharField(max_length=20, primary_key=True)
    airline = models.CharField(max_length=20, null=False)
    departureAirport = models.CharField(max_length=3, null=False)
    arrivalAirport = models.CharField(max_length=3, null=False)
    scheduledTime = models.TimeField(null=False)

    class Meta:
        db_table = 'rotas'

# Classe Voo
class Flight(models.Model):
    flightId = models.BigAutoField(primary_key=True)
    flightCode = models.ForeignKey(Route, on_delete=models.CASCADE)
    scheduledDate = models.DateField(null=False)
    realDate = models.DateField(null=True)
    realTime = models.TimeField(null=True)
    status = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'voos'