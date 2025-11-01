"""
Perspective Transform and Affine Transform

Concept: Affine preserves parallelism; perspective handles keystoning (4-point warps).

Visualization: One image sheared (affine) and another with a perspective warp.

Practice Exercise: Use 4 corner points to rectify a tilted rectangle back to fronto-parallel.

Real-world Application: Document scanning, homography, and AR overlays.
"""

import cv2
import numpy as np

# Ensure we have a sample image to work with
sample_path = r"C:\python\image-processing-opencv\tutorials\assets\sample_synthetic.png"
img = cv2.imread(sample_path)
if img is None:
    raise RuntimeError("Failed to load synthetic sample image.")


h, w = img.shape[:2]

# Affine transform: shear/rotate via 3 points
src_aff = np.float32([[0, 0], [w-1, 0], [0, h-1]])
dst_aff = np.float32([[0, 0], [int(0.8*(w-1)), 50], [50, int(0.9*(h-1))]])
M_aff = cv2.getAffineTransform(src_aff, dst_aff)
aff = cv2.warpAffine(img, M_aff, (w, h))

# Perspective transform using 4 points
src = np.float32([[50,50],[w-50,50],[50,h-50],[w-50,h-50]])
dst = np.float32([[10,70],[w-60,20],[60,h-40],[w-20,h-10]])
M_p = cv2.getPerspectiveTransform(src, dst)
persp = cv2.warpPerspective(img, M_p, (w, h))

cv2.imshow("Affine", aff)
cv2.imshow("Perspective", persp)
cv2.waitKey(800)


cv2.destroyAllWindows()

