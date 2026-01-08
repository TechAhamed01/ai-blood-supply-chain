from django.urls import path
from . import views

urlpatterns = [
    # 1. Create blood request
    path("request/create/", views.create_blood_request, name="create_blood_request"),

    # 2. Generate AI suggestions for a request
    path(
        "request/<int:request_id>/suggestions/",
        views.generate_suggestions,
        name="generate_suggestions",
    ),

    # 3. Confirm selected blood bank
    path(
        "suggestion/<int:suggestion_id>/confirm/",
        views.confirm_allocation,
        name="confirm_allocation",
    ),

    # 4. Assign driver & create delivery
    path("delivery/assign/", views.assign_driver, name="assign_driver"),

    # 5. Update delivery status
    path(
        "delivery/<int:delivery_id>/status/",
        views.update_delivery_status,
        name="update_delivery_status",
    ),

    # 6. Track blood request / delivery
    path("track/<int:request_id>/", views.track_request, name="track_request"),
]
