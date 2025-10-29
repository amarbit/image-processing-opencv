### Color Spaces (BGR, RGB, Grayscale, HSV, LAB)

**Concept**: Color can be represented in multiple spaces. HSV separates color (hue) from intensity. LAB approximates human perception.

**Hands-on Code Example**:
```python
import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow("BGR", img)
cv2.imshow("RGB", cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV (visualized as BGR)", cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))
cv2.imshow("LAB (visualized as BGR)", cv2.cvtColor(lab, cv2.COLOR_LAB2BGR))
cv2.waitKey(1000)


cv2.destroyAllWindows()
```

**What you will see**: Multiple windows: same scene rendered via different color conversions.

**Practice exercise**: Extract the S (saturation) channel from HSV and display it.

**Real-world application**: HSV helps with color-based segmentation under lighting changes.
