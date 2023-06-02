# Generated by Django 4.2.1 on 2023-06-02 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galactic', '0009_planet_light_laser_cost_manufacture_metal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='heavy_fighter_cost_manufacture_metal',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='planet',
            name='heavy_fighter_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='planet',
            name='heavy_fighter_manufacture_amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='planet',
            name='heavy_fighter_manufacture_time',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='planet',
            name='heavy_fighter_next_manufacture',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planet',
            name='light_fighter_cost_manufacture_metal',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='planet',
            name='light_fighter_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='planet',
            name='light_fighter_manufacture_amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='planet',
            name='light_fighter_manufacture_time',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='planet',
            name='light_fighter_next_manufacture',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='metal_mining_next_batch',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 19, 53, 46, 797223, tzinfo=datetime.timezone.utc)),
        ),
    ]
