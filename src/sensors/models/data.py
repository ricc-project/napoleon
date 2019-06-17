from django.db import models
from boogie.rest import rest_api

from . import base

@rest_api()
class SoilData(base.Data):
    moisture1 = models.FloatField()
    moisture2 = models.FloatField()
    moisture3 = models.FloatField()
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


json_names = {
    "soil": {
        "model":SoilData,
        "fields":["moisture1","moisture2","moisture3", "temperature"]
    },
    "air":  {
        "model":AirData,
        "fields":["humidity", "temperature", "pressure"]
    },
    "wind":  {
        "model":WindData,
        "fields":["speed", "direction"]
    },
    "rain":  {
        "model":RainData,
        "fields":["rainfall"]
    },
    "solar":  {
        "model":SolarData,
        "fields":["radiation"]
    },
    "actuator":  {
        "model":ActuatorData,
        "fields":["status"]
    }
}
