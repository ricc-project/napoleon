from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User

from boogie.rest import rest_api


class DataCluster(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    collected_at = models.DateTimeField(auto_now=True)
    

class Data(models.Model):
    data_cluster = models.ForeignKey(DataCluster, on_delete=models.CASCADE)

    class Meta:
        abstract = True