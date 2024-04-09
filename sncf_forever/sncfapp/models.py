from django.db import models

class Trains(models.Model):

    trainId = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    image = models.CharField(max_length = 300, null=True)
    destination = models.CharField(max_length = 30)
    description = models.TextField()

