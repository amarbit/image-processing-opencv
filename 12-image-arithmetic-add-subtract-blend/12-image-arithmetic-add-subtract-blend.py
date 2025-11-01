"""
Image Arithmetic (Add, Subtract, Blend)

Concept: Combine images through addition, subtraction, and weighted blending.

Visualization: Original + a red disk image; show added, subtracted, and blended outcomes.

Practice Exercise: Try different alpha/beta weights in addWeighted.

Real-world Application: Image compositing, exposure fusion, and change detection.
"""

import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


h, w = img.shape[:2]
other = np.zeros_like(img)
cv2.circle(other, (w//2, h//2), min(h, w)//4, (0, 0, 255), -1)

added = cv2.add(img, other)
sub = cv2.subtract(img, other)
blend = cv2.addWeighted(img, 0.7, other, 0.3, 0)

cv2.imshow("Original", img)
cv2.imshow("Other", other)
cv2.imshow("Added", added)
cv2.imshow("Subtracted", sub)
cv2.imshow("Blended", blend)
cv2.waitKey(1000)


cv2.destroyAllWindows()

