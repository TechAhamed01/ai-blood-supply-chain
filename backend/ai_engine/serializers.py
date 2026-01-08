from rest_framework import serializers
from ai_engine.models import AllocationSuggestion
from delivery.models import Delivery
from blood_requests.models import BloodRequest


class AllocationSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocationSuggestion
        fields = "__all__"


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"


class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = "__all__"
