from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from .util import get_time_inteval, generate_forecast_json

from .serializers import (
    PVDataSerializer,
    PVDataMeteorologicalSerializer,
    PVDataPowerSerializer,
    PowerForecastSerializer,
    YieldDaySerializer,
    YieldMonthSerializer,
    YieldYearSerializer,
    YieldMinuteSerializer)
from .models import (
    PVData,
    PowerForecast,
    YieldDay,
    YieldMonth,
    YieldYear,
    YieldMinute)

# Create your views here.

class PVDataViewSet(viewsets.ModelViewSet):
    queryset = PVData.objects.all()
    serializer_class = PVDataSerializer

    @action(methods=['GET'], url_path='latest', detail=False)
    def pv_data_latest(self, request):
        latest_data = PVData.objects.latest('timestamp')
        return Response(PVDataSerializer(latest_data).data)

    @action(methods=['GET'], url_path='meteorologicalhistory', detail=False)
    def meteorological_history(self, request):
        now = datetime.now()
        datetime_lte = now.strftime('%Y-%m-%dT%H:%M:%S.%f-03:00')
        yesterday = now - timedelta(days=1)
        datetime_gte = yesterday.strftime('%Y-%m-%dT%H:%M:%S.%f-03:00')
        day_data = PVData.objects.filter(timestamp__gte=datetime_gte, timestamp__lte=datetime_lte)

        return Response(PVDataMeteorologicalSerializer(day_data, many=True).data)

    @action(methods=['GET'], url_path='powerhistory', detail=False)
    def power_history(self, request):
        time_interval = get_time_inteval(request)

        now = datetime.now()
        datetime_lte = now.strftime('%Y-%m-%dT%H:%M:%S.%f-03:00')
        yesterday = now - timedelta(minutes=time_interval)
        datetime_gte = yesterday.strftime('%Y-%m-%dT%H:%M:%S.%f-03:00')
        power_data = PVData.objects.filter(timestamp__gte=datetime_gte, timestamp__lte=datetime_lte)

        return Response(PVDataPowerSerializer(power_data, many=True).data)

class PowerForecastViewSet(viewsets.ModelViewSet):
    queryset = PowerForecast.objects.all()
    serializer_class = PowerForecastSerializer

    @action(methods=['GET'], url_path='history', detail=False)
    def forecast_history(self, request):
        time_interval = get_time_inteval(request)

        now = datetime.now()
        datetime_lte = now.strftime('%Y-%m-%dT%H:%M:%S.%f-03:00')
        yesterday = now - timedelta(minutes=time_interval+1)
        datetime_gte = yesterday.strftime('%Y-%m-%dT%H:%M:%S.%f-03:00')
        power_forecast = PowerForecast.objects.filter(timestamp__gte=datetime_gte, timestamp__lte=datetime_lte)

        forecast_json = generate_forecast_json(PowerForecastSerializer(power_forecast, many=True).data)

        return Response(forecast_json)

class YieldDayViewSet(viewsets.ModelViewSet):
    queryset = YieldDay.objects.all()
    serializer_class = YieldDaySerializer

    @action(methods=['GET'], url_path='now', detail=False)
    def yield_now(self, request):
        yield_today = YieldDay.objects.latest('timestamp')
        return Response(YieldDaySerializer(yield_today).data)

    @action(methods=['GET'], url_path='latest15', detail=False)
    def yield_latest_15(self, request):
        now = datetime.now()
        datetime_lte = now.strftime('%Y-%m-%dT23:59:59.999999-03:00')
        yesterday = now - timedelta(days=15)
        datetime_gte = yesterday.strftime('%Y-%m-%dT00:00:00.000000-03:00')
        yield_days = YieldDay.objects.filter(timestamp__gte=datetime_gte, timestamp__lte=datetime_lte)

        return Response(YieldDaySerializer(yield_days, many=True).data)

class YieldMonthViewSet(viewsets.ModelViewSet):
    queryset = YieldMonth.objects.all()
    serializer_class = YieldMonthSerializer

    @action(methods=['GET'], url_path='latest12', detail=False)
    def yield_latest_12(self, request):
        now = datetime.now()
        datetime_lte = now.strftime('%Y-%m-%dT23:59:59.999999-03:00')
        yesterday = now - relativedelta(months=12)
        datetime_gte = yesterday.strftime('%Y-%m-01T00:00:00.000000-03:00')
        yield_months = YieldMonth.objects.filter(timestamp__gte=datetime_gte, timestamp__lte=datetime_lte)

        return Response(YieldMonthSerializer(yield_months, many=True).data)

class YieldYearViewSet(viewsets.ModelViewSet):
    queryset = YieldYear.objects.all()
    serializer_class = YieldYearSerializer

    @action(methods=['GET'], url_path='latest10', detail=False)
    def yield_latest_10(self, request):
        now = datetime.now()
        datetime_lte = now.strftime('%Y-%m-%dT23:59:59.999999-03:00')
        yesterday = now - relativedelta(months=120)
        datetime_gte = yesterday.strftime('%Y-01-01T00:00:00.000000-03:00')
        yield_year = YieldYear.objects.filter(timestamp__gte=datetime_gte, timestamp__lte=datetime_lte)

        return Response(YieldYearSerializer(yield_year, many=True).data)

class YieldMinuteViewSet(viewsets.ModelViewSet):
    queryset = YieldMinute.objects.all()
    serializer_class = YieldMinuteSerializer

    @action(methods=['GET'], url_path='today', detail=False)
    def yield_today(self, request):
        now = datetime.now()
        datetime_lte = now.strftime('%Y-%m-%dT%H:%M:%S.%f-03:00')
        datetime_gte = now.strftime('%Y-%m-%dT00:00:00.000000-03:00')
        yield_today = YieldMinute.objects.filter(timestamp__gte=datetime_gte, timestamp__lte=datetime_lte)

        return Response(YieldMinuteSerializer(yield_today, many=True).data)