from django.contrib import admin

from .models import PVData, PowerForecast, YieldDay

# Register your models here.

admin.site.register(PVData)
admin.site.register(PowerForecast)
admin.site.register(YieldDay)