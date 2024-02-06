from django_cron import CronJobBase, Schedule
from map.views import get_bus_locations
from map.models import BusLocation
from django.contrib.gis.geos import Point

class UpdateBusLocationsJob(CronJobBase):
    RUN_EVERY_MINS = 5  # adjust the frequency as needed

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'map.update_bus_locations_job'

    def do(self):
        bus_locations = get_bus_locations()

        for location in bus_locations:
            # Save bus locations to the database
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