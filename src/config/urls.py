from django.contrib import admin
from django.urls import path, include

from sensors.urls import router_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_v1.urls))
]
