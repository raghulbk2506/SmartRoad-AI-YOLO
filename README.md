# SmartRoad AI 🚗🅿️🚦
## AI-Based Roadside Parking and Traffic Congestion Detection

A student prototype combining a web dashboard with actual vehicle detection using Python, OpenCV, and YOLO.

## Features
- YOLO vehicle detection
- Car, motorcycle, bus and truck filtering
- Bounding-box visualization
- Configurable roadside parking zone
- Prototype parking-zone occupancy detection
- LOW / MEDIUM / HIGH congestion estimation
- Annotated output video
- JSON processing summary
- Interactive web dashboard

## Quick Start
```bash
python -m venv .venv
pip install -r requirements.txt
```

Add a permitted road video as `data/road.mp4`, then:
```bash
python ai/detect.py --source data/road.mp4
```

Webcam:
```bash
python ai/detect.py --source 0 --show
```

Outputs are saved in `outputs/`.

## Project structure
```text
SmartRoad-AI-YOLO/
├── ai/
│   ├── detect.py
│   ├── test_installation.py
│   └── README.md
├── data/
│   └── README.md
├── docs/
│   ├── problem-statement.md
│   ├── ai-ideation.md
│   ├── user-testing.md
│   └── technical-architecture.md
├── prototype/
├── index.html
├── style.css
├── script.js
├── requirements.txt
└── README.md
```

## Limitations
This is an academic prototype. Current congestion uses per-frame vehicle counts, and parking-zone detection checks whether a vehicle centre is inside a configured zone. A production system should add object tracking, calibration, privacy safeguards, and human review.
