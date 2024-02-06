from django.shortcuts import render
from google.transit import gtfs_realtime_pb2
import urllib.request
from .models import BusLocation
import json
import logging
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

logger = logging.getLogger(__name__)

def get_bus_locations():
    try:
        url = 'https://apis.metroinfo.co.nz/rti/gtfsrt/v1/vehicle-positions.pb'

        hdr = {
            # Request Headers
            'Cache-Control': 'no-cache',
                'Ocp-Apim-Subscription-Key': 'e08c855c857f497aa456af61a41789ee'
                }
    
        req = urllib.request.Request(url, headers=hdr)
        req.get_method = lambda:'GET'
        response = urllib.request.urlopen(req)
        gtfs_data = response.read()

        # Parse protocol buffers data
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(gtfs_data)

        # extract relevant data
        bus_locations = []
        for entity in feed.entity:
            if entity.HasField('vehicle') and entity.vehicle.HasField('position'):
                vehicle_info = entity.vehicle
                location = vehicle_info.position
                bus_locations.append({
                    'trip_id': entity.id,
                    'bus_id': vehicle_info.vehicle.id,
                    'lat': location.latitude,
                    'lon': location.longitude,
                    'start_time': vehicle_info.trip.start_time,
                    'start_date': vehicle_info.trip.start_date,
                    'route_id': vehicle_info.trip.route_id,
                    'status': vehicle_info.current_status,
                    'timestamp': vehicle_info.timestamp,
                    'stop_id': vehicle_info.stop_id

                })
        return bus_locations
    
    except urllib.error.URLError as e:
        logger.error(f"Error during HTTP request: {e}")
        return None
    except urllib.error.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None


def index(request):
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    bus_locations_json = json_serializer.serialize(BusLocation.objects.all())
    return render(request, 'map/index.html', {"bus_locations_json": bus_locations_json})
    
