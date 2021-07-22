import sys
import cv2

cap = cv2.VideoCapture('ch2/video1.mp4')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # edge 탐지 함수
    edge = cv2.Canny(frame, 50, 150)

    fps = str(cap.get(cv2.CAP_PROP_FPS))
    cv2.putText(frame, fps, (50, 50),
                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
    # cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    if cv2.waitKey(240) == 27:  # esc
        break

cap.release()
cv2.destroyAllWindows()
