# SmartRoad AI — Next Review

Additional code and documentation for the next review.

## Files
- `ai/config.py` — shared detection settings
- `ai/centroid_tracker.py` — lightweight tracking foundation
- `ai/analytics.py` — congestion classification and summary helpers
- `ai/test_analytics.py` — standard-library unit tests
- `docs/technical-improvements.md` — improvements and limitations
- `CHANGELOG.md` — review-stage change log

## Test
From this folder run: `python -m unittest discover -s ai -p "test_*.py" -v`

These are additions, not yet integrated into the original `ai/detect.py` pipeline. Validate them with real road footage before making performance claims.
