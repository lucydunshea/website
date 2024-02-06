# Generated by Django 4.1 on 2024-02-06 02:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('date', models.CharField(max_length=50)),
                ('route_id', models.CharField(max_length=50)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('status', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('stop_id', models.CharField(max_length=50)),
                ('bus_id', models.CharField(max_length=50)),
            ],
        ),
    ]