from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import (
    PVData,
    PVString,
    PowerForecast,
    YieldDay,
    YieldMonth
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

class YieldDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldDay
        fields = ['timestamp', 'yield_day', 'yield_day_forecast']

class YieldMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldMonth
        fields = ['timestamp', 'yield_month', 'yield_month_forecast']