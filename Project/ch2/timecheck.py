import sys
import numpy as np
import cv2

img = cv2.imread('ch2/hongkong.jpg')

if img is None:
    print('Image load failed')
    sys.exit()

# tickmeter 객체 생성
tm = cv2.TickMeter()

tm.start()  # 시간 측정 시작

edge = cv2.Canny(img, 50, 150)

tm.stop()  # 시간 측정 종료
ms = tm.getTimeMilli()

print('Elapsed time : {}ms'.format(ms))
