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
    AllocationSuggestionSerializer,
    DeliverySerializer,
    # BloodRequestSerializer can be imported from api/serializers or create here
)
from api.serializers import BloodRequestSerializer  # reuse serializer
@api_view(["POST"])
def create_blood_request(request):
    serializer = BloodRequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def generate_suggestions(request, request_id):
    try:
        blood_request = BloodRequest.objects.get(id=request_id)
    except BloodRequest.DoesNotExist:
        return Response({"error": "Request not found"}, status=404)

    suggestions = suggest_blood_banks(blood_request)

    saved = []

    for s in suggestions:
        obj = AllocationSuggestion.objects.create(
            blood_request=blood_request,
            suggested_blood_bank=s["blood_bank"],
            distance_km=s["distance_km"],
            eta_minutes=s["eta_minutes"],
            score=s["score"],
        )
        saved.append(obj)

    serializer = AllocationSuggestionSerializer(saved, many=True)
    return Response(serializer.data)
@api_view(["POST"])
def confirm_allocation(request, suggestion_id):
    try:
        suggestion = AllocationSuggestion.objects.get(id=suggestion_id)
    except AllocationSuggestion.DoesNotExist:
        return Response({"error": "Suggestion not found"}, status=404)

    blood_request = suggestion.blood_request
    blood_request.status = "ALLOCATED"
    blood_request.save()

    return Response({"message": "Blood bank confirmed successfully"})
@api_view(["POST"])
def assign_driver(request):
    blood_request_id = request.data.get("blood_request_id")
    driver_id = request.data.get("driver_id")

    try:
        blood_request = BloodRequest.objects.get(id=blood_request_id)
        driver = Driver.objects.get(id=driver_id)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

    delivery = Delivery.objects.create(
        blood_request=blood_request,
        driver=driver,
        status="ASSIGNED",
    )

    serializer = DeliverySerializer(delivery)
    return Response(serializer.data)
@api_view(["POST"])
def update_delivery_status(request, delivery_id):
    status_text = request.data.get("status")

    try:
        delivery = Delivery.objects.get(id=delivery_id)
    except Delivery.DoesNotExist:
        return Response({"error": "Delivery not found"}, status=404)

    delivery.status = status_text
    delivery.save()

    return Response({"message": "Status updated successfully"})
@api_view(["GET"])
def track_request(request, request_id):
    try:
        delivery = Delivery.objects.get(blood_request_id=request_id)
    except Delivery.DoesNotExist:
        return Response({"message": "Delivery not assigned yet"})

    serializer = DeliverySerializer(delivery)
    return Response(serializer.data)
