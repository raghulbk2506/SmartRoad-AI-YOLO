# Technical Architecture
`Video/Webcam → OpenCV → YOLO detection → vehicle filtering → parking-zone overlap → congestion heuristic → annotated video + JSON`

Current prototype limitations:
1. Counts are per-frame, not unique vehicles.
2. Parking-zone presence does not prove a vehicle is stationary.
3. Thresholds require calibration.
4. Weather, darkness, occlusion and camera angle affect accuracy.

Recommended next step: add multi-object tracking and classify a vehicle as parked only after it remains nearly stationary inside the zone.
