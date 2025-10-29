### Bitwise Operations and Masking

**Concept**: Masks select regions. Bitwise ops combine images based on masks.

**Hands-on Code Example**:
```python
import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


h, w = img.shape[:2]
mask = np.zeros((h, w), dtype=np.uint8)
cv2.circle(mask, (w//2, h//2), min(h, w)//4, 255, -1)

masked = cv2.bitwise_and(img, img, mask=mask)
inv = cv2.bitwise_not(img)

cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked)
cv2.imshow("Bitwise NOT (invert)", inv)
cv2.waitKey(800)


cv2.destroyAllWindows()
```

**What you will see**: A circular region of the image kept, rest black; and inverted colors.

**Practice exercise**: Create a rectangular mask and combine with the circular one (AND).

**Real-world application**: Region-of-interest selection, alpha compositing, background removal.
