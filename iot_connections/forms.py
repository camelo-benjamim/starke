from django import forms
from iot_connections.models import *
class FormIotDevice(forms.ModelForm):
    class Meta:
        model = IotDevice
        fields = ['device_name','direction_sense','module_sense','sense']
        labels = {'device_name':('Nome do dispositivo:  '),'direction_sense':('Senso de direção: '),'module_sense':('Senso de direção: '),'sense':('Senso de sentido: ')}
        
class FormSensor(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['iot_device','sensor_name','active','port_micro']
        labels = {'iot_device':('Dispositivo IOT:  '),'sensor_name':('Nome do sensor: '),'active':('Ativo: '),'port_micro':('Port Micro: ')}

class FormIotDevice(forms.ModelForm):
    class Meta:
        model = Actuator
        fields = ['iot_device_actuator','actuator_name','is_actuator_active','port_micro_actuator']
        labels = {'iot_device_actuator':('Dispositivo IOT:  '),'actuator_name':('Nome do atuador: '),'is_actuator_active':('O atuador está ativo: '),'port_micro_actuator':('Port Micro: ')}