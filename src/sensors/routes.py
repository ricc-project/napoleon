from boogie.router import Router
from django.http import Http404, HttpResponse
from .models import User
from rest_framework import status

urlpatterns = Router()

@urlpatterns.route("signup/")
def signup(request):
    rstatus = status.HTTP_403_FORBIDDEN
    if(request.method == "POST"):
        if request.POST.keys() >= {"username", "password"}:
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.create_user(username, password)
            except:
                response = {"Unavailable username": "username already taken"}
            response = {"authentication_token": user.authToken}
            rstatus = status.HTTP_200_OK
        else:
            response = {"Not enough credencials": "You need to send password and username."}
    else:
        response = {"Wrong method.": "Can't signup with GET method."}

    return HttpResponse(str(response), status=rstatus)

@urlpatterns.route("login/")
def login(request):
    return {}