"""VisionRoute educational obstacle-awareness prototype.

Safety note: This is not a certified mobility aid. Never rely on it as the
sole means of navigation. Use only in a safe, controlled test environment.
"""
import os
import time
import cv2
import pyttsx3
from ultralytics import YOLO

CAMERA_INDEX = int(os.getenv("VISIONROUTE_CAMERA_INDEX", "0"))
CONFIDENCE = float(os.getenv("VISIONROUTE_CONFIDENCE", "0.45"))
MODEL_NAME = "yolov8n.pt"
ALERT_COOLDOWN_SECONDS = 3.0

# COCO classes likely to be useful in a basic demo. This is not a complete
# hazard list; the model may miss hazards or classify them incorrectly.
INTERESTING_LABELS = {
    "person", "bicycle", "car", "motorcycle", "bus", "truck",
    "chair", "bench", "potted plant", "dog", "cat", "suitcase",
    "backpack", "handbag", "bottle", "dining table"
}

def rough_visual_proximity(box, frame_width, frame_height):
    """Return a rough alert only; bbox size is not a reliable distance measure."""
    x1, y1, x2, y2 = box
    area_ratio = max(0, x2 - x1) * max(0, y2 - y1) / float(frame_width * frame_height)
    if area_ratio > 0.22:
        return "possibly close"
    if area_ratio > 0.08:
        return "in view"
    return "farther in view"

def main():
    print("Loading model. The first run may download model weights...")
    model = YOLO(MODEL_NAME)
    speech = pyttsx3.init()
    speech.setProperty("rate", 165)

    camera = cv2.VideoCapture(CAMERA_INDEX)
    if not camera.isOpened():
        raise RuntimeError(
            f"Could not open camera index {CAMERA_INDEX}. Check webcam permissions "
            "or set VISIONROUTE_CAMERA_INDEX to another index."
        )

    last_alert_at = {}
    print("VisionRoute running. Press 'q' in the video window to quit.")
    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Camera frame unavailable.")
                break

            results = model.predict(frame, conf=CONFIDENCE, verbose=False)
            annotated = frame.copy()
            now = time.time()

            for result in results:
                if result.boxes is None:
                    continue
                names = result.names
                for detected_box in result.boxes:
                    class_id = int(detected_box.cls[0].item())
                    label = names.get(class_id, str(class_id))
                    confidence = float(detected_box.conf[0].item())
                    if label not in INTERESTING_LABELS:
                        continue

                    x1, y1, x2, y2 = map(int, detected_box.xyxy[0].tolist())
                    proximity = rough_visual_proximity(
                        (x1, y1, x2, y2), frame.shape[1], frame.shape[0]
                    )
                    cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 220, 0), 2)
                    cv2.putText(
                        annotated, f"{label} {confidence:.2f} - {proximity}",
                        (x1, max(20, y1 - 8)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 220, 0), 2
                    )

                    # Only announce likely-close objects; this is a rough demo heuristic.
                    if proximity == "possibly close" and now - last_alert_at.get(label, 0) >= ALERT_COOLDOWN_SECONDS:
                        message = f"{label} detected, possibly close. Please check your surroundings."
                        print(message)
                        speech.say(message)
                        speech.runAndWait()
                        last_alert_at[label] = time.time()

            cv2.imshow("VisionRoute - prototype (press q to quit)", annotated)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
        try:
            speech.stop()
        except Exception:
            pass

if __name__ == "__main__":
    main()
