import cv2
import numpy as np

# 관심 영역(Region Of Interest, ROI) 지정

img = cv2.imread('img/man1.jpg')

x = 1500
y = 2250
w = 70
h = 70  # roi 좌표

roi = img[y:y+h, x:x+w]  # roi 지정
img2 = roi.copy()  # roi 복제

print(roi.shape)
cv2.rectangle(roi, (0, 0), (h-1, w-1), (255, 0, 0))
cv2.imshow('img1', img)
cv2.imshow('img2', img2)  # img2 출력
cv2.waitKey(0)
cv2.moveWindow('img', 0, 0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 마우스로 관심영역 지정 함수

isDragging = False  # 마우스 드래그 상태 저장
x0, y0, w, h = -1, -1, -1, -1  # 영역 선택 좌표 저장
blue, red = (255, 0, 0), (0, 0, 255)  # 색상 값


def onMouse(event, x, y, flags, param):  # 마우스 이벤트 핸들 함수
    global isDragging, x0, y0, img
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼을 눌렀을 경우, 드래그 시작
        isDragging = True  # 마우스 드래그 상태 = True
        x0 = x  # x0 에 현재 마우스 클릭 위치의 x 좌표 저장
        y0 = y  # y0 에 현재 마우스 클릭 위치의 y 좌표 저장
    elif event == cv2.EVENT_MOUSEMOVE:  # event 가 마우스 움직이는 이벤트와 동일할 때,
        if isDragging:  # isDragging 가 True 라면
            img_draw = img.copy()  # 사각형 그림 표현을 위한 이미지 복제
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)  # 드래그 진행 영역 사각형으로 표시
            cv2.imshow('img', img_draw)   # 사각형으로 표시된 그림 화면 출력
    elif event == cv2.EVENT_LBUTTONUP:  # event 가 왼쪽 마우스 버튼업일 때,
        if isDragging:
            isDragging = False  # 드래그 False 값으로 지정
            w = x - x0  # 드래그 영역 폭 계산
            h = y - y0  # 드래그 영역 높이 계산
            print("x:{}, y:{}, w:{}, h{}".format(x0, y0, w, h))
            if w > 0 and h > 0:  # 폭(x - x0)과 높이(y - y0)가 음수이면 드래그 방향이 옳음
                img_draw = img.copy()  # 선택 영역에 사각형 그림을 표시할 이미지 복제
                # 선택 영역에 빨간색 사각형 표시
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)  # 빨간색 사각형이 그려진 이미지 화면 출력
                roi = img[y0:y0+h, x0:x0+w]  # 원본 이미지에서 선택 영역만 ROI 로 지정
                cv2.imshow('cropped', roi)  # ROI 지정 영역을 새 창으로 표시
                cv2.moveWindow('cropped', 0, 0)  # 새 창을 화면 좌측 상단으로 이동
                cv2.imwrite('img/cropped.jpg', roi)  # ROI 영역만 파일로 저장
                print('crop complete.')
            else:
                cv2.imshow('img', img)
                print("좌측 상단에서 우측 하단으로 영역을 드래그 해주세요.")


img = cv2.imread('img/man1.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)  # 마우스 이벤트 등록
cv2.waitKey()
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 마우스로 관심영역 지정 함수(OpenCV3 selectROI)

img = cv2.imread('img/man1.jpg')

x, y, w, h = cv2.selectROI('selectROI', img, False)  # 창의 이름 / ROI 선택을 진행할 이미지, 선택영역 중심에 십자 모양 표시 여부

if w and h:
    roi = img[y : y+h, x : x+w]
    cv2.imshow('cropped', roi)
    cv2.moveWindow('cropped', 0, 0)
    cv2.imwrite('img/cropped2.jpg', roi)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(x, y, w, h)
