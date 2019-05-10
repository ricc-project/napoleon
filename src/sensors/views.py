from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import DataCluster
from .serializers import DataClusterSerializer


class DataClusterViewSet(viewsets.ModelViewSet):
    serializer_class = DataClusterSerializer
    queryset = DataCluster.objects.all()
    
    def list(self, request):
        serializer = DataClusterSerializer(
            self.queryset,
            many=True,
            context={'request', request}
        )

        return Response(serializer.data)