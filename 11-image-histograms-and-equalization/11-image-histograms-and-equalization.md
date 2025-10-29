### Image Histograms and Equalization

**Concept**: Histograms show pixel intensity distribution; equalization improves contrast.

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
hist = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()
eq = cv2.equalizeHist(gray)

# Simple plot-free visualization: stack histogram as bars into an image
import numpy as np
hist_img = np.full((200, 256, 3), 255, dtype=np.uint8)
cv2.normalize(hist, hist, 0, 200, cv2.NORM_MINMAX)
for x, v in enumerate(hist.astype(int)):
    cv2.line(hist_img, (x, 199), (x, 199 - v), (0, 0, 0), 1)

cv2.imshow("Gray", gray)
cv2.imshow("Equalized", eq)
cv2.imshow("Histogram (visual)", hist_img)
cv2.waitKey(1000)


cv2.destroyAllWindows()
```

**What you will see**: Grayscale vs equalized image and a simple histogram image.

**Practice exercise**: Equalize only the Y channel in YCrCb for color images.

**Real-world application**: Enhancing low-contrast photos, medical images, and OCR preprocessing.
