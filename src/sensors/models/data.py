from django.db import models
from boogie.rest import rest_api

from . import base

@rest_api()
class SoilData(base.Data):
    moisture = models.FloatField()
    temperature = models.FloatField()

@rest_api()
class AirData(base.Data):
    humidity = models.FloatField()
    temperature = models.FloatField()
    pressure = models.FloatField()

@rest_api()
class WindData(base.Data):
    speed = models.FloatField()
    direction = models.PositiveIntegerField()

@rest_api()
class RainData(base.Data):
    rainfall = models.PositiveIntegerField()

@rest_api()
class SolarData(base.Data):
    radiation = models.PositiveIntegerField()

@rest_api()
class ActuatorData(base.Data):
    status = models.BooleanField(default=False)
