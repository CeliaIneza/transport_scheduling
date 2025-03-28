from django.urls import path
from .views import (
    vehicle_list, add_vehicle, edit_vehicle, delete_vehicle,
    driver_list, add_driver, edit_driver, delete_driver,
    route_list, add_route, edit_route, delete_route,
    schedule_list, add_schedule, edit_schedule, delete_schedule,dashboard, vehicle_data,predict_journey_duration
)
app_name= 'transport'
urlpatterns = [
    #dashboard
    path('dashboard/', dashboard, name='dashboard'),
    # Vehicle URLs
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('vehicles/add/', add_vehicle, name='add_vehicle'),
    path('vehicles/edit/<int:vehicle_id>/', edit_vehicle, name='edit_vehicle'),
    path('vehicles/delete/<int:vehicle_id>/', delete_vehicle, name='delete_vehicle'),
    path('vehicles/vehicle_data',vehicle_data, name='vehicle_data'),
    
    # Driver URLs
    path('drivers/', driver_list, name='driver_list'),
    path('drivers/add/', add_driver, name='add_driver'),
    path('drivers/edit/<int:driver_id>/', edit_driver, name='edit_driver'),
    path('drivers/delete/<int:driver_id>/', delete_driver, name='delete_driver'),
    
    # Route URLs
    path('routes/', route_list, name='route_list'),
    path('routes/add/', add_route, name='add_route'),
    path('routes/edit/<int:route_id>/', edit_route, name='edit_route'),
    path('routes/delete/<int:route_id>/', delete_route, name='delete_route'),

    # Schedule URLs
    path('schedules/', schedule_list, name='schedule_list'),
    path('schedules/add/', add_schedule, name='add_schedule'),
    path('schedules/edit/<int:schedule_id>/', edit_schedule, name='edit_schedule'),
    path('schedules/delete/<int:schedule_id>/', delete_schedule, name='delete_schedule'),

    #model predictions
    path('predict/', predict_journey_duration, name='predict'),
]
