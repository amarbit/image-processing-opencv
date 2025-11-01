"""
Smoothing and Blurring Techniques

Concept: Reduce noise using averaging, Gaussian, median, and bilateral filters.

Visualization: Side-by-side windows showing different blur effects.

Practice Exercise: Increase kernel sizes to see stronger smoothing.

Real-world Application: Denoising before edge detection or segmentation.
"""

import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


avg = cv2.blur(img, (7, 7))
gauss = cv2.GaussianBlur(img, (7, 7), 1.5)
median = cv2.medianBlur(img, 7)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Original", img)
cv2.imshow("Average Blur", avg)
cv2.imshow("Gaussian Blur", gauss)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral", bilateral)
cv2.waitKey(1000)


cv2.destroyAllWindows()

