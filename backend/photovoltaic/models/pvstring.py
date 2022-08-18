from unicodedata import name
from django.db import models

class PVString(models.Model):
    name = models.CharField(max_length=1024, primary_key=True)
    timestamp = models.DateTimeField()
    voltage = models.FloatField(default=0, null=True)
    current = models.FloatField(default=0, null=True)
    power = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.name + " " + str(self.voltage) + " " + str(self.current) + " " + str(self.power)