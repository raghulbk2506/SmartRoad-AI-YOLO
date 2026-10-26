# Technical Improvements — Next Review

- Centralized detection configuration defaults.
- Added a lightweight centroid tracking foundation.
- Added reusable congestion classification and summary helpers.
- Added standard-library unit tests.

## Limitations
- The centroid tracker is a basic nearest-neighbour baseline and can lose identities when objects overlap or cross.
- It is not yet wired into the original detection pipeline.
- Congestion thresholds are example values and need calibration on representative footage.
- Repeated per-frame detections are not unique vehicle counts unless tracking-aware aggregation is implemented.
- Detection inside a parking zone does not prove illegal parking or stationary duration.

## Validation checklist
1. Run the unit tests.
2. Test on representative road footage.
3. Record false positives and missed detections.
4. Collect and document actual feedback from at least three real users.
