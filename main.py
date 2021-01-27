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
            cv2.waitKey(16)
        else:
            break

else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()


# 카메라(웹캠) 프레임 읽기

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
            break
else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows()

# OpenCV 카메라 비디오 속성 제어, fps, delay
video_file = 'video/samplevideo.mov'

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    print("FPS : %f, Delay : %dms" % (fps, delay))

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()


# OpenCV 카메라 비디오 속성 제어, width, height 조절
cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Original width : %d, height : %d" % (width, height))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Resize width : %d, height : %d" % (width, height))

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('Mac camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print("no frame!")
            break
else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()
