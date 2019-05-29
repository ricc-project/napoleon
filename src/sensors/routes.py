from boogie.router import Router
from django.http import Http404, HttpResponse
from .models import User

urlpatterns = Router()

@urlpatterns.route("signup/")
def signup(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = User.objects.create_user(username, password)
            response = {"authentication_token": user.authToken}
            return HttpResponse(str(response))
        else:
            return Http404("You need to send password and username.")
    return Http404("Can't signup with GET method.")

@urlpatterns.route("login/")
def login(request):
    return {}