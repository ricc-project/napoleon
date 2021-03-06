from django.contrib import admin
from django.urls import path, include
from boogie.rest import rest_api
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sensors.routes')),
    path('api/', include(rest_api.urls))
]
