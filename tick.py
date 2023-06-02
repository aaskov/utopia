#!/usr/bin/env python
"""Tick tock

Use this script in order to make the world run. Use the following command in
order to make the world tick.

$ python3 manage.py shell < tick.py

"""
import datetime
from django.utils import timezone
from galactic.models import Planet


# Set time
now = timezone.now()



# =================
# BATCH
# -----------------

# For the Metal Mining ressource
planets = Planet.objects.filter(metal_mining_next_batch__lte=now)
for p in planets:
	# Increase the metal balance
	p.metal += p.metal_mining_production

	# Set next batch time
	p.metal_mining_next_batch = now + datetime.timedelta(hours=1)

	# Save
	p.save()




# =================
# RESSOURCES
# -----------------

# For the Metal Mining ressource
planets = Planet.objects.filter(metal_mining_next_upgrade__isnull=False)
for p in planets:
	# Increase level
	p.metal_mining_level += 1

	# Subtract upgrade cost
	p.metal -= p.metal_mining_cost_upgrade_metal

	# Increase next production measure
	p.metal_mining_production = p.metal_mining_level ** 2

	# Remove next upgrade time
	p.metal_mining_next_upgrade = None

	# Save
	p.save()


# For the Solar Plant ressource
planets = Planet.objects.filter(solar_plant_next_upgrade__isnull=False)
for p in planets:
	# Increase level
	p.solar_plant_level += 1

	# Subtract upgrade cost
	p.metal -= p.solar_plant_cost_upgrade_metal

	# Increase next production measure
	p.solar_plant_production = p.solar_plant_level ** 2

	# Remove next upgrade time
	p.solar_plant_next_upgrade = None

	# Save
	p.save()



# =================
# FACILITY
# -----------------

# For the Robotics Factory
planets = Planet.objects.filter(robotics_factory_next_upgrade__isnull=False)
for p in planets:
	# Increase level
	p.robotics_factory_level += 1

	# Subtract upgrade cost
	p.metal -= p.metal_mining_cost_upgrade_metal

	# Remove next upgrade time
	p.robotics_factory_next_upgrade = None

	# Save
	p.save()


# For the Shipyard Dock
planets = Planet.objects.filter(shipyard_dock_next_upgrade__isnull=False)
for p in planets:
	# Increase level
	p.shipyard_dock_level += 1

	# Subtract upgrade cost
	p.metal -= p.solar_plant_cost_upgrade_metal

	# Remove next upgrade time
	p.shipyard_dock_next_upgrade = None

	# Save
	p.save()




# =================
# DEFENCE
# -----------------

# For the Rocket Launcher
planets = Planet.objects.filter(rocket_launcher_next_manufacture__lte=now)
for p in planets:

	# Add to count
	p.rocket_launcher_count += p.rocket_launcher_manufacture_amount

	# Remove next upgrade time
	p.rocket_launcher_next_manufacture = None

	# Remove next amount
	p.rocket_launcher_manufacture_amount = 0

	# Save
	p.save()



# For the Light laser
planets = Planet.objects.filter(light_laser_next_manufacture__lte=now)
for p in planets:

	# Add to count
	p.light_laser_count += p.light_laser_manufacture_amount

	# Remove next upgrade time
	p.light_laser_next_manufacture = None

	# Remove next amount
	p.light_laser_manufacture_amount = 0

	# Save
	p.save()



# =================
# SHIPYARD
# -----------------

# For the Rocket Launcher
planets = Planet.objects.filter(light_fighter_next_manufacture__lte=now)
for p in planets:

	# Add to count
	p.light_fighter_count += p.light_fighter_manufacture_amount

	# Remove next upgrade time
	p.light_fighter_next_manufacture = None

	# Remove next amount
	p.light_fighter_manufacture_amount = 0

	# Save
	p.save()



# For the Light laser
planets = Planet.objects.filter(heavy_fighter_next_manufacture__lte=now)
for p in planets:

	# Add to count
	p.heavy_fighter_count += p.heavy_fighter_manufacture_amount

	# Remove next upgrade time
	p.heavy_fighter_next_manufacture = None

	# Remove next amount
	p.heavy_fighter_manufacture_amount = 0

	# Save
	p.save()