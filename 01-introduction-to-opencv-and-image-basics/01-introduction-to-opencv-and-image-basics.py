
Introduction to OpenCV and Image Basics

Concept: OpenCV is a popular open-source library for computer vision. An image is a grid of pixels; color images typically have 3 channels (B, G, R) in OpenCV.

Visualization: A 3x3 image scaled up showing distinct blue, green, red squares.

Practice Exercise: Change the pixel at (2,2) to yellow (BGR: 0,255,255) and re-run.

Real-world Application: Understanding pixels/channels underlies all vision tasks like filtering and detection.


import cv2
import numpy as np

# Create a tiny synthetic image to demonstrate pixel access
img = np.zeros((3, 3, 3), dtype=np.uint8)
img[0, 0] = (255, 0, 0)  # Blue in BGR
img[0, 1] = (0, 255, 0)  # Green
img[0, 2] = (0, 0, 255)  # Red

print("Image shape:", img.shape)  # (H, W, C)
print("Top-left pixel (B, G, R):", img[0, 0])

# Resize for visualization
big = cv2.resize(img, (300, 300), interpolation=cv2.INTER_NEAREST)
cv2.imshow("Intro: Pixels (BGR)", big)
cv2.waitKey(1000)
cv2.destroyAllWindows()
