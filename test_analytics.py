import unittest
from analytics import build_summary, classify_congestion

class AnalyticsTests(unittest.TestCase):
    def test_thresholds(self):
        self.assertEqual(classify_congestion(5), "LOW")
        self.assertEqual(classify_congestion(6), "MEDIUM")
        self.assertEqual(classify_congestion(12), "MEDIUM")
        self.assertEqual(classify_congestion(13), "HIGH")
    def test_custom_thresholds(self):
        self.assertEqual(classify_congestion(3, 2, 4), "MEDIUM")
    def test_negative_count(self):
        with self.assertRaises(ValueError):
            classify_congestion(-1)
    def test_summary(self):
        self.assertEqual(build_summary(20, 7, "medium"),
                         {"frame_count": 20, "vehicle_count": 7, "congestion": "MEDIUM"})
    def test_invalid_summary(self):
        with self.assertRaises(ValueError):
            build_summary(-1, 0, "LOW")

if __name__ == "__main__":
    unittest.main()
