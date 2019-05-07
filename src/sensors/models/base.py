from django.db import models
from polymorphic.models import PolymorphicModel


class Sensor(PolymorphicModel):

    def data(self):
        pass

    def collect(self, data):
        pass


class Data(PolymorphicModel):
    collected_at = models.DateTimeField(auto_now=True)
