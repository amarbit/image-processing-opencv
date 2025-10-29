
Drawing Shapes and Writing Text on Images

Concept: Draw primitives to annotate results or generate synthetic data.

Visualization: Annotated image with rectangle, filled circle, line, and text.

Practice Exercise: Draw a triangle by connecting three points with lines.

Real-world Application: Visualization of detections, bounding boxes, and labels.


import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


canvas = img.copy()
cv2.rectangle(canvas, (30, 30), (200, 160), (0, 255, 0), 2)
cv2.circle(canvas, (350, 120), 50, (0, 0, 255), -1)
cv2.line(canvas, (50, 300), (550, 350), (255, 255, 0), 3)
cv2.putText(canvas, "Hello OpenCV", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Annotations", canvas)
cv2.waitKey(800)


cv2.destroyAllWindows()
