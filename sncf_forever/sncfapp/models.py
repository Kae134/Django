from django.db import models
from django.utils import timezone


class Trains(models.Model):

    trainId = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    image = models.CharField(max_length = 300, null=True)
    departure = models.TimeField(default=timezone.now)
    arrive = models.TimeField(default=timezone.now)
    destination = models.CharField(max_length = 30)
    description = models.TextField()

