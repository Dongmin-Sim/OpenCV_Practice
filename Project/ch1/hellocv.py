import sys
import cv2


# opencv 버전확인
print('opencv version : ', cv2.__version__)

# 이미지 불러와 변수에 담기
img = cv2.imread('images/ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)

# 이미지 로드에 실패했을 경우 에러메세지 출력, interpreter 종료
if img is None:
    print('Image load failed')
    sys.exit()

# 그레이스케일의 img 저장
cv2.imwrite('cat_gray.png', img)

# 윈도우 창 생성, 윈도우에 이미지 띄우기, 이미지 holding
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

# 특정 키 입력될때까지 waitKey하기
while True:
    if cv2.waitKey() == ord('q'):
        break

# 창 닫기
cv2.destroyAllWindows()
