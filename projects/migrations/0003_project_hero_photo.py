# Generated by Django 4.1 on 2024-02-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hero_photo',
            field=models.ImageField(default='image.png', upload_to=''),
            preserve_default=False,
        ),
    ]
