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

# 프레임 폭, 높이 설정 (but error 발생)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

if cap.isOpened():
    ret, a = cap.read()  # a 프레임 읽기
    ret, b = cap.read()  # b 프레임 읽기

    while ret:  # c 프레임 읽기
        ret, c = cap.read()  # 출력 영상에 사용할 복제본
        draw = c.copy()
        if not ret:  # ret(초기화 여부) 이 True 가 아니면 반복문 밖으로
            break

        # 3개의 영상을 그레이 스케일로 변경 (BGR -> GRAY)
        a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

        # a-b, b-c 절대 값 차이 구하기
        diff_ab = cv2.absdiff(a_gray, b_gray)
        diff_bc = cv2.absdiff(b_gray, c_gray)

        # 스레스 홀드로 tresh 이내의 차이는 무시(감도 설정)
        ret, diff_ab_t = cv2.threshold(diff_ab, thresh, 225, cv2.THRESH_BINARY)
        ret, diff_bc_t = cv2.threshold(diff_bc, thresh, 255, cv2.THRESH_BINARY)

        # 두 차이에 대해서 AND 연산, 두 영상의 차이가 모두 발견된 경우
        diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)

        # 열림 연산으로 노이즈 제거 (미세한 노이즈를 제거하는 코드)
        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

        # 차이가 발생한 픽셀의 갯수가 max_diff 보다 많은 경우 사각형 및 문구 표시
        diff_cnt = cv2.countNonZero(diff)
        if diff_cnt > max_diff:
            nzero = np.nonzero(diff)  # 0이 아닌 픽셀의 좌표 얻기
            cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])), (max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)
            cv2.putText(draw, "motion detected.", (10, 50), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))

        # 컬러 스케일 영상과 스레시 홀드 영상을 통합해서 출력
        stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
        cv2.imshow('motion sensor', stacked)

        # 다음 비교를 위해 영상 순서 정리
        a = b
        b = c

        if cv2.waitKey(1) & 0xFF == 27:  # esc 를 누르면 종료
            break
