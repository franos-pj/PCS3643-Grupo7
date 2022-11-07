from django.contrib.auth import get_user_model
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission
import django.contrib.auth.validators
from monitoring.models import Route, Flight
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command


def migrationScripts(apps, schema_editor):
    createPermissions(apps, schema_editor)
    createGroups(apps, schema_editor)
    createUsers(apps, schema_editor)


def createPermissions(apps, schema_editor):

    # Workaround so permissions get set during migration
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None


def createGroups(apps, schema_editor):

    # Gets all Route permissions
    routeContentType = ContentType.objects.get_for_model(Route)
    routePermission = Permission.objects.filter(content_type=routeContentType)

    # Gets Flight permissions separately, se we can selectively attribute them
    flightContentType = ContentType.objects.get_for_model(Flight)
    addFlightPermission = Permission.objects.get(
        codename='add_flight',
        content_type=flightContentType,
    )
    viewFlightPermission = Permission.objects.get(
        codename='view_flight',
        content_type=flightContentType,
    )
    changeFlightPermission = Permission.objects.get(
        codename='change_flight',
        content_type=flightContentType,
    )
    deleteFlightPermission = Permission.objects.get(
        codename='delete_flight',
        content_type=flightContentType,
    )
    changeFlightStatusPilotPerm = Permission.objects.get(
        codename='can_change_status_as_pilot_flight',
        content_type=flightContentType,
    )
    changeFlightStatusAirlinePerm = Permission.objects.get(
        codename='can_change_status_as_airline_flight',
        content_type=flightContentType,
    )
    changeFlightStatusTowerPerm = Permission.objects.get(
        codename='can_change_status_as_tower_flight',
        content_type=flightContentType,
    )
    changeFlightRealDatePerm = Permission.objects.get(
        codename='can_change_real_date_flight',
        content_type=flightContentType,
    )
    changeFlightRealTimePerm = Permission.objects.get(
        codename='can_change_real_time_flight',
        content_type=flightContentType,
    )
    changeFlightScheduledDatePerm = Permission.objects.get(
        codename='can_change_scheduled_date_flight',
        content_type=flightContentType,
    )

    # Creates authentation groups for every type of user
    pilotGroup = Group.objects.get_or_create(name="Pilots")[0]
    towerGroup = Group.objects.get_or_create(name="ControlTower")[0]
    airlineGroup = Group.objects.get_or_create(name="Airlines")[0]
    operatorGroup = Group.objects.get_or_create(name="Operators")[0]

    # Gives Route and Flight CRUD permission for operators
    for perm in routePermission:
        operatorGroup.permissions.add(perm)
    for flightDefaultPerm in [addFlightPermission, viewFlightPermission,
                              changeFlightPermission, deleteFlightPermission]:
        operatorGroup.permissions.add(flightDefaultPerm)

    # Gives Flight Read and Update permissions for pilots, airlines, tower
    for perm in [viewFlightPermission, changeFlightPermission]:
        pilotGroup.permissions.add(perm)
        towerGroup.permissions.add(perm)
        airlineGroup.permissions.add(perm)

    # Extra permissions for pilot group
    pilotGroup.permissions.add(changeFlightStatusPilotPerm)
    pilotGroup.permissions.add(changeFlightRealDatePerm)
    pilotGroup.permissions.add(changeFlightRealTimePerm)

    # Extra permissions for airlines, control tower, operators groups
    airlineGroup.permissions.add(changeFlightStatusAirlinePerm)
    towerGroup.permissions.add(changeFlightStatusTowerPerm)
    operatorGroup.permissions.add(changeFlightScheduledDatePerm)


def createUsers(apps, schema_editor):
    mockUsers = [
        {"username": "francisco.mariani", "password": "SR71"},
        {"username": "lucas.palmiro", "password": "A380"},
        {"username": "lucas.garcia", "password": "B52"},
        {"username": "michelet.chavez", "password": "PCS3643"},
        {"username": "kechi.hirama", "password": "PCS3643"}
    ]

    pilotGroup = Group.objects.get_or_create(name="Pilots")[0]
    towerGroup = Group.objects.get_or_create(name="ControlTower")[0]
    airlineGroup = Group.objects.get_or_create(name="Airlines")[0]
    operatorGroup = Group.objects.get_or_create(name="Operators")[0]
    managerGroup = Group.objects.get_or_create(name="Managers")[0]

    User = get_user_model()

    pilot = User.objects.create_user(
        username=mockUsers[0]["username"], password=mockUsers[0]["password"])
    pilot.groups.add(pilotGroup)

    tower = User.objects.create_user(
        username=mockUsers[1]["username"], password=mockUsers[1]["password"])
    tower.groups.add(towerGroup)

    airline = User.objects.create_user(
        username=mockUsers[2]["username"], password=mockUsers[2]["password"])
    airline.groups.add(airlineGroup)

    operator = User.objects.create_user(
        username=mockUsers[3]["username"], password=mockUsers[3]["password"])
    operator.groups.add(operatorGroup)

    manager = User.objects.create_user(
        username=mockUsers[4]["username"], password=mockUsers[4]["password"])
    manager.groups.add(managerGroup)


def loadInitialRoutes(apps, schema_editor):
    call_command("loaddata", "routes.json")


def loadInitialFlights(apps, schema_editor):
    call_command("loaddata", "flights.json")
