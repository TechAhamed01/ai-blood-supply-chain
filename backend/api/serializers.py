from rest_framework import serializers
from blood_requests.models import BloodRequest
from hospitals.models import Hospital
from ai_engine.models import AllocationSuggestion
from delivery.models import Delivery, Driver


class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = "__all__"


class AllocationSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocationSuggestion
        fields = "__all__"


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"
