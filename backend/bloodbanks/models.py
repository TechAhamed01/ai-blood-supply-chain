
from django.db import models


class BloodBank(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
