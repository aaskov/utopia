# Generated by Django 4.2.1 on 2023-05-30 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galactic', '0004_planet_metal_mining_production_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='metal_mining_next_batch',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 17, 59, 16, 507577, tzinfo=datetime.timezone.utc)),
        ),
    ]