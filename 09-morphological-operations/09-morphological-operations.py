
Morphological Operations (Erosion, Dilation, Opening, Closing)

Concept: Morphology modifies shapes in binary images; erosion shrinks, dilation grows objects.

Visualization: Binary versus morphology outcomes on synthetic shapes.

Practice Exercise: Try an elliptical kernel via cv2.MORPH_ELLIPSE.

Real-world Application: Clean up noise and fill gaps in segmentation masks.


import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

eroded = cv2.erode(binary, kernel, iterations=1)
dilated = cv2.dilate(binary, kernel, iterations=1)
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Binary", binary)
cv2.imshow("Eroded", eroded)
cv2.imshow("Dilated", dilated)
cv2.imshow("Opened", opened)
cv2.imshow("Closed", closed)
cv2.waitKey(1000)


cv2.destroyAllWindows()
