"""Central configuration for the SmartRoad AI prototype."""

VEHICLE_CLASSES = {"car", "motorcycle", "bus", "truck"}

# Prototype thresholds; calibrate with local traffic data before real deployment.
CONGESTION_LOW = 8
CONGESTION_HIGH = 18

# Parking-zone configuration as a fraction of frame height.
PARKING_ZONE_TOP_RATIO = 0.72

# A vehicle must remain near the same position for this many frames
# before the optional stationary-vehicle logic flags it.
STATIONARY_FRAMES = 20
POSITION_TOLERANCE_PX = 45
