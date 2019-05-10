from rest_framework import routers

from . import views

router_v1 = routers.DefaultRouter()

router_v1.register(
    r'data-clusters',
    views.DataClusterViewSet,
    base_name='data-cluster'
)

# router_v1.register(
#     r'data-clusters',
#     views.DataClusterViewSet,
#     base_name='data-cluster'
# )