# Generated by Django 4.1 on 2024-02-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_buslocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buslocation',
            name='start_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='buslocation',
            name='timestamp',
            field=models.CharField(max_length=50),
        ),
    ]