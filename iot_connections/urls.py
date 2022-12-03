from django.urls import path
from iot_connections.views import *

urlpatterns = [
    path('',mainFrame),
    path('show_iot_devices',showIotDevices),
    path('add_iot_device/',addIotDevice),
    path('edit_iot_device/<str:device_key>',editIotDevice),
    path('delete_iot_device/<str:device_key>',deleteIotDevice),
    path('device_control/<str:device_key>',deviceControl),
    path('manual_control/<str:device_key>',manualControl),
    path('btn_action/<str:btn_key>/<str:device_key>/',btnAction),
    path('micro_communication/<str:device_key>',microCommunication),
   
]
