# Generated by Django 4.2.1 on 2023-05-28 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galactic', '0002_planet_energy_level_planet_metal_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='energy_level',
            new_name='metal_mining_level',
        ),
        migrations.RenameField(
            model_name='planet',
            old_name='metal_level',
            new_name='solar_plant_level',
        ),
    ]