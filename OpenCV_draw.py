import cv2
import numpy as np

img = np.full((500, 500, 3), 255, dtype=np.uint8)
cv2.imwrite('black_500.jpg', img)


# 직선 그리기
img = cv2.imread('black_500.jpg')

cv2.line(img, (50, 50), (150, 50), (255, 0, 0))  # 파색 1 px 선
cv2.line(img, (200, 50), (300, 50), (0, 255, 0))  # 초록색 1 px 선
cv2.line(img, (350, 50), (450, 50), (0, 0, 255))  # 빨간색 1 px 선

cv2.line(img, (100, 100), (400, 100), (255, 255, 0), 10)  # 하늘색 10 px 선
cv2.line(img, (100, 150), (400, 150), (255, 0, 255), 10)  # 분홍색 10 px 선

cv2.line(img, (100, 350), (400, 400), (0, 0, 255), 20, cv2.LINE_4)  # 4연결선
cv2.line(img, (100, 400), (400, 450), (0, 0, 255), 20, cv2.LINE_8)  # 8연결선
cv2.line(img, (100, 450), (400, 500), (0, 0, 255), 20, cv2.LINE_AA)  # 안티에일리어싱 선

cv2.line(img, (0, 0), (500, 500), (0, 0, 255))  # 대각선 그리기

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 사각형 그리기
img = cv2.imread('black_500.jpg')

cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0))  # 좌상, 우하 좌표로 사각형 그리기
cv2.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 10)  # 우하, 좌상 좌표로 사각형 그리기
cv2.rectangle(img, (450, 200), (200, 450), (0, 0, 255), -1)  # 우상, 좌하 좌표로 사각형 채워 그리


cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
