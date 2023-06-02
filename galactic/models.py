from django.db import models
from django.utils import timezone

# Create your models here.
class Planet(models.Model):
    
    # =============
    # GEOGRAPHY
    # This section describes the planet geography and related stuff
    # -------------
    discovered_date = models.DateTimeField('date discovered')
    
    # =============
    # DEPOT
    # This section contains the current ressources available on the planet
    # -------------
    energy = models.IntegerField(default=100)
    metal = models.IntegerField(default=30)
    
    
    # =============
    # RESSOURCES
    # This section contains the ressources
    # -------------
    
    # -------------
    # Solar Plant
    # .............
    solar_plant_level = models.IntegerField(default=1)
    solar_plant_production = models.IntegerField(default=10)
    solar_plant_next_upgrade = models.DateTimeField(null=True, blank=True)
    solar_plant_cost_upgrade_metal = models.IntegerField(default=10)
    solar_plant_upgrade_time = models.IntegerField(default=10)


    # -------------
    # Metal Mining
    # .............
    metal_mining_level = models.IntegerField(default=1)
    metal_mining_production = models.IntegerField(default=10)
    metal_mining_next_batch = models.DateTimeField(default=timezone.now())
    metal_mining_energy_consumption = models.IntegerField(default=10)
    metal_mining_next_upgrade = models.DateTimeField(null=True, blank=True)
    metal_mining_cost_upgrade_metal = models.IntegerField(default=10)
    metal_mining_upgrade_time = models.IntegerField(default=10)



    # =============
    # FACILITIES
    # This section contains the facilities
    # -------------
    
    # -------------
    # Robotics Factory
    # .............
    robotics_factory_level = models.IntegerField(default=1)
    robotics_factory_next_upgrade = models.DateTimeField(null=True, blank=True)
    robotics_factory_cost_upgrade_metal = models.IntegerField(default=10)
    robotics_factory_upgrade_time = models.IntegerField(default=10)


    # -------------
    # Shipyard Dock
    # .............
    shipyard_dock_level = models.IntegerField(default=1)
    shipyard_dock_next_upgrade = models.DateTimeField(null=True, blank=True)
    shipyard_dock_cost_upgrade_metal = models.IntegerField(default=10)
    shipyard_dock_upgrade_time = models.IntegerField(default=10)



    # =============
    # DEFENCE
    # This section contains the defence items
    # -------------

    # -------------
    # Rocket Launcher
    # .............
    rocket_launcher_count = models.IntegerField(default=1)
    rocket_launcher_next_manufacture = models.DateTimeField(null=True, blank=True)
    rocket_launcher_cost_manufacture_metal = models.IntegerField(default=1000)
    rocket_launcher_manufacture_time = models.IntegerField(default=10)
    rocket_launcher_manufacture_amount = models.IntegerField(default=1)



    # -------------
    # Light Laser
    # .............
    light_laser_count = models.IntegerField(default=1)
    light_laser_next_manufacture = models.DateTimeField(null=True, blank=True)
    light_laser_cost_manufacture_metal = models.IntegerField(default=1000)
    light_laser_manufacture_time = models.IntegerField(default=10)
    light_laser_manufacture_amount = models.IntegerField(default=1)



    # =============
    # Shipyard
    # This section contains the shipyard items
    # -------------


    # -------------
    # Light Fighter
    # .............
    light_fighter_count = models.IntegerField(default=1)
    light_fighter_next_manufacture = models.DateTimeField(null=True, blank=True)
    light_fighter_cost_manufacture_metal = models.IntegerField(default=1000)
    light_fighter_manufacture_time = models.IntegerField(default=10)
    light_fighter_manufacture_amount = models.IntegerField(default=1)



    # -------------
    # Heavy Fighter
    # .............
    heavy_fighter_count = models.IntegerField(default=1)
    heavy_fighter_next_manufacture = models.DateTimeField(null=True, blank=True)
    heavy_fighter_cost_manufacture_metal = models.IntegerField(default=1000)
    heavy_fighter_manufacture_time = models.IntegerField(default=10)
    heavy_fighter_manufacture_amount = models.IntegerField(default=1)





    
    # =============
    
    def __str__(self):
        return "Planet discovered on " + str(self.discovered_date)
