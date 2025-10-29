
Project: Real-time Edge Detection with Webcam

Concept: Use your webcam stream and apply Canny in real time with trackbars to tune thresholds.

Visualization: Window with original frame and dynamic edge map; sliders control thresholds.

Practice Exercise: Add a GaussianBlur before Canny controlled by a trackbar for kernel size.

Real-world Application: Interactive parameter tuning for vision prototyping.


import cv2
import numpy as np

cap = cv2.VideoCapture(0)
use_synth = False
if not cap.isOpened():
    use_synth = True

def nothing(x):
    pass

cv2.namedWindow("Edges")
cv2.createTrackbar("T1", "Edges", 50, 500, nothing)
cv2.createTrackbar("T2", "Edges", 150, 500, nothing)

for i in range(120):
    if use_synth:
        frame = np.zeros((360, 640, 3), dtype=np.uint8)
        cv2.putText(frame, f"Synth {i}", (200, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    else:
        ret, frame = cap.read()
        if not ret:
            break

    t1 = cv2.getTrackbarPos("T1", "Edges")
    t2 = cv2.getTrackbarPos("T2", "Edges")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, max(1, t1), max(1, t2))
    cv2.imshow("Edges", np.hstack([frame, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)]))
    if cv2.waitKey(1) & 0xFF == 27:
        break

if not use_synth:
    cap.release()
cv2.destroyAllWindows()
