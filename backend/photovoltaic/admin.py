from django.contrib import admin

from .models import PVData, PowerForecast, YieldDay, YieldMonth, YieldYear, YieldMinute

# Register your models here.

admin.site.register(PVData)
admin.site.register(PowerForecast)
admin.site.register(YieldDay)
admin.site.register(YieldMonth)
admin.site.register(YieldYear)
admin.site.register(YieldMinute)