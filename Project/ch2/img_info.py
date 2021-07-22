import sys
import cv2

img_dir = 'cat.bmp'

img1 = cv2.imread(img_dir, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img_dir, cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed')
    sys.exit()


# imread로 불러온 값의 타입 == ndarry
print(type(img1))

# imread로 불러오느 값의 형태 == tuple(h, w, c)
print((img1.shape))
print((img2.shape))

# dtype는 uint8 형식
print((img1.dtype))
print((img2.dtype))

h, w = img1.shape
print('w * h = {} * {}'.format(w, h))

h, w = img2.shape[:2]
print('w * h = {} * {}'.format(w, h))


if img1.ndim == 2:
    print('img1 is a grayscale image')
elif img2.ndim == 3:
    print('img2 is a color image')

# 영상의 픽셀 값
x = 20
y = 10

# 그레이스케일 영상의 픽셀값
pixel = img1[y, x]
print(pixel)

# 컬러 영상의 필셀값
pixel = img2[y, x]
print(pixel)

# 픽셀값 처리
img1[y, x] = 0
img2[y, x] = [0, 0, 0]


# 영상 로드
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
