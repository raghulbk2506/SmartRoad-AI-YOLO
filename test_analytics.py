from analytics import congestion_level, summarize_counts


def test_congestion_levels():
    assert congestion_level(3, 8, 18) == "LOW"
    assert congestion_level(10, 8, 18) == "MEDIUM"
    assert congestion_level(20, 8, 18) == "HIGH"


def test_summary():
    result = summarize_counts([2, 4, 6])
    assert result["frames"] == 3
    assert result["average_vehicle_count"] == 4
    assert result["peak_vehicle_count"] == 6


if __name__ == "__main__":
    test_congestion_levels()
    test_summary()
    print("All SmartRoad AI analytics tests passed.")
