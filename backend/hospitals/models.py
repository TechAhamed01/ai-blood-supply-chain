
# Create your models here.
from django.db import models
from accounts.models import User


class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
