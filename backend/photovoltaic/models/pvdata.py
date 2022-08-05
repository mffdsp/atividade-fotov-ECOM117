from django.db import models

class PVData(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    irradiation = models.FloatField(default=0, null=True)
    temperature_pv = models.FloatField(default=0, null=True)
    temperature_amb = models.FloatField(default=0, null=True)
    voltage_s1 = models.FloatField(default=0, null=True)
    current_s1 = models.FloatField(default=0, null=True)
    power_s1 = models.FloatField(default=0, null=True)
    voltage_s2 = models.FloatField(default=0, null=True)
    current_s2 = models.FloatField(default=0, null=True)
    power_s2 = models.FloatField(default=0, null=True)
    power_avg = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.timestamp