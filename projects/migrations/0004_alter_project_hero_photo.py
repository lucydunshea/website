# Generated by Django 4.1 on 2024-02-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_hero_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='hero_photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]