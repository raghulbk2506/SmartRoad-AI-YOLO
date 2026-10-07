"""Lightweight centroid tracker for the SmartRoad AI prototype.

This tracker assigns persistent IDs using nearest-centroid matching.
It is intentionally simple and dependency-light; it is not a production
multi-object tracker.
"""

import math


class CentroidTracker:
    def __init__(self, max_distance=70, max_missing=10):
        self.next_id = 1
        self.objects = {}
        self.missing = {}
        self.max_distance = max_distance
        self.max_missing = max_missing

    @staticmethod
    def _centroid(box):
        x1, y1, x2, y2 = box
        return ((x1 + x2) // 2, (y1 + y2) // 2)

    def update(self, boxes):
        centers = [self._centroid(b) for b in boxes]

        if not self.objects:
            for center in centers:
                self.objects[self.next_id] = center
                self.missing[self.next_id] = 0
                self.next_id += 1
            return dict(self.objects)

        assigned = set()
        updated = {}

        # Greedy nearest-neighbour matching.
        for object_id, old_center in list(self.objects.items()):
            best_idx, best_dist = None, float("inf")
            for idx, center in enumerate(centers):
                if idx in assigned:
                    continue
                dist = math.hypot(center[0] - old_center[0],
                                  center[1] - old_center[1])
                if dist < best_dist:
                    best_idx, best_dist = idx, dist

            if best_idx is not None and best_dist <= self.max_distance:
                updated[object_id] = centers[best_idx]
                self.missing[object_id] = 0
                assigned.add(best_idx)
            else:
                self.missing[object_id] = self.missing.get(object_id, 0) + 1
                if self.missing[object_id] <= self.max_missing:
                    updated[object_id] = old_center

        for idx, center in enumerate(centers):
            if idx not in assigned:
                updated[self.next_id] = center
                self.missing[self.next_id] = 0
                self.next_id += 1

        self.objects = updated
        self.missing = {k: v for k, v in self.missing.items() if k in updated}
        return dict(self.objects)
