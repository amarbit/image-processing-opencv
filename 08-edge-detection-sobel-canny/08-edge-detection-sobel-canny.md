### Edge Detection (Sobel, Canny)

**Concept**: Edges are rapid intensity changes. Sobel computes gradients; Canny provides robust edges.

**Hands-on Code Example**:
```python
import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.convertScaleAbs(cv2.magnitude(sobelx, sobely))
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("Sobel Magnitude", sobel)
cv2.imshow("Canny", canny)
cv2.waitKey(800)


cv2.destroyAllWindows()
```

**What you will see**: Two windows: Sobel gradient magnitude and crisp Canny edges.

**Practice exercise**: Lower Canny thresholds to detect more edges (and noise).

**Real-world application**: Feature extraction and object boundary detection.
