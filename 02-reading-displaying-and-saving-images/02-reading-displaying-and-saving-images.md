### Reading, Displaying, and Saving Images

**Concept**: Read images from disk, show them in a window, and save results to files.

**Hands-on Code Example**:
```python
import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


print("Loaded image shape:", img.shape)
cv2.imshow("Original", img)
cv2.waitKey(500)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(500)

out_path = sample_path.replace(".png", "_gray.png")
cv2.imwrite(out_path, gray)
print("Saved:", out_path)


cv2.destroyAllWindows()
```

**What you will see**: Two windows briefly: original color image and its grayscale version.

**Practice exercise**: Save the color image as JPEG and compare file size to PNG.

**Real-world application**: Saving intermediate results is common in preprocessing pipelines and datasets.
