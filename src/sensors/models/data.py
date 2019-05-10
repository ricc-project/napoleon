from django.db import models

from . import base


class SoilData(base.Data):
    moisture = models.FloatField()
    temperature = models.FloatField()


class AirData(base.Data):
    humidity = models.FloatField()
    temperature = models.FloatField()
    pressure = models.FloatField()


class WindData(base.Data):
    speed = models.FloatField()
    direction = models.PositiveIntegerField()


class RainData(base.Data):
    rainfall = models.PositiveIntegerField()


class SolarData(base.Data):
    radiation = models.PositiveIntegerField()


class ActuatorData(base.Data):
    status = models.BooleanField(default=False)
