import cv2
import numpy as np

'''
<motion_detection 프로그램>
카메라 영상의 차영상으로 움직임을 감지하고 움직임이 있는 영역을 표시하는 프로그램입니다. 

<개요>
세 프레임 a, b, c 를 순차적으로 얻어서 a, b의 차이 b, c의 차이가 모두 발견되는 경우에 한해서 움직임을 판단합니다.
따라서 각 프레임의 차이가 특정 기준치 보다 많은 경우에 움직임이 있는 것으로 간주합니다.

<기준치>
설치된 환경과 카메라 품질에 따라 조정
'''

# 감도 설정 (카메라 품질에 따라 조정필요)
thresh = 55  # 달라진 픽셀 값 기준치 설정 / 움직임 감도
max_diff = 22  # 달라진 픽셀 갯수 기준치 설정

# 카메라 캡션 장치 준비
a, b, c = None, None, None
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()

    while ret:
        ret, c = cap.read()
        draw = c.copy()
        if not ret:
            break

        a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

        diff_ab = cv2.absdiff(a_gray, b_gray)
        diff_bc = cv2.absdiff(b_gray, c_gray)

        ret, diff_ab_t = cv2.threshold(diff_ab, thresh, 225, cv2.THRESH_BINARY)
        ret, diff_bc_t = cv2.threshold(diff_bc, thresh, 255, cv2.THRESH_BINARY)

        diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)

        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

        diff_cnt = cv2.countNonZero(diff)
        if diff_cnt > max_diff:
            nzero = np.nonzero(diff)
            cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])), (max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)
            cv2.putText(draw, "motion detected.", (10, 50), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))

        stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
        cv2.imshow('motion sensor', stacked)

        a = b
        b = c

        if cv2.waitKey(1) & 0xFF == 27:
            break
