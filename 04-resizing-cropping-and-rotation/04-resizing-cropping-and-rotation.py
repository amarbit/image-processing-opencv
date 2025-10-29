
Image Resizing, Cropping, and Rotation

Concept: Resize to change resolution, crop to focus on regions, rotate for orientation.

Visualization: Four windows: smaller, larger, centered crop, and 30° rotated image.

Practice Exercise: Rotate by -45° and scale by 0.5 at the same time.

Real-world Application: Normalization for model input and data augmentation.


import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


# Resize
small = cv2.resize(img, (300, 200), interpolation=cv2.INTER_AREA)
big = cv2.resize(img, (900, 600), interpolation=cv2.INTER_CUBIC)

# Crop
h, w = img.shape[:2]
crop = img[h//4: h//4 + h//2, w//4: w//4 + w//2]

# Rotate 30 degrees around center
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Resized Small", small)
cv2.imshow("Resized Big", big)
cv2.imshow("Crop", crop)
cv2.imshow("Rotated", rotated)
cv2.waitKey(1000)


cv2.destroyAllWindows()
