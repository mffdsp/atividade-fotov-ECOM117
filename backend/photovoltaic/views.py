from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PVDataSerializer, PowerForecastSerializer
from .models import PVData, PowerForecast

# Create your views here.

class PVViewSet(viewsets.ModelViewSet):
    serializer_class = PVDataSerializer
    queryset = PVData.objects.all()

class PowerForecastSet(viewsets.ModelViewSet):
    serializer_class = PowerForecastSerializer
    queryset = PowerForecast.objects.all()