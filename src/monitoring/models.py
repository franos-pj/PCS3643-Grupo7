import datetime
from django.db import models


class Route(models.Model):
    # Classe Rota

    flightCode = models.CharField(max_length=20, primary_key=True, verbose_name="Código de Voo")
    airline = models.CharField(max_length=20, null=False, verbose_name="Companhia")
    departureAirport = models.CharField(max_length=3, null=False, verbose_name="Aeroporto de Origem")
    arrivalAirport = models.CharField(max_length=3, null=False, verbose_name="Aeroporto de Destino")
    scheduledTime = models.TimeField(null=False, verbose_name="Horário Previsto")

    class Meta:
        db_table = 'rotas'

    def __str__(self):
        return self.flightCode


class Flight(models.Model):
    # Classe Voo

    flightId = models.BigAutoField(primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="Rota")
    scheduledDate = models.DateField(null=False, verbose_name="Data Prevista")
    realDate = models.DateField(null=True, verbose_name="Data Real")
    realTime = models.TimeField(null=True, verbose_name="Horário Real")
    status = models.CharField(max_length=20, null=True, verbose_name="Status")

    class Meta:
        db_table = 'voos'

    def __str__(self):
        return "Voo: " + self.route.__str__() + " " + str(self.scheduledDate)
    
    def delay(self):
        if (self.realDate):
            realDateTime = datetime.datetime.combine(self.realDate, self.realTime)
            scheduledDateTime = datetime.datetime.combine(self.scheduledDate, self.route.scheduledTime)
            delay = realDateTime - scheduledDateTime
            if (delay.total_seconds() > 0):
                if (delay.total_seconds() < 86400):
                    hours = str(delay).split(':')[:2][0]
                    mins = str(delay).split(':')[:2][1]
                    return hours + 'h' + mins + 'min'
                else:
                    return delay;
            else:
                return 'sem atraso'
        else:
            return 'cancelado'
    
    @property
    def delayNumber(self):
        realDateTime = datetime.datetime.combine(self.realDate, self.realTime)
        scheduledDateTime = datetime.datetime.combine(self.scheduledDate, self.route.scheduledTime)
        delay = realDateTime - scheduledDateTime
        return delay.total_seconds()
        
