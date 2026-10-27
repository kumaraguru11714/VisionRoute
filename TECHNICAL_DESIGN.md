# VisionRoute — Technical Design Document

## 1. Objective
Demonstrate camera-based recognition of selected everyday objects and spoken alerts in a controlled environment.

## 2. Architecture
`Camera/Webcam → OpenCV frame capture → YOLO object detector → label/confidence filter → rough bounding-box heuristic → text-to-speech → system audio output`

A Bluetooth headset or speaker may be used when paired and selected as the operating system's audio output. Bluetooth connectivity is handled by the operating system; this prototype does not directly manage Bluetooth pairing.

## 3. Components
- **Input:** laptop/USB webcam.
- **Image handling:** OpenCV captures video frames.
- **Inference:** Ultralytics YOLO small pretrained model identifies common object classes.
- **Decision logic:** selected labels are filtered by confidence; bounding-box area is used only as a rough visual heuristic.
- **Output:** pyttsx3 speaks an alert through the default audio device.
- **Configuration:** environment variables for camera index and confidence threshold.

## 4. Data flow
1. Read a frame from the camera.
2. Run object detection.
3. Filter detections to labels supported by the demo.
4. Draw detections and show the live preview.
5. If a detected object's box occupies a large fraction of the frame, issue a rate-limited spoken warning.
6. Continue until the user presses `q`.

## 5. Limitations and risk controls
Bounding-box size is not a true distance measurement. The model is not trained or validated for safe navigation. It may miss obstacles, confuse objects, or fail in poor lighting. It cannot guarantee detection of stairs, holes, drop-offs, glass, or fast-moving traffic. Do not use it as a replacement for a cane or guide dog. Test only in safe, controlled settings with a helper.

## 6. Future improvements
- Add a calibrated depth sensor or validated depth-estimation component.
- Add dedicated detection for stairs, drop-offs, and road hazards.
- Evaluate latency, precision, recall, false alerts, and missed hazards using an approved dataset.
- Conduct accessibility testing with informed consent and safety supervision.
- Add privacy controls and avoid storing camera frames by default.
