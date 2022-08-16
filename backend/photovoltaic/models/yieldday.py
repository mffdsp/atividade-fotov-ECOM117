from django.db import models

class YieldDay(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    yield_day = models.FloatField(default=0, null=True) 
    yield_day_forecast = models.FloatField(default=0, null=True)

    def __str__(self):
        return str(self.timestamp) + " " + str(self.yield_day) + " " + str(self.yield_day_forecast)