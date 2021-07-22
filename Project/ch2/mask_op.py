import cv2

src = cv2.imread('ch2/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('ch2/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('ch2/field.bmp', cv2.IMREAD_COLOR)

# copyto 함수를 사용하는 방법
# cv2.copyTo(src=src, mask=mask, dst=dst)

# 인덱스를 활용하는 방법
dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()


# png 영상 channel이 4개 cv2.IMREAD_UNCHANGED로 불러와야 함.
src = cv2.imread('ch2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:, :, -1]  # 맨 마지막 채널
src = src[:, :, 0:3]
dst = cv2.imread('ch2/field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]

crop = dst[10:h+10, 10:w+10]

cv2.copyTo(src, mask=mask, dst=crop)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.imshow('dst crop', crop)
cv2.waitKey(0)

cv2.destroyAllWindows()
