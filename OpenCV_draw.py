import cv2
import numpy as np

img = np.full((500, 500, 3), 255, dtype=np.uint8)
cv2.imwrite('black_500.jpg', img)
