"""Reusable congestion and JSON-summary helpers."""
def classify_congestion(vehicle_count, low_max=5, medium_max=12):
    if vehicle_count < 0:
        raise ValueError("vehicle_count cannot be negative")
    if low_max < 0 or medium_max < low_max:
        raise ValueError("thresholds must satisfy 0 <= low_max <= medium_max")
    if vehicle_count <= low_max:
        return "LOW"
    if vehicle_count <= medium_max:
        return "MEDIUM"
    return "HIGH"

def build_summary(frame_count, vehicle_count, congestion):
    if frame_count < 0 or vehicle_count < 0:
        raise ValueError("counts cannot be negative")
    label = str(congestion).upper()
    if label not in {"LOW", "MEDIUM", "HIGH"}:
        raise ValueError("congestion must be LOW, MEDIUM, or HIGH")
    return {"frame_count": int(frame_count), "vehicle_count": int(vehicle_count), "congestion": label}
