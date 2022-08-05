from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PVDataSerializer
from .models import PVData

# Create your views here.

class PVViewSet(viewsets.ModelViewSet):
    serializer_class = PVDataSerializer
    queryset = PVData.objects.all()