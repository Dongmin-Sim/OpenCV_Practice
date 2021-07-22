import cv2
import numpy as np

img = np.full((400, 400, 3), 255, dtype=np.uint8)

cv2.line(img, (50, 50), (200, 50), color=(0, 0, 255), thickness=5)
cv2.line(img, (50, 60), (150, 160), color=(0, 0, 128))

# 사각형 그리기
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

# 원 그리기
cv2.circle(img, center=(300, 100), radius=30,
           color=(255, 255, 0), thickness=-1, lineType=cv2.LINE_AA)
cv2.circle(img, center=(300, 100), radius=60,
           color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# 다각형 그리기
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2, cv2.LINE_AA)

# 문자열 출력
text = 'Hello? OpenCV' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_COMPLEX,
            0.8, (255, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
