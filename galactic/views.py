import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Planet


# ================
# VIEWS
# ----------------


def index(request):
    """Main front-page."""

    # Construct a list of the latest 5 discovered planets
    latest_planet_list = Planet.objects.all()
    
    # Set the template for Django rendering
    template = loader.get_template('galactic/index.html')
    context = { 'latest_planet_list' : latest_planet_list }

    return HttpResponse(template.render(context, request))
  
    
def planet(request, planet_id):
    """Planet stats and geography."""
    
    try:
        planet = Planet.objects.get(pk=planet_id)
        
    except Planet.DoesNotExist:
        raise Http404("Planet does not exist")
    
    return render(request, 'galactic/planet.html', {'planet': planet})


def ressources(request, planet_id):
    """See and upgrade the current set of ressources (metal, energy, etc.)"""
    
    try:
        planet = Planet.objects.get(pk=planet_id)
        
    except Planet.DoesNotExist:
        raise Http404("Ressource does not exist")
    
    return render(request, 'galactic/ressources.html', {'planet': planet})


def facilities(request, planet_id):
    """See and upgrade the current set of facilities (robotics factory, shipyard dock, etc.)"""
    
    try:
        planet = Planet.objects.get(pk=planet_id)
        
    except Planet.DoesNotExist:
        raise Http404("Ressource does not exist")
    
    return render(request, 'galactic/facilities.html', {'planet': planet})


def defence(request, planet_id):
    """See and manufacture the current set of defence (rocket launcher, etc.)"""
    
    try:
        planet = Planet.objects.get(pk=planet_id)
        
    except Planet.DoesNotExist:
        raise Http404("Defence does not exist")
    
    return render(request, 'galactic/defence.html', {'planet': planet})


def shipyard(request, planet_id):
    """See and manufacture the current set of shipyard (light fighter, etc.)"""
    
    try:
        planet = Planet.objects.get(pk=planet_id)
        
    except Planet.DoesNotExist:
        raise Http404("Shipyard does not exist")
    
    return render(request, 'galactic/shipyard.html', {'planet': planet})


# ================
# FUNCTIONS
# ----------------



def upgrade_ressources(request, planet_id):

    # Set now
    now = timezone.now()

    # Get the Planet object
    planet = get_object_or_404(Planet, pk=planet_id)

    # Get the request from the form
    req = request.POST['button']

    # Check if upgrade in progress [ressources]
    if planet.metal_mining_next_upgrade or planet.solar_plant_next_upgrade:
        return render(request, 
                'galactic/ressources.html', 
                {'planet': planet, 'error_message': 'One upgrade is active'})

    
    # Initiate the upgrade or return a error message
    if req == "metal_mining":

        # Check ressource requirements are met
        if planet.metal >= planet.metal_mining_cost_upgrade_metal:

            # Set next upgrade time
            addition = datetime.timedelta(minutes=planet.metal_mining_upgrade_time)
            planet.metal_mining_next_upgrade = now + addition

        else:
            return render(request, 
                'galactic/ressources.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})

    elif req == "solar_plant":

        # Check ressource requirements are met
        if planet.metal >= planet.solar_plant_cost_upgrade_metal:

            # Set next upgrade time
            addition = datetime.timedelta(minutes=planet.solar_plant_upgrade_time)
            planet.solar_plant_next_upgrade = now + addition

        else:
            return render(request, 
                'galactic/ressources.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})

    
    else:
        return render(request, 
                'galactic/ressources.html', 
                {'planet': planet, 'error_message': 'Ressource not found'})

    # Save
    planet.save()
    
    # Return safely
    return HttpResponseRedirect(reverse('galactic:ressources', args=(planet.id,)))




def upgrade_facilities(request, planet_id):

    # Set now
    now = timezone.now()

    # Get the Planet object
    planet = get_object_or_404(Planet, pk=planet_id)

    # Get the request from the form
    req = request.POST['button']

    # Check if upgrade in progress [facilities]
    if planet.robotics_factory_next_upgrade or planet.shipyard_dock_next_upgrade:
        return render(request, 
                'galactic/facilities.html', 
                {'planet': planet, 'error_message': 'One upgrade is active'})

    
    # Initiate the upgrade or return a error message
    if req == "robotics_factory":

        # Check ressource requirements are met
        if planet.metal >= planet.robotics_factory_cost_upgrade_metal:

            # Set next upgrade time
            addition = datetime.timedelta(minutes=planet.robotics_factory_upgrade_time)
            planet.robotics_factory_next_upgrade = now + addition

        else:
            return render(request, 
                'galactic/facilities.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})


    if req == "shipyard_dock":

        # Check ressource requirements are met
        if planet.metal >= planet.shipyard_dock_cost_upgrade_metal:

            # Set next upgrade time
            addition = datetime.timedelta(minutes=planet.shipyard_dock_upgrade_time)
            planet.shipyard_dock_next_upgrade = now + addition

        else:
            return render(request, 
                'galactic/facilities.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})
    
    else:
        return render(request, 
                'galactic/facilities.html', 
                {'planet': planet, 'error_message': 'Ressource not found'})

    # Save
    planet.save()
    
    # Return safely
    return HttpResponseRedirect(reverse('galactic:facilities', args=(planet.id,)))


def manufacture_defence(request, planet_id):

    # Set now
    now = timezone.now()

    # Get the Planet object
    planet = get_object_or_404(Planet, pk=planet_id)

    # Get the request from the form
    req = request.POST['button']

    # Check if upgrade in progress [defence]
    if planet.rocket_launcher_next_manufacture or planet.light_laser_next_manufacture:
        return render(request, 
                'galactic/defence.html', 
                {'planet': planet, 'error_message': 'One upgrade is active'})

    
    # Set form variables
    amount = int(request.POST['amount'])

    if req == "rocket_launcher":

        # Check ressource requirements are met
        if planet.metal >= amount * planet.rocket_launcher_cost_manufacture_metal:

            # Remove ressource
            planet.metal -= amount * planet.rocket_launcher_cost_manufacture_metal

            # Set next upgrade time
            addition = datetime.timedelta(minutes=amount * planet.rocket_launcher_manufacture_time)
            planet.rocket_launcher_next_manufacture = now + addition

            # Set next amount
            planet.rocket_launcher_manufacture_amount = amount

        else:
            return render(request, 
                'galactic/defence.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})


    elif req == "light_laser":

        # Check ressource requirements are met
        if planet.metal >= amount * planet.light_laser_cost_manufacture_metal:

            # Remove ressource
            planet.metal -= amount * planet.light_laser_cost_manufacture_metal

            # Set next upgrade time
            addition = datetime.timedelta(minutes=amount * planet.light_laser_manufacture_time)
            planet.light_laser_next_manufacture = now + addition

            # Set next amount
            planet.light_laser_manufacture_amount = amount

        else:
            return render(request, 
                'galactic/defence.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})


    else:
        return render(request, 
                'galactic/defence.html', 
                {'planet': planet, 'error_message': 'Defence not found'})


    # Save
    planet.save()
    
    # Return safely
    return HttpResponseRedirect(reverse('galactic:defence', args=(planet.id,)))


def manufacture_shipyard(request, planet_id):

    # Set now
    now = timezone.now()

    # Get the Planet object
    planet = get_object_or_404(Planet, pk=planet_id)

    # Get the request from the form
    req = request.POST['button']

    # Check if upgrade in progress [shipyard]
    if planet.light_fighter_next_manufacture or planet.heavy_fighter_next_manufacture:
        return render(request, 
                'galactic/shipyard.html', 
                {'planet': planet, 'error_message': 'One upgrade is active'})

    
    # Set form variables
    amount = int(request.POST['amount'])

    if req == "light_fighter":

        # Check ressource requirements are met
        if planet.metal >= amount * planet.light_fighter_cost_manufacture_metal:

            # Remove ressource
            planet.metal -= amount * planet.light_fighter_cost_manufacture_metal

            # Set next upgrade time
            addition = datetime.timedelta(minutes=amount * planet.light_fighter_manufacture_time)
            planet.light_fighter_next_manufacture = now + addition

            # Set next amount
            planet.light_fighter_manufacture_amount = amount

        else:
            return render(request, 
                'galactic/shipyard.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})


    elif req == "heavy_fighter":

        # Check ressource requirements are met
        if planet.metal >= amount * planet.heavy_fighter_cost_manufacture_metal:

            # Remove ressource
            planet.metal -= amount * planet.heavy_fighter_cost_manufacture_metal

            # Set next upgrade time
            addition = datetime.timedelta(minutes=amount * planet.heavy_fighter_manufacture_time)
            planet.heavy_fighter_next_manufacture = now + addition

            # Set next amount
            planet.heavy_fighter_manufacture_amount = amount

        else:
            return render(request, 
                'galactic/shipyard.html', 
                {'planet': planet, 'error_message': 'Not enough ressources'})


    else:
        return render(request, 
                'galactic/shipyard.html', 
                {'planet': planet, 'error_message': 'Shipyard not found'})


    # Save
    planet.save()
    
    # Return safely
    return HttpResponseRedirect(reverse('galactic:shipyard', args=(planet.id,)))