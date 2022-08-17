from django.db import models

class YieldMonth(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    yield_month = models.FloatField(default=0, null=True) 
    yield_month_forecast = models.FloatField(default=0, null=True)

    def __str__(self):
        return str(self.timestamp) + " " + str(self.yield_month) + " " + str(self.yield_month_forecast)