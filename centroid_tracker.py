"""Basic nearest-centroid tracker foundation; not a production tracker."""
from math import hypot

class CentroidTracker:
    def __init__(self, max_distance=60.0, max_missing=8):
        if max_distance <= 0 or max_missing < 0:
            raise ValueError("max_distance must be positive and max_missing non-negative")
        self.max_distance = float(max_distance)
        self.max_missing = int(max_missing)
        self.next_id = 1
        self.objects = {}
        self.missing = {}

    @staticmethod
    def _center(box):
        x1, y1, x2, y2 = box
        return ((float(x1) + float(x2)) / 2, (float(y1) + float(y2)) / 2)

    def update(self, boxes):
        centers = [self._center(b) for b in boxes]
        candidates = []
        for oid, old in self.objects.items():
            for i, center in enumerate(centers):
                d = hypot(center[0] - old[0], center[1] - old[1])
                if d <= self.max_distance:
                    candidates.append((d, oid, i))
        candidates.sort()
        result, used_ids, used_indices = {}, set(), set()
        for _, oid, i in candidates:
            if oid not in used_ids and i not in used_indices:
                result[oid] = centers[i]
                used_ids.add(oid)
                used_indices.add(i)
        for i, center in enumerate(centers):
            if i not in used_indices:
                result[self.next_id] = center
                self.next_id += 1
        new_missing = {}
        for oid, old_center in self.objects.items():
            if oid not in used_ids:
                count = self.missing.get(oid, 0) + 1
                if count <= self.max_missing:
                    new_missing[oid] = count
                    result[oid] = old_center
        self.objects, self.missing = result, new_missing
        return dict(self.objects)
