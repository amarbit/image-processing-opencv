
Project: Building a Simple Object Tracker

Concept: Track a colored object using HSV thresholding and contour centroid tracking.

Visualization: The object centroid marked with a red dot and its motion trail; mask view beside it.

Practice Exercise: Add a bounding box and display its area as text.

Real-world Application: Ball tracking in sports, simple robotics following a colored beacon.


import cv2
import numpy as np

cap = cv2.VideoCapture(0)
use_synth = False
if not cap.isOpened():
    use_synth = True

lower = np.array([20, 100, 100])  # example: yellow-ish
upper = np.array([35, 255, 255])

trail = []
while len(trail) < 100:
    if use_synth:
        frame = np.zeros((360, 640, 3), dtype=np.uint8)
        cx = 50 + (len(trail) * 5) % 540
        cy = 180
        cv2.circle(frame, (cx, cy), 20, (0, 255, 255), -1)
    else:
        ret, frame = cap.read()
        if not ret:
            break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.medianBlur(mask, 7)
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if cnts:
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            trail.append((cx, cy))
            cv2.circle(frame, (cx, cy), 8, (0, 0, 255), -1)

    for i in range(1, len(trail)):
        cv2.line(frame, trail[i-1], trail[i], (0, 0, 255), 2)

    cv2.imshow("Tracker (HSV mask on color)", np.hstack([frame, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)]))
    if cv2.waitKey(30) & 0xFF == 27:
        break

if not use_synth:
    cap.release()
cv2.destroyAllWindows()
