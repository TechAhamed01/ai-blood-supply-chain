from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from blood_requests.models import BloodRequest
from ai_engine.recommender import suggest_blood_banks
from ai_engine.models import AllocationSuggestion
from delivery.models import Delivery, Driver

from .serializers import (
    BloodRequestSerializer,
    AllocationSuggestionSerializer,
    DeliverySerializer,
)
