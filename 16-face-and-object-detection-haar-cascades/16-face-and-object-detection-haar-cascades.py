"""
Face and Object Detection Basics (using Haar cascades)

Concept: Haar cascades are classic detectors trained on features; fast but less robust than modern CNNs.

Visualization: A window with rectangles if any faces are detected (synthetic image likely none).

Practice Exercise: Load a real photo with a face and run detection on it.

Real-world Application: Access control, photo tagging, and driver monitoring.
"""

import cv2
import numpy as np

# We will use a synthetic image if no webcam is available; for real testing, use your webcam.
img = np.full((400, 600, 3), 220, dtype=np.uint8)
cv2.putText(img, "Face Demo", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)

# Load a built-in Haar cascade if available
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Haar Cascade Faces", img)
cv2.waitKey(800)
cv2.destroyAllWindows()

