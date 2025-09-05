import cv2
import numpy as np

print("Testing OpenCV in-memory operations...")
print("OpenCV version:", cv2.__version__)

# Create the green square that worked before
img = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(img, (20, 20), (80, 80), (0, 255, 0), 2)

print("✅ Green square created!")
print("Image shape:", img.shape)
print("Test passed! 🎉")