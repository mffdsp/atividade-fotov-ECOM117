from django.db import models

class YieldYear(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    yield_year = models.FloatField(default=0, null=True) 
    yield_year_forecast = models.FloatField(default=0, null=True)

    def __str__(self):
        return str(self.timestamp) + " " + str(self.yield_year) + " " + str(self.yield_year_forecast)