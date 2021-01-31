import cv2
import numpy as np

img = np.full((500, 500, 3), 255, dtype=np.uint8)
cv2.imwrite('black_500.jpg', img)

# ----------------------------------------------------------------------
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

# ----------------------------------------------------------------------
# 사각형 그리기
img = cv2.imread('black_500.jpg')

cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0))  # 좌상, 우하 좌표로 사각형 그리기
cv2.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 10)  # 우하, 좌상 좌표로 사각형 그리기
cv2.rectangle(img, (450, 200), (200, 450), (0, 0, 255), -1)  # 우상, 좌하 좌표로 사각형 채워 그리


cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ----------------------------------------------------------------------
# 원, 타원, 호 그리기

img = cv2.imread('black_500.jpg')

# 원중심 (150, 150), 반지름 100
cv2.circle(img, (150, 150), 100, (255, 0, 0))
# 원중심 (300, 150), 반지름 70
cv2.circle(img, (300, 150), 70, (0, 255, 0), 5)
# 원중심 (400, 150), 반지름 50 색상 채우기
cv2.circle(img, (400, 150), 50, (0, 0, 255), -1)

# 원중심 (100, 300), 반지름(50), 기준 축 회전 각도 0, 0도부터 360도 그리기
cv2.ellipse(img, (50, 300), (50, 50), 0, 0, 360, (0, 0, 255))
# 원중심 (200, 300), 반지름(50), 기준 축 회전 각도 0, 0도부터 180도 그리기
cv2.ellipse(img, (200, 300), (50, 50), 0, 0, 180, (255, 0, 0))
# 원중심 (300, 300), 반지름(50), 기준 축 회전 각도 0, 181도부터 360도 그리기
cv2.ellipse(img, (250, 300), (50, 50), 0, 181, 360, (0, 0, 255))

# 원중심(50, 425), 반지름(50, 75), 회전 15도
cv2.ellipse(img, (50, 425), (50, 75), 15, 0, 180, (0, 0, 255))
# 원중심(200, 425), 반지름(50 75), 회전 45도
cv2.ellipse(img, (200, 425), (50, 75), 45, 0, 360, (0, 0, 0))

cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ----------------------------------------------------------------------
# 글씨그리기

img = cv2.imread('black_500.jpg')

cv2.putText(img, "PLAIN", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
cv2.putText(img, "SIMPLEX", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
cv2.putText(img, "DUPLEX", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))

cv2.putText(img, "SIMPLEX * 2", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 250))
cv2.putText(img, "COMPLEX_SMALL", (200, 110), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))

# 이 코드는 폰트를 함께 사용하는 방법입니다.
cv2.putText(img, "PLAIN | ITALIC", (50, 430), cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0, 0, 0))
cv2.putText(img, "COMPLEX | ITALIC", (50, 470), cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0, 0, 0))

cv2.imshow('Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
