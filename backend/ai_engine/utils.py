import math


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Returns distance in kilometers
    """

    R = 6371  # Earth radius in KM

    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(d_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c
def estimate_eta_minutes(distance_km, avg_speed_kmph=45):
    """
    Estimate travel time in minutes
    """
    if avg_speed_kmph <= 0:
        return None

    return int((distance_km / avg_speed_kmph) * 60)
