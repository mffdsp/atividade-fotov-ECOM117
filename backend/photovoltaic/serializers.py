from rest_framework import serializers
from .models import (
    PVData,
    PVString,
    PowerForecast,
)

class PVStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = PVString
        fields = ['name', 'timestamp', 'voltage', 'current', 'power']

class PVDataSerializer(serializers.ModelSerializer):
    strings = PVStringSerializer(read_only=True, many=True)

    class Meta:
        model = PVData
        fields = ['timestamp', 'irradiation', 'temperature_pv', 'temperature_amb', 'power_avg', 'strings']

class PowerForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerForecast
        fields = ['timestamp', 't1', 't2', 't3', 't4', 't5']