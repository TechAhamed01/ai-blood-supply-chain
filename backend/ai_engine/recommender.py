from datetime import date
from bloodbanks.models import BloodBank
from inventory.models import BloodInventory
from .utils import haversine_distance, estimate_eta_minutes


def suggest_blood_banks(request):
    """
    Input: BloodRequest object
    Output: List of ranked blood bank suggestions
    """

    hospital = request.hospital

    suggestions = []

    blood_banks = BloodBank.objects.all()

    for bank in blood_banks:
        inventories = BloodInventory.objects.filter(
            blood_bank=bank,
            blood_group=request.blood_group,
            units_available__gte=request.units_required
        )

        if not inventories.exists():
            continue  # not enough blood

        # choose earliest expiry to reduce waste
        inventory = inventories.order_by("expiry_date").first()

        # distance
        distance = haversine_distance(
            hospital.latitude,
            hospital.longitude,
            bank.latitude,
            bank.longitude
        )

        # ETA
        eta = estimate_eta_minutes(distance)

        # score: nearer + soon expiry preferred
        expiry_days_left = (inventory.expiry_date - date.today()).days

        score = (1 / (distance + 1)) + (1 / (expiry_days_left + 1))

        suggestions.append({
            "blood_bank": bank,
            "distance_km": round(distance, 2),
            "eta_minutes": eta,
            "expiry_days_left": expiry_days_left,
            "score": round(score, 4),
        })

    # sort best first
    suggestions = sorted(suggestions, key=lambda x: x["score"], reverse=True)

    return suggestions
