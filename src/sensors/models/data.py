from django.db import models
from boogie.rest import rest_api

# from .base import DataCluster

class Data(models.Model):
    data_cluster = models.ForeignKey('sensors.DataCluster', on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True

@rest_api()
class SoilData(Data):
    moisture1 = models.FloatField()
    moisture2 = models.FloatField()
    moisture3 = models.FloatField()
    temperature = models.FloatField()

@rest_api()
class AirData(Data):
    humidity = models.FloatField()
    temperature = models.FloatField()
    pressure = models.FloatField()

@rest_api()
class WindData(Data):
    speed = models.FloatField()
    direction = models.PositiveIntegerField()

@rest_api()
class RainData(Data):
    rainfall = models.PositiveIntegerField()

@rest_api()
class SolarData(Data):
    radiation = models.PositiveIntegerField()

@rest_api()
class ActuatorData(Data):
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

classes = {
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