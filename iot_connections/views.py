from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from iot_connections.models import *
# Create your views here.
@login_required
def showIotDevices(request):
    user = request.user
    third_devices = IotDevice.objects.filter(users_may_access=user)
    my_devices = IotDevice.objects.filter(owner=user)
    context = {
        'third_devices': third_devices,
        'my_devices': my_devices,
    }
    return render(request,'iot_connection/index.html',context=context)
def mainFrame(request):
    return render(request,'index.html')
def addIotDevice(request):
    pass
def editIotDevice(request,device):
    pass
def deleteIotDevice(request,device):
    pass
def addSensor(request):
    pass
def editSensor(request,sensor):
    pass
def removeSensor(request,sensor):
    pass

def addActuator(request):
    pass
def editActuator(request,actuator):
    pass
def deleteActuator(request,actuator):
    pass
def deviceControl(request,device_key):
    print(device_key)
##controle manual
def manualControl(request,device_key):
    return render(request,"iot_connection/manual_control.html")
##controle automático

def microCommunication(request,device_code):
    pass

def showCodePastMicro(request,device_code):
    pass