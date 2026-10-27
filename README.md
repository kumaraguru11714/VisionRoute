# VisionRoute
AI-assisted obstacle awareness prototype for visually impaired users.

## Purpose
VisionRoute uses a camera, an object-detection model, and spoken alerts to help a user notice selected obstacles. This is an educational prototype, not a certified mobility aid. It must not replace a white cane, guide dog, or trained orientation-and-mobility support.

## Features
- Live camera input using OpenCV
- Object detection using a YOLO model from Ultralytics
- Spoken obstacle labels using text-to-speech
- Works with the computer's default audio output; a paired Bluetooth headset/speaker can be selected in the operating system
- Test cases and architecture notes included

## Requirements
- Python 3.10 or 3.11 recommended
- Webcam
- Speakers/headphones (Bluetooth audio can be used if paired and selected as the system output)
- Internet connection for the first model download

## Setup
1. Install Python.
2. Download or clone this repository.
3. Create and activate a virtual environment:
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python src/visionroute.py`
6. Allow camera access if prompted. Press `q` to quit.

## Configuration
The prototype uses the default webcam (`CAMERA_INDEX = 0`) and a small pretrained YOLO model (`yolov8n.pt`). Change these in `src/visionroute.py` if needed. The first run may download model weights.

## Environment variables
No secrets or API keys are required. Optional:
- `VISIONROUTE_CAMERA_INDEX`: camera device index (default `0`)
- `VISIONROUTE_CONFIDENCE`: detection confidence threshold (default `0.45`)

## How it works
The camera frame is passed to YOLO. Detected labels are displayed and announced with a cooldown to avoid repeating the same alert continuously. A bounding-box-size heuristic produces only a rough visual proximity warning; it is not a distance sensor and can be wrong.

## Safety and limitations
- Do not use this prototype as the only navigation aid or test it in traffic, near stairs, or in other hazardous places.
- Detection may fail due to lighting, occlusion, camera angle, model limitations, or hardware performance.
- It does not reliably detect drop-offs, potholes, transparent objects, or all moving hazards.
- Test seated or in a safe, controlled area with a sighted helper.
- This is not a medical device and is not validated for real-world independent navigation.

## Repository contents
- `src/visionroute.py`: prototype source code
- `docs/TECHNICAL_DESIGN.md`: architecture and design
- `docs/TEST_CASES.md`: sample test cases and results template
- `data/sample_scenarios.csv`: scenario dataset for manual testing
- `LICENSE`: MIT License
