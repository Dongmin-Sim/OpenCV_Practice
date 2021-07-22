import sys
import cv2
import numpy as np


oldx = oldy = -1


def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        cv2.circle(img, (x, y), 4, (0, 0, 255), -1)
        cv2.imshow('img', img)
        print('EVENT_LBUTTONDOWN : {}, {}'.format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP : {}, {}'.format(x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        # flags 를 사용할 때는 & 연산자를 사용한다.
        if flags & cv2.EVENT_FLAG_LBUTTON:
            print('EVENT_MOUSEMOVE : {}, {}'.format(x, y))
            # cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imshow('img', img)
            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('img')

# 윈도우가 지정된 이후에 작성해야 함.
cv2.setMouseCallback('img', on_mouse)

cv2.imshow('img', img)
cv2.waitKey()

cv2.destroyAllWindows()
