from boogie.router import Router

urlpatterns = Router()

@urlpatterns.route("")
def detail(request):
    user = request.user
    return {"user": user
    }