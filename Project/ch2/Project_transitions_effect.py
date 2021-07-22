import sys
import cv2
import numpy as np

cap1 = cv2.VideoCapture('ch2/video1.mp4')
cap2 = cv2.VideoCapture('ch2/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('Video load failed!')
    sys.exit()

# 두 동영상의 크기, FPS같다고 가정
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)

print('Frame_cnt1 : ', frame_cnt1)
print('Frame_cnt2 : ', frame_cnt2)
print('Fps : ', fps)

delay = int(1000/fps)

# 출력 동영상 정보
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('ch2/project_output.avi', fourcc, fps, (w, h))

# 동영상 합성
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    out.write(frame1)

    cv2.imshow('frame', frame1)
    cv2.waitKey(delay)

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # 합성
    dx = int((w * i) / effect_frames)

    # # 새로운 프레임에서 두 프레임을 dx를 기준으로 겹쳐서 사용함.
    # frame = np.zeros((h, w, 3), dtype=np.uint8)
    # frame[:, 0:dx] = frame2[:, 0:dx]
    # frame[:, dx:w] = frame1[:, dx:w]

    # 디졸브 효과
    alpha = 1.0 - i / effect_frames
    frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha, 0)

    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)


for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        break

    out.write(frame2)

    cv2.imshow('frame', frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
