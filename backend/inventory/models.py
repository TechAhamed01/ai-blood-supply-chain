
from django.db import models
from bloodbanks.models import BloodBank


class BloodInventory(models.Model):
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    )

    blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    units_available = models.PositiveIntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.blood_group} - {self.blood_bank.name}"
