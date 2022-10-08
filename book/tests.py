from django.test import TestCase
import datetime

# Test Models
from book.models import Route, Flight


class RouteModelTest(TestCase):
    # CRUD tests for Route model

    # Creation operation tests:
    @classmethod
    def setUpTestData(cls):
        Route.objects.create(
            flightCode='AF443',
            airline='Air France',
            departureAirport='FLL',
            arrivalAirport='CDG',
            scheduledTime=datetime.time(10, 30, 0)
        )

        Route.objects.create(
            flightCode='LH507',
            airline='Lufthansa',
            departureAirport='FRA',
            arrivalAirport='FLL',
            scheduledTime=datetime.time(22, 40, 0)
        )

    # Reading operation tests:
    def testRouteRead(self):
        # Gets previsouly created Route using the flightCode primary key
        parisRoute = Route.objects.get(flightCode="AF443")

        # Check if Route data is correct
        self.assertEqual(parisRoute.airline, 'Air France')
        self.assertEqual(parisRoute.departureAirport, 'FLL')
        self.assertEqual(parisRoute.arrivalAirport, 'CDG')
        self.assertEqual(parisRoute.scheduledTime, datetime.time(10, 30, 0))

    # Update operation tests:
    def testRouteUpdate(self):
        # Gets previously created Route
        frankfurtRoute = Route.objects.get(flightCode='LH507')

        # Updates Route's scheduled time
        frankfurtRoute.scheduledTime = datetime.time(21, 20, 0)
        frankfurtRoute.save()

        # Checks if Route has a new scheduled time
        self.assertEqual(frankfurtRoute.scheduledTime,
                         datetime.time(21, 20, 0))

    # Delete operation tests:
    def testRouteDeletion(self):
        # Deletes previously created Route
        Route.objects.get(flightCode='AF443').delete()

        # Looks for entries with the same atributes as the deleted Route
        parisRouteSet = Route.objects.filter(flightCode='AF443')

        # Checks if there are no such Routes
        self.assertEqual(parisRouteSet.count(), 0)


class FlightModelTest(TestCase):
    # CRUD tests for Flight model

    # Creation operation tests:
    @classmethod
    def setUpTestData(cls):
        parisRoute = Route.objects.create(
            flightCode='AF443',
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
            route__flightCode="AF443",
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
            route__flightCode='AF443',
            scheduledDate=datetime.date(year=2022, month=11, day=29),
        ).delete()

        # Looks for entries with the same atributes as the deleted Flight
        flightsToParisSet = Flight.objects.filter(
            route__flightCode='AF443',
            scheduledDate=datetime.date(year=2022, month=11, day=29)
        )

        # Checks if there are no such Flights
        self.assertEqual(flightsToParisSet.count(), 0)
