from django.db import models

# Create your models here.
class Port(models.Model):
    country = models.CharField(max_length=100)
    city = models.TextField(max_length=100)
    name = models.TextField(max_length=100)

class Trip(models.Model):
    fromPort = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='fromPort')
    toPort = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='toPort')
    cost = models.FloatField()
    currency = models.CharField(max_length=10)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    duration = models.DurationField()
    scales = models.PositiveSmallIntegerField()
    sourceURL = models.URLField()