
from django.db import models
from hospitals.models import Hospital


class BloodRequest(models.Model):
    URGENCY_CHOICES = (
        ('NORMAL', 'Normal'),
        ('URGENT', 'Urgent'),
        ('CRITICAL', 'Critical'),
    )

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    units_required = models.PositiveIntegerField()
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES)

    status = models.CharField(
        max_length=20,
        choices=(
            ('REQUESTED', 'Requested'),
            ('APPROVED', 'Approved'),
            ('ALLOCATED', 'Allocated'),
            ('DISPATCHED', 'Dispatched'),
            ('ON_THE_WAY', 'On the way'),
            ('DELIVERED', 'Delivered'),
            ('REJECTED', 'Rejected'),
        ),
        default='REQUESTED'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hospital.name} - {self.blood_group} ({self.units_required})"
