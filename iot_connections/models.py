from django.db import models
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from accounts.models import Account

# As model field:
from django_currentuser.db.models import CurrentUserField
# Create your models here.
from random import *
import string
class IotDevice(models.Model):
    owner = CurrentUserField()
    users_may_access = models.ManyToManyField(Account,related_name="users_may_access")
    device_name = models.CharField(max_length=30)
    direction_sense = models.BooleanField(default=True),
    module_sense = models.BooleanField(default=True),
    sense = models.BooleanField(default=True)
    def devicegen():
        alphabet = string.ascii_letters + string.digits
        pseudorandomic_string = ''
        for i in range(10):
            randomic_number = randint(0,len(alphabet) - 1)
            pseudorandomic_string += alphabet[randomic_number]
        return pseudorandomic_string
    device_key = models.CharField(max_length=12, primary_key=True, default=devicegen)

    def __str__(self):
        return self.device_name

class Sensor(models.Model):
    iot_device = models.ForeignKey(IotDevice,on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    port_micro = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.sensor_name

class Actuator(models.Model):
    iot_device_actuator = models.ForeignKey(IotDevice,on_delete=models.CASCADE)
    actuator_name = models.CharField(max_length=50)
    is_actuator_active = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    port_micro_actuator = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.actuator_name


##SCRIPT/ROTINA
class Routine(models.Model):
    routine_name = models.CharField(max_length=32)
    routine_description = models.TextField()
    device_routine = models.ForeignKey(IotDevice,on_delete=models.CASCADE)
    

