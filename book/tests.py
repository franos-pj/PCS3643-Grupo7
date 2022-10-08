from django.test import TestCase
import datetime

# Test Models
from book.models import Route, Flight


class RouteModelTest(TestCase):
    # CRUD tests for Route model
    pass


class FlightModelTest(TestCase):
    # CRUD tests for Flight model

    # Creation operation tests:
    @classmethod
    def setUpTestData(cls):
        parisRoute = Route.objects.create(
            flightCode='AF0443',
            airline='Air France',
            departureAirport='FLL',
            arrivalAirport='CDG',
            scheduledTime=datetime.time(10, 30, 0)
        )

        Flight.objects.create(
            route=parisRoute,
            scheduledDate=datetime.date(year=2022, month=11, day=26),
        )

        Flight.objects.create(
            route=parisRoute,
            scheduledDate=datetime.date(year=2022, month=11, day=29),
        )

        newYorkRoute = Route.objects.create(
            flightCode='LA8180',
            airline='Latam',
            departureAirport='JFK',
            arrivalAirport='FLL',
            scheduledTime=datetime.time(18, 10, 0)
        )

        Flight.objects.create(
            route=newYorkRoute,
            scheduledDate=datetime.date(year=2022, month=8, day=2),
        )

    # Reading operation tests:
    def testFlightRead(self):
        # Gets previsouly created Flight using the composite
        # primary key of (flightCode, scheduledDate)
        flightToParis = Flight.objects.get(
            route__flightCode="AF0443",
            scheduledDate=datetime.date(year=2022, month=11, day=26)
        )

        # Check if Flight data is correct
        self.assertEqual(flightToParis.scheduledDate,
                         datetime.date(year=2022, month=11, day=26))

    # Update operation tests:
    def testFlightUpdate(self):
        # Gets previously created Flight
        flightFromNY = Flight.objects.get(
            route__flightCode='LA8180',
            scheduledDate=datetime.date(year=2022, month=8, day=2)
        )

        # Updates Flight status
        flightFromNY.status = 'BOARDING'
        flightFromNY.save()

        # Checks if Flight has new status
        self.assertEqual(flightFromNY.status, 'BOARDING')

    # Delete operation tests:
    def testFlightDeletion(self):
        # Deletes previously created Flight
        Flight.objects.get(
            route__flightCode='AF0443',
            scheduledDate=datetime.date(year=2022, month=11, day=29),
        ).delete()

        # Looks for entries with the same atributes as the deleted Flight
        flightsToParisSet = Flight.objects.filter(
            route__flightCode='AF0443',
            scheduledDate=datetime.date(year=2022, month=11, day=29)
        )

        # Checks if there are no such Flights
        self.assertEqual(flightsToParisSet.count(), 0)
