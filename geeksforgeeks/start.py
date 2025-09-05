import cv2
import numpy as np

# Create a black image
img = np.zeros((100, 100, 3), dtype=np.uint8)
# Draw a green rectangle
cv2.rectangle(img, (20, 20), (80, 80), (0, 255, 0), 2)

print('Basic OpenCV operations working!')
print('Image shape:', img.shape)
print('OpenCV version:', cv2.__version__)

# Optional: Display the image (will open a window)
cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()