from django.db import models
from django.contrib.gis.db import models as geomodels

class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'cities'

class BusLocation(models.Model):
    trip_id = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    route_id = models.CharField(max_length=50)
    location = geomodels.PointField()
    status = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
    stop_id = models.CharField(max_length=50)
    bus_id = models.CharField(max_length=50)
        
    def __str__(self):
        return f"Bus {self.bus_id} - ({self.location.x}, {self.location.y})"