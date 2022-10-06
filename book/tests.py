from django.test import TestCase
import datetime

# Test Models
from models import Flight, Route

class FlightModelTest(TestCase):

    @classmethod
    def test_creation(self):
        Route.objects.create(
            flightCode='AF0443',
            airline='Air France', 
            departureAirport = 'FLL',
            arrivalAirport = 'CDG', 
            scheduledTime = datetime.time(10, 30, 0)
        )

        Flight.objects.create(
            flightCode='AF0443',
            scheduledDate = datetime.date(year=2022, month=11, day=26),
        )

        flight_1 = Flight.objects.get(flightCode='AF0443')
        self.assertEqual(flight_1.scheduledDate, datetime.date(year=2022, month=11, day=26))