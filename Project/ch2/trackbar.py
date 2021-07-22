import numpy as np
import cv2


def on_level_changed(pos):
    global img

    level = pos * 16
    level = np.clip(level, 0, 255)

    img[:, :] = level
    cv2.imshow('img', img)


img = np.zeros((480, 640), dtype=np.uint8)

cv2.namedWindow('img')

# 윈도우이름이 지정된 후에 사용해야 함.
cv2.createTrackbar('level', 'img', 0, 16, on_level_changed)

cv2.imshow('img', img)
cv2.waitKey()

cv2.destroyAllWindows()
