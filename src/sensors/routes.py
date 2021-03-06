from datetime import timezone, timedelta
from django.core import serializers
from boogie.router import Router
from django.http import Http404, HttpResponse, JsonResponse
from .models import User, json_names, DataCluster
from .serializer import create_serializer, DataClusterSerializer
from .manager import verify_password
from rest_framework import status
import hashlib
import binascii
import json
urlpatterns = Router()


@urlpatterns.route("signup/")
def signup(request):
    rstatus = status.HTTP_403_FORBIDDEN
    if(request.method == "POST"):
        data = json.loads(request.body)
        if data.keys() >= {"username", "password"}:
            username = data['username']
            password = data['password']
            try:
                user = User.objects.create_user(username, password)
                response = {"authentication_token": str(user.auth_token)}
                rstatus = status.HTTP_201_CREATED
            except:
                response = {"Unavailable username": "username already taken"}
        else:
            response = {
                "Not enough credencials": "You need to send password and username."}
    else:
        response = {"Wrong method.": "Can't signup with GET method."}

    return JsonResponse(response)


@urlpatterns.route("login/")
def login(request):

    rstatus = status.HTTP_403_FORBIDDEN
    user = verify_auth(request)
    response = response = {"Incorrect Credentials": "Invalid login information."}
    data = json.loads(request.body)
    password = data['password']
    if(verify_password(user, password)):
        response = {"authentication_token": str(user.auth_token)}
        rstatus = status.HTTP_202_ACCEPTED
    else:
        response = {"Incorrect Credentials": "Invalid login information."}
    
    return JsonResponse(response)

@urlpatterns.route('send-data/')
def send_data(request):
    user = verify_auth(request)
    data = get_data(request)
    time = get_time(request)
    print(data)
    if user and data and time:
        # try:
        create_data(user, data, time)
        return HttpResponse("Ae", status=status.HTTP_201_CREATED)
        # except:
            # return HttpResponse("Data in invalid format", status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return HttpResponse("Unauthorized.", status=status.HTTP_403_FORBIDDEN)

@urlpatterns.route('get_last/')
def last_data(request):
    user = verify_auth(request)
    if user:
        data_cluster = user.data.last()
        serializer = DataClusterSerializer(data_cluster)
        data = serializer.data

        if data_cluster is not None:
            brazil_hour = data_cluster.collected_at.astimezone(timezone(timedelta(hours=-3)))
            collected_at = brazil_hour.strftime("%d/%m/%Y - %H:%M:%S")
            data.update({'collected_at': collected_at})
        
        data = json.dumps(data)
        
        return HttpResponse(data, status=status.HTTP_200_OK)
    else:
        return HttpResponse("Unauthorized.", status=status.HTTP_403_FORBIDDEN)

@urlpatterns.route('get_period_data/')
def period_data(request):
    if(request.method == "POST"):
        request_data = json.loads(request.body)

        user = verify_auth(request)

        if user:
            results = []
            data_clusters = list(user.data.all())[-20:]
            filters = request_data['filters']

            category = filters['category']
            measure = filters['measure']
            amount = filters['amount']

            measures = []
            collects = []


            for data_cluster in data_clusters:
                result = {}
                data_measure = {}
                serializer = DataClusterSerializer(data_cluster)
                data = serializer.data


                if serializer.data is not None:
                    brazil_hour = data_cluster.collected_at.astimezone(timezone(timedelta(hours=-3)))
                    collected_at = brazil_hour.timestamp() * 1000
                    collects.append(collected_at)

                    data_measure.update(
                        {
                            "value": serializer.data[category][0][measure],
                            "time": collected_at
                        }
                    )
                    measures.append(data_measure)
                    
            result = {
                "data": measures,
                "labels": collects
            }
            print(result)
            return HttpResponse(json.dumps(result), status=status.HTTP_200_OK)
        else:
            return HttpResponse("Unauthorized.", status=status.HTTP_403_FORBIDDEN)


@urlpatterns.route('get_last_switch_activated/')
def last_switch_activated(request):
    user = verify_auth(request)
    if user:
        last_data_cluster = user.data.last()
        data = {}

        if last_data_cluster is not None:
            brazil_hour = last_data_cluster.collected_at.astimezone(timezone(timedelta(hours=-3)))
            collected_at = brazil_hour.strftime("%d/%m/%Y - %H:%M:%S")
            data.update({'collected_at': collected_at})
        
        activated_data_cluster = user.data.filter(actuatordata__status=True).last()
        print("active", activated_data_cluster)

        if activated_data_cluster is not None:
            brazil_hour = activated_data_cluster.collected_at.astimezone(timezone(timedelta(hours=-3)))
            collected_at = brazil_hour.strftime("%d/%m/%Y - %H:%M:%S")
            data.update({'last_active': last_active})

        data = json.dumps(data)
        
        return HttpResponse(data, status=status.HTTP_200_OK)
    else:
        return HttpResponse("Unauthorized.", status=status.HTTP_403_FORBIDDEN)


def create_data(user, cluster_data, time):
    # TODO use time on DataCluster Constructor
    cluster = DataCluster(owner=user)
    cluster.save()
    print("Received data for: " + str(cluster_data.keys()))
    for data in cluster_data.keys():
        serializer = create_serializer(data)
        serializer = serializer(data=cluster_data[data])

        if serializer.is_valid():
            model = json_names[data]['model'](**serializer.data)
            model.data_cluster = cluster
            model.save()
            print("saved: " + data)

def verify_auth(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        if 'auth_token' in data.keys():
            user = User.objects.filter(auth_token=data['auth_token'])
            print(user)
            if user:
                return user.first()
        return None
    else:
        return None

def get_data(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        if 'data' in data.keys():
            return data['data']
        return None
    else:
        return None


def get_time(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        if 'timestamp' in data.keys():
            return data['timestamp']
        return None
    else:
        return None