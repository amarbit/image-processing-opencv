
Video Processing using OpenCV

Concept: Read frames from a video or webcam, process per-frame, and display.

Visualization: A live window showing original frames and their edge maps side-by-side.

Practice Exercise: Overlay FPS text on frames using moving average timing.

Real-world Application: Dashcams, CCTV analytics, and robotics vision loops.


import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Try default webcam; if not present, fallback to synthetic frames
use_synth = False
if not cap.isOpened():
    use_synth = True

frame_idx = 0
while frame_idx < 60:  # ~2 seconds at 30 FPS
    if use_synth:
        frame = np.zeros((360, 640, 3), dtype=np.uint8)
        cv2.putText(frame, f"Synthetic {frame_idx}", (50, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    else:
        ret, frame = cap.read()
        if not ret:
            break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 160)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    stacked = np.hstack([frame, edges_bgr])
    cv2.imshow("Video | Original | Canny", stacked)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    frame_idx += 1

if not use_synth:
    cap.release()
cv2.destroyAllWindows()
