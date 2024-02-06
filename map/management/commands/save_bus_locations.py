from map.views import get_bus_locations
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from map.models import BusLocation


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Your logic for obtaining bus locations (e.g., from API) goes here
        bus_locations = get_bus_locations()

        # # Save bus locations to the database
        # self.save_bus_locations(bus_locations0
        for location in bus_locations:
            BusLocation.objects.create(
                trip_id=location['trip_id'],
                start_time=location['start_time'],
                date=location['start_date'],
                route_id=location['route_id'],
                location=Point(location['lon'], location['lat']),
                status=location['status'],
                timestamp=location['timestamp'],
                stop_id=location['stop_id'],
                bus_id=location['bus_id']
            )
        self.stdout.write(self.style.SUCCESS('Bus locations saved successfully.'))