import sys
import cv2

cap = cv2.VideoCapture(0)
# cap.open(0)

if not cap.isOpened():
    print('camera open failed!')
    sys.exit()

# 프레임 가로, 세로 크기 받아오기
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

# 프레임 가로, 세로 크기 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #
    edge = cv2.Canny(frame, 50, 150)

    fps = str(cap.get(cv2.CAP_PROP_FPS))
    cv2.putText(frame, fps, (50, 50),
                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
    # cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    if cv2.waitKey(20) == 27:  # esc
        break

cap.release()
cv2.destroyAllWindows()
