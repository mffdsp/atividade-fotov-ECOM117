from rest_framework import serializers
from .models import (
    PVData,
    PVString,
    PowerForecast,
    YieldDay,
    YieldMonth,
    YieldYear,
    YieldMinute,
    AlertTreshold,
    Settings
)

class PVStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = PVString
        fields = ['name', 'timestamp', 'voltage', 'current', 'power', 'voltage_alert', 'current_alert', 'string_number']

class PVDataSerializer(serializers.ModelSerializer):
    strings = PVStringSerializer(read_only=True, many=True)

    class Meta:
        model = PVData
        fields = ['timestamp', 'irradiation', 'temperature_pv', 'temperature_amb', 'power_avg', 'strings']

class PVDataMeteorologicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PVData
        fields = ['timestamp', 'irradiation', 'temperature_pv', 'temperature_amb']

class PVDataPowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PVData
        fields = ['timestamp', 'power_avg']

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

class YieldYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldYear
        fields = ['timestamp', 'yield_year', 'yield_year_forecast']

class YieldMinuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldMinute
        fields = ['timestamp', 'yield_minute', 'yield_day_forecast']

class AlertTresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertTreshold
        fields = ['id', 'alert_type', 'string_number', 'meteorological_value', 'treshold_wa_max', 'treshold_wa_min', 'treshold_ft_max', 'treshold_ft_min']

class SettingaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'fault_vt_percentile', 'warning_vt_percentile', 'delt_vt', 'fault_cr_percentile', 'warning_cr_percentile', 'delt_cr',
                'fault_user_active', 'warning_user_active', 'alert_days_active', 'days_left', 'retraining_interval']