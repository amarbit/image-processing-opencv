
Image Gradients and Laplacian

Concept: Gradients capture directional changes; Laplacian highlights regions of rapid intensity change.

Visualization: Two windows: gradient magnitude and Laplacian edge-like map.

Practice Exercise: Try ksize=5 for Sobel and Laplacian to see smoothing effect.

Real-world Application: Feature detection, focus metrics, and edge-based segmentation.


import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
mag = cv2.convertScaleAbs(cv2.magnitude(grad_x, grad_y))
lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
lap = cv2.convertScaleAbs(lap)

cv2.imshow("Gradient Magnitude", mag)
cv2.imshow("Laplacian", lap)
cv2.waitKey(800)


cv2.destroyAllWindows()
