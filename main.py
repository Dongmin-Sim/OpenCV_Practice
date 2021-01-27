import cv2

img_file = 'img/man1.jpg'
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('NO IMAGE FILE')


# 그레이 색상으로 불러온 후 저장하는 법
save_file = 'img/man1_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # 컬러옵션, cv2.IMREAD_GRAYSCALE 그레이 색상으로 불러오는 인자값
cv2.imshow(img_file, img)

# 파일로 저장, 포맷을 확장자에 따름
cv2.imwrite(save_file, img)

cv2.waitKey()
cv2.destroyAllWindows()

# 동영상 및 카메라 프레임 읽기
video_file = 'video/samplevideo.mov'
cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
        else:
            break

else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()