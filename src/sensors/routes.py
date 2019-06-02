from django.core import serializers
from boogie.router import Router
from django.http import Http404, HttpResponse, JsonResponse
from .models import User, json_names, DataCluster
from .serializer import create_serializer
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
    if(verify_sent_credentials(request)):
        username = request.POST['username']
        password = request.POST['password']
        user = None
        try:
            user = User.objects.get(username=username)
        except:
            response = response = {"Incorrect Credentials": "Invalid login information."}

        if(verify_password(user, password)):
            response = {"authentication_token": str(user.auth_token)}
            rstatus = status.HTTP_202_ACCEPTED
        else:
            response = {"Incorrect Credentials": "Invalid login information."}
    else:
        response = {
            "Not enough information sent to do this.":
            "No username or Password, maybe not a POST method."}
    
    return JsonResponse(response)

@urlpatterns.route('send-data/')
def send_data(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        if 'auth_token' in data.keys():
            if 'data' in data.keys():
                user = User.objects.filter(auth_token=data['auth_token'])
                if user:
                    # try:
                    create_data(user.first(), json.loads(request.POST['data']))
                    return HttpResponse("Ae", status=status.HTTP_201_CREATED)
                    # except:
                        # return HttpResponse("Data in invalid format", status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return HttpResponse("Unauthorized.", status=status.HTTP_403_FORBIDDEN)
            else:
                return HttpResponse("No data.", status=status.HTTP_403_FORBIDDEN)
        return HttpResponse("Unauthorized.", status=status.HTTP_403_FORBIDDEN)
    return HttpResponse("Wrong http method, not a POST!", status=status.HTTP_400_BAD_REQUEST)


def create_data(user, request_data):
    cluster = DataCluster(owner=user)
    cluster.save()
    print("Received data for: " + str(request_data.keys()))
    for data in request_data.keys():
        serializer = create_serializer(data)
        serializer = serializer(data=request_data[data])
        if serializer.is_valid():
            model = json_names[data]['model'](**serializer.data)
            model.data_cluster = cluster
            model.save()

def verify_sent_credentials(request):
    if(request.method == "POST"):
        if request.POST.keys() >= {"username", "password"}:
            return True
    return False



    return pwdhash == stored_password