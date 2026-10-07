"""Reusable traffic analytics helpers."""

def congestion_level(vehicle_count, low=8, high=18):
    if vehicle_count < low:
        return "LOW"
    if vehicle_count < high:
        return "MEDIUM"
    return "HIGH"


def summarize_counts(counts):
    counts = list(counts)
    if not counts:
        return {
            "frames": 0,
            "average_vehicle_count": 0,
            "peak_vehicle_count": 0,
        }
    return {
        "frames": len(counts),
        "average_vehicle_count": round(sum(counts) / len(counts), 2),
        "peak_vehicle_count": max(counts),
    }
