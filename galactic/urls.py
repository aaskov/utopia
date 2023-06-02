from django.urls import path

from . import views

app_name = 'galactic'
urlpatterns = [

    # Ex: '/galactic/'
    path('', views.index, name='index'),
    
    # Ex: '/galactic/5/'
    path('<int:planet_id>/', views.planet, name='planet'),
    
    # Ex: '/galactic/5/ressources/'
    path('<int:planet_id>/ressources/', views.ressources, name='ressources'),
    
    # (Post for upgrade metal mining)
    path('<int:planet_id>/upgrade_ressources/', views.upgrade_ressources, name='upgrade_ressources'),
    
    # Ex '/galactic/5/facilities'
    path('<int:planet_id>/facilities/', views.facilities, name='facilities'),

    # (Post for upgrade robotics factory)
    path('<int:planet_id>/upgrade_facilities/', views.upgrade_facilities, name='upgrade_facilities'),

    # Ex '/galactic/5/defence'
    path('<int:planet_id>/defence/', views.defence, name='defence'),

    # (Post for manufacture rocket launcher)
    path('<int:planet_id>/manufacture_defence/', views.manufacture_defence, name='manufacture_defence'),

    # Ex '/galactic/5/shipyard'
    path('<int:planet_id>/shipyard/', views.shipyard, name='shipyard'),

    # (Post for manufacture light fighter)
    path('<int:planet_id>/manufacture_shipyard/', views.manufacture_shipyard, name='manufacture_shipyard'),

]
