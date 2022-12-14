from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from iot_connections.models import *
from django.http import JsonResponse
import json
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
    if request.user.is_authenticated == True:
        return redirect ('/show_iot_devices')
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

def addRoutiine(request):
    pass
def editRoutine(request,device_key,routine):
    pass
def deleteRoutine(request,device_key,routine):
    pass
@login_required
def deviceControl(request,device_key):
    try:
        device = get_object_or_404(IotDevice,device_key=device_key)
        context = {
            'device': device,
        }
    except:
        pass
    return render(request,'iot_connection/device_control.html',context=context)
##controle manual
def manualControl(request,device_key):
        iot_device_actuator = get_object_or_404(IotDevice,device_key=device_key)
        device_groups = ActuatorOrganize.objects.filter(device=iot_device_actuator)
        actuators = Actuator.objects.filter(iot_device_actuator=iot_device_actuator)
        context = {
            'device_groups': device_groups,
            'actuators': actuators,
            'device_key': device_key,
        }
        return render(request,"iot_connection/manual_control.html",context=context)    

def btnAction(request,btn_key, device_key):
    device = get_object_or_404(IotDevice,device_key=device_key)
    actuator = get_object_or_404(Actuator,actuator_name=btn_key,iot_device_actuator=device)
    if actuator.is_actuator_active == True:
        actuator.is_actuator_active = False
    else:
        actuator.is_actuator_active = True
    
    actuator.save()

    return redirect('/manual_control/'+ str(device_key))
##controle autom??tico
def automaticControl(request,device_key):
    pass
def automaticRoutineExecution(request,device_key,routine):
    pass
def microCommunication(request,device_key):
    if request.method == "GET":
        iot_device = get_object_or_404(IotDevice,device_key=device_key)
        atuadores = Actuator.objects.filter(iot_device_actuator=iot_device)
        dictionary = {}
        indent = len(atuadores)
        for i in atuadores:
            dictionary.update({i.port_micro_actuator : i.is_actuator_active})
        jsonFile = json.dumps(dictionary,indent=indent-1)
        print(jsonFile)
        return JsonResponse(jsonFile,safe=False)


