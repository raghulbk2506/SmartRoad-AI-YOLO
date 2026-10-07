# Technical Improvements Added in Review Stage

The review-stage implementation adds modular code for better maintainability
and future validation.

## 1. Central configuration
`ai/config.py` moves vehicle classes, congestion thresholds and parking-zone
parameters into one place. This makes calibration easier without editing the
core detection logic.

## 2. Persistent vehicle IDs
`ai/centroid_tracker.py` adds a lightweight nearest-centroid tracker. It can
associate detections across frames and provides a foundation for determining
whether a vehicle remains stationary.

## 3. Reusable analytics
`ai/analytics.py` separates congestion classification and summary calculations
from video-processing code.

## 4. Automated checks
`ai/test_analytics.py` contains basic tests for congestion levels and summary
statistics.

## 5. Responsible interpretation
The project does not claim that zone occupancy automatically means illegal
parking. Real deployment would require calibrated camera geometry, robust
tracking, stationary-duration thresholds, privacy controls and validation
with representative road footage.
