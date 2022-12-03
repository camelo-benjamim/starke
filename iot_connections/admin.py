from django.contrib import admin

from iot_connections.models import *
@admin.register(IotDevice)
class IotDeviceAdmin(admin.ModelAdmin):
    list_display = ['owner','device_name','device_key',]
    ##ordering = ('-id',)
    
    
    def has_add_permission(self, request, obj=None):
        return True
    def has_edit_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Sensor)

class SensorAdmin(admin.ModelAdmin):
    list_display = ['iot_device','active','port_micro',]
    ##ordering = ('-id',)
    
    def has_add_permission(self, request, obj=None):
        return True
    def has_edit_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(Actuator)
class ActuatorAdmin(admin.ModelAdmin):
    list_display = ['iot_device_actuator','actuator_name','port_micro_actuator',]
    ##ordering = ('-id',)
    
    
    def has_add_permission(self, request, obj=None):
        return True
    def has_edit_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(ActuatorOrganize)
class ActuatorOrganizeAdmin(admin.ModelAdmin):
    list_display = ['group_name',]
    ##ordering = ('-id',)
    
    
    def has_add_permission(self, request, obj=None):
        return True
    def has_edit_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True