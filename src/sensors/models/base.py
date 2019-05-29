from django.db import models
from boogie.rest import rest_api
from ..manager import UserManager

@rest_api(['username'])
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    hash = models.CharField(max_length=128)
    authToken = models.CharField(max_length=64)
    objects = UserManager()
       

@rest_api()
class DataCluster(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    collected_at = models.DateTimeField(auto_now=True)

class Data(models.Model):
    data_cluster = models.ForeignKey(DataCluster, on_delete=models.CASCADE)

    class Meta:
        abstract = True