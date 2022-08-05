from rest_framework import serializers
from .models import (
    PVData,
)

class PVDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PVData
        fields = ['timestamp', 'irradiation', 'temperature_pv', 'temperature_amb',
                'voltage_s1', 'current_s1', 'power_s1',
                'voltage_s2', 'current_s2', 'power_s2',
                'power_avg']