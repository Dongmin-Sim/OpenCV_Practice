import cv2
import numpy as np
import matplotlib.pyplot as plt

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

#------------------------------------------------------------------
#컬러스페이스 RGB, BGR, RGBA
img = cv2.imread('img/cropped.jpg')  # 기본 값 옵션
bgr = cv2.imread('img/cropped.jpg', cv2.IMREAD_COLOR)  # IMREAD_COLOR 옵션
bgra = cv2.imread('img/cropped.jpg', cv2.IMREAD_UNCHANGED)

# 각 옵션에 따른 이미지 SHAPE
print("default : ", img.shape, "color : ", bgr.shape, "unchanged : ", bgra.shape)

cv2.imshow('bgr', bgr)
cv2.imshow('bgra', bgra)
cv2.imshow('alpha', bgra[:,:,2])  # 알파 채널만 표시

cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 컬러스페이스 변환
img = cv2.imread('img/cropped.jpg')
img2 = img.astype(np.uint16)  # dtype 변경
b, g, r = cv2.split(img)  # 채널별로 분리
gray1 = ((b+g+r)/3).astype(np.uint8)  # 평균값 연산 후 dtype 변경

gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 스레스 홀딩 (threshold return 값으로 경계값, 스레스홀딩된 바이너리 이미지)

img = cv2.imread('img/gray_gradient.jpg')
value = 127

# 1. Numpy API로 바이너리 이미지 만들기
thresh_np = np.zeros_like(img)
thresh_np[img > 127] = 255

# 2. OpenCV API 로 바이너리 이미지 만들기
ret, thresh_cv = cv2.threshold(img, value, 255, cv2.THRESH_BINARY)  # 변환할 이미지, 경계값, 픽셀에 적용할 값(value), 경계값을 넘으면 value 넘지 못하면 0
print('thresh_binary value : ', ret)  # 127.0 바이너리 이미지에 사용된 값 반환

# 2-1 다양한 바이너리 이미지
_, t_biniv = cv2.threshold(img, value, 255, cv2.THRESH_BINARY_INV)
_, t_trunc = cv2.threshold(img, value, 255, cv2.THRESH_TRUNC)
_, t_tozero = cv2.threshold(img, value, 255, cv2.THRESH_TOZERO)
_, t_tozero_inv = cv2.threshold(img, value, 255, cv2.THRESH_TOZERO_INV)

# 3. 원본과 결과물 출력
imgs = {'Original':img, 'Numpy API':thresh_np, 'cv2.threshold':thresh_cv, 'cv2.BINARY_INV':t_biniv, 'cv2.TRUNC':t_trunc, 'cv2.TOZERO':t_tozero, 'cv2.TOZERO_INV':t_tozero_inv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(3, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]), plt.yticks([])
plt.show()

# ------------------------------------------------------------------
# 오츠의 알고리즘

# 이미지를 그레이 스케일로 읽기
img = cv2.imread('img/receipt.jpg', cv2.IMREAD_GRAYSCALE)

# 경계값을 80/100/130/170으로 지정
_, t_80 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
_, t_100 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
_, t_170 = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)

# 경계값을 지정하지 않고 OTSU 알고리즘 선택
ret, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold : ', ret)

imgs = {
    'Original':img,
    't:80': t_80,
    't:100':t_100,
    't:130':t_130,
    't:170':t_170,
    'otsu:%d'%ret:t_otsu
}

# 원본과 결과물 출력
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()

# ------------------------------------------------------------------
# 적응형 스레시 홀드

blk_size = 9  # 블럭 사이즈
C = 5  # 차감 상수
img = cv2.imread('img/receipt.jpg', cv2.IMREAD_GRAYSCALE)  # gray_scale 로 읽기

# 1. 오츠의 알고리즘으로 단일 경계 값을 전체 이미지에 적용
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 2. adaptive threshold 를 평균과 가우시안 분포로 각각 적용
# adaptiveThreshold(입력 영상, 조건 맞는 픽셀에 적용할 값, 스레시홀드 적용방법 지정과(이웃픽셀평균 or 가우시안 분포에 따른 가중치의 합), 영역으로 나눌 이웃의 크기(홀수), 계산된 경계값 결에서 가감할 상수)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

# 3. 결과를 출력
imgs = {'Original':img, "Global-Otus:%d"%ret:th1, 'Adapted-Mean':th2, 'Adapted-Gaussian':th3}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.title(k)
    plt.imshow(v, 'gray')
    plt.xticks([]), plt.yticks([])

plt.show()

# ------------------------------------------------------------------
# 알파 블랜딩 (일반적인 덧셈 활용)

# 1. 연산에 사용할 이미지 읽기
img1 = cv2.imread('img/man1.jpg')
img2 = cv2.imread('img/man1_gray.jpg')

# 2. 이미지 덧셈
img3 = img1 + img2
img4 = cv2.add(img1, img2)

imgs = {'im1':img1, 'im2':img2, 'img3':img3, 'img4':img4}

# 3. 이미지 출력
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(value[:, :, ::-1])
    plt.title(key)
    plt.xticks([]); plt.yticks([])
plt.show()

# ------------------------------------------------------------------
# 알파 블랜딩(알파값 사용)
alpha = 0.5

# 1. 합성에 사용할 이미지 읽기
img1 = cv2.imread('img/man1.jpg')
img2 = cv2.imread('img/man1_gray.jpg')

# 2. 수식을 직접 연산해서 알파 블랜딩 적용
blened = img1 * alpha + img2 * (1-alpha)
blened = blened.astype(np.uint8)
cv2.imshow('img * alpha + img2 * (1-alpha)', blened)

# 3. 함수를 활용한 방법
dst = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
cv2.imshow('cv2.addWeighted', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 알파 블랜딩-트랙바

# 연산에 사용할 이미지 읽기 (두 이미지의 사이즈가 같아야 함)
img1 = cv2.imread('img/man1.jpg')
img2 = cv2.imread('img/man1_gray.jpg')

win_name = 'Alpha blending'
trackbar_name = 'fade'

def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
    cv2.imshow(win_name, dst)

cv2.imshow(win_name, img1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 차영상

img1 = cv2.imread('img/man1.jpg')
img2 = cv2.imread('img/man1.jpg')
img1_gray = cv2.imread(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.imread(img2, cv2.COLOR_BGR2GRAY)

# 두 사진의 절대값 차이 연산 absdiff 함수
diff = cv2.absdiff(img1_gray, img2_gray)

# 차이를 명확하게 해주는 스레스 홀드 기법 전처리
_, diff = cv2.threshold(diff, 1, 255, cv2.THRESH_BINARY)
diff_red = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
diff_red[:, :, 2] = 0

# 두 번째 이미지에 변화 부분 표시
spot = cv2.bitwise_xor(img2, diff_red)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('diff', diff)
cv2.imshow('spot', spot)
cv2.waitKey()
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 이미지 합성과 마스킹

# 1. 신호등 영상을 읽어서 HSV 로 변환
img = cv2.imread('img/4_color.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2. 색상별 영역 지정
blue1 = np.array([90, 50, 50])
blue2 = np.array([120, 255, 255])
green1 = np.array([45, 50, 50])
green2 = np.array([75, 255, 255])
red1 = np.array([0, 50, 50])
red2 = np.array([15, 255, 255])
red3 = np.array([165, 50, 50])
red4 = np.array([180, 255, 255])
yellow1 = np.array([20, 50, 50])
yellow2 = np.array([35, 255, 255])

# 3. 색상에 따른 마스크 생성
mask_blue = cv2.inRange(hsv, blue1, blue2)
mask_green = cv2.inRange(hsv, green1, green2)
mask_red = cv2.inRange(hsv, red1, red2)
mask_red2 = cv2.inRange(hsv, red3, red4)
mask_yellow = cv2.inRange(hsv, yellow1, yellow2)

# 4. 색상별 마스크로 색상만 추출
res_blue = cv2.bitwise_and(img, img, mask=mask_blue)
res_green = cv2.bitwise_and(img, img, mask=mask_green)
res_red1 = cv2.bitwise_and(img, img, mask_red)
res_red2 = cv2.bitwise_and(img, img, mask_red2)
res_red = cv2.bitwise_or(res_red1, res_red2)
res_yellow = cv2.bitwise_and(img, img, mask=mask_yellow)

# 5. 결과 출력
imgs = {'original': img, 'blue':res_blue, 'green':res_green, 'red':res_red, 'yellow':res_yellow}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(key)
    plt.imshow(value[:, :, ::-1])
    plt.xticks([]); plt.yticks([])
plt.show()

