# Generated by Django 3.2.16 on 2022-12-03 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
import iot_connections.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actuator_name', models.CharField(max_length=50)),
                ('is_actuator_active', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('port_micro_actuator', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='IotDevice',
            fields=[
                ('device_name', models.CharField(max_length=30)),
                ('sense', models.BooleanField(default=True)),
                ('device_key', models.CharField(default=iot_connections.models.IotDevice.devicegen, max_length=12, primary_key=True, serialize=False)),
                ('owner', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users_may_access', models.ManyToManyField(blank=True, default=None, null=True, related_name='users_may_access', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('port_micro', models.CharField(max_length=2)),
                ('iot_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_connections.iotdevice')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routine_name', models.CharField(max_length=32)),
                ('routine_description', models.TextField()),
                ('device_routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_connections.iotdevice')),
            ],
        ),
        migrations.CreateModel(
            name='ActuatorOrganize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
                ('actuators', models.ManyToManyField(related_name='actuators_name', to='iot_connections.Actuator')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_connections.iotdevice')),
            ],
        ),
        migrations.AddField(
            model_name='actuator',
            name='iot_device_actuator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_connections.iotdevice'),
        ),
    ]
