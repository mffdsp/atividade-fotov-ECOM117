from django.contrib import admin

from .models import PVData, PowerForecast

# Register your models here.

admin.site.register(PVData)
admin.site.register(PowerForecast)