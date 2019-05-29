from django.db import models
from django.contrib.auth.models import User as BaseUser

from boogie.rest import rest_api

@rest_api(["id"])
class User(BaseUser):
    """
    asddsaidsadasj
    """

@rest_api()
class DataCluster(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    collected_at = models.DateTimeField(auto_now=True)
    
@rest_api()
class Data(models.Model):
    data_cluster = models.ForeignKey(DataCluster, on_delete=models.CASCADE)

    class Meta:
        abstract = True