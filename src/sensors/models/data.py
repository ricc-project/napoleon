from django.db import models
from .base import Data


class SoilData(Data):
    moisture = models.FloatField()
    temperature = models.FloatField()


class AirData(Data):
    humidity = models.FloatField()
    temperature = models.FloatField()
    pressure = models.FloatField()


class WindData(Data):
    speed = models.FloatField()
    direction = models.PositiveIntegerField()


class RainData(Data):
    rainfall = models.PositiveIntegerField()


class SolarData(Data):
    radiation = models.PositiveIntegerField()


class ActuatorData(Data):
    status = models.BooleanField(default=False)
