from django.contrib.auth.models import User

from rest_framework import serializers

from .models import data, base


class SoilDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data.SoilData
        fields= '__all__'


class AirDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data.AirData
        fields= '__all__'


class WindDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data.WindData
        fields= '__all__'


class RainDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data.RainData
        fields= '__all__'


class SolarDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data.SolarData
        fields= '__all__'


class ActuatorDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data.ActuatorData
        fields= '__all__'


class DataClusterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = base.DataCluster
        fields= '__all__'
