from django.db import models

class PowerForecast(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    t1 = models.FloatField(default=0, null=True)
    t2 = models.FloatField(default=0, null=True)
    t3 = models.FloatField(default=0, null=True)
    t4 = models.FloatField(default=0, null=True)
    t5 = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.timestamp