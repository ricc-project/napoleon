from django.db import models
from boogie.rest import rest_api
from ..manager import UserManager
from .data import *

@rest_api(exclude=['hash','auth_token'])
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    hash = models.CharField(max_length=128)
    auth_token = models.CharField(max_length=64)
    objects = UserManager()

@rest_api()
class DataCluster(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="data")
    collected_at = models.DateTimeField(auto_now=True)
    
    @property
    def rain_datas(self):
        return RainData.objects.filter(data_cluster=self)
    @property
    def wind_datas(self):
        return WindData.objects.filter(data_cluster=self)
    @property
    def solar_datas(self):
        return SolarData.objects.filter(data_cluster=self)
    @property
    def soil_datas(self):
        return SoilData.objects.filter(data_cluster=self)
    @property
    def air_datas(self):
        return AirData.objects.filter(data_cluster=self)
    @property
    def actuator_datas(self):
        return ActuatorData.objects.filter(data_cluster=self)

