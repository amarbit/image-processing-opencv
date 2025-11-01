"""
Contour Detection and Shape Approximation

Concept: Contours trace object boundaries; polygonal approximation simplifies shapes.

Visualization: Edges and simplified polygon contours overlaid in green.

Practice Exercise: Label each contour with the number of vertices.

Real-world Application: Shape analysis, document detection, and object counting.

"""
import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 80, 160)
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

vis = img.copy()
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    cv2.drawContours(vis, [approx], -1, (0, 255, 0), 2)

cv2.imshow("Edges", edges)
cv2.imshow("Contours + Approx", vis)
cv2.waitKey(800)


cv2.destroyAllWindows()

