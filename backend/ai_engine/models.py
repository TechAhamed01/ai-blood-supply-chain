from django.db import models
from blood_requests.models import BloodRequest
from bloodbanks.models import BloodBank


class AllocationSuggestion(models.Model):
    blood_request = models.ForeignKey(BloodRequest, on_delete=models.CASCADE)
    suggested_blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
    distance_km = models.FloatField()
    eta_minutes = models.IntegerField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
