
from django.db import models
from accounts.models import User
from bloodbanks.models import BloodBank
from blood_requests.models import BloodRequest
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_blood_bank = models.ForeignKey(BloodBank, on_delete=models.SET_NULL, null=True)
    vehicle_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
class Delivery(models.Model):
    blood_request = models.OneToOneField(BloodRequest, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    
    pickup_time = models.DateTimeField(null=True, blank=True)
    drop_time = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=(
            ('ASSIGNED', 'Assigned'),
            ('PICKED_UP', 'Picked Up'),
            ('ON_THE_WAY', 'On the Way'),
            ('DELIVERED', 'Delivered'),
        ),
        default='ASSIGNED'
    )

    def __str__(self):
        return f"Delivery for Request {self.blood_request.id}"

