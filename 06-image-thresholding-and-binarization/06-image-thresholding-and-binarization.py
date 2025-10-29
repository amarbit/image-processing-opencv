
Image Thresholding and Binarization

Concept: Convert grayscale images to binary using fixed or adaptive thresholds.

Visualization: Four windows comparing gray vs different binarization results.

Practice Exercise: Try inverse binary threshold (cv2.THRESH_BINARY_INV).

Real-world Application: Document scanning and segmentation of foreground from background.


import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th_fixed = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
th_adapt_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 11, 2)
th_adapt_gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Gray", gray)
cv2.imshow("Fixed Threshold", th_fixed)
cv2.imshow("Adaptive Mean", th_adapt_mean)
cv2.imshow("Adaptive Gaussian", th_adapt_gauss)
cv2.waitKey(1000)


cv2.destroyAllWindows()
