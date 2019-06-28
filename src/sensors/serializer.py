from rest_framework import serializers
from collections import OrderedDict
from rest_framework.serializers import ModelSerializer
from .models import json_names, classes
def serializer_factory(mdl, fields=None, **kwargss):
    """ Generalized serializer factory to increase DRYness of code.

    :param mdl: The model class that should be instanciated
    :param fields: the fields that should be exclusively present on the serializer
    :param kwargss: optional additional field specifications
    :return: An awesome serializer
    """
    class MySerializer(ModelSerializer):
        class Meta:
            model = mdl

        if fields:
            setattr(Meta, "fields", fields)

    return MySerializer

def create_serializer(model_json_name):
    myserializer = serializer_factory(
        json_names[model_json_name]['model'],fields=json_names[model_json_name]['fields'],
    )
    return myserializer

def create_serializer_by_class(class_name):
    myserializer = serializer_factory(
        classes[class_name]['class'], fields=classes[class_name]['fields'],
    )
    return myserializer

class SensorDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(max_value=None, min_value=0)
    amount = serializers.IntegerField(max_value=None, min_value=1)


class DataClusterSerializer(serializers.Serializer):
    rain_datas = create_serializer("rain")(many=True)
    soil_datas = create_serializer("soil")(many=True)
    solar_datas = create_serializer("solar")(many=True)
    wind_datas = create_serializer("wind")(many=True)
    actuator_datas = create_serializer("actuator")(many=True)
    air_datas = create_serializer("air")(many=True)




