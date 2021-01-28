import cv2

# 이미지 읽는 법
img_file = 'img/man1.jpg'  # 표시할 이미지 경로
img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당

if img is not None:
    cv2.imshow('IMG', img)  # 읽은 이미지를 화면에 표시
    cv2.waitKey()  # 키가 입력될 때까지 대기
    cv2.destroyAllWindows()  # 창 모두 닫기(설정하지 않으면 강제종료해야 합니다.)
else:
    print('NO IMAGE FILE')

# -----------------------------------------------------------------------------

# 그레이 색상으로 불러온 후 저장하는 법
save_file = 'img/man1_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # 컬러옵션, cv2.IMREAD_GRAYSCALE 그레이 색상으로 불러오는 인자값
cv2.imshow(img_file, img)

cv2.imwrite(save_file, img)  # 파일로 저장, 포맷을 확장자에 따름

cv2.waitKey()
cv2.destroyAllWindows()

# -----------------------------------------------------------------------------

# 동영상 및 카메라 프레임 읽기
video_file = 'video/samplevideo.mov'  # 동영상 파일 경로
cap = cv2.VideoCapture(video_file)  # 동영상 캡처 객체 생성자 (file_path, index) 파일 경로 혹은 카메라 장치번호

if cap.isOpened():  # 캡처 객체 초기화 확인 | return : True/False
    while True:
        ret, img = cap.read()  # 다음 프레임 읽기 | return : Boolean 변수 & 프레임 이미지 Numpy 배열을 쌍으로 갖는 튜플
        if ret:  # ret=True/False 값(초기화 여부) | 프레임 읽기 True 이면
            cv2.imshow(video_file, img)  # 화면에 표시(창 이름, 프레임)
            cv2.waitKey(25)  # 25ms 지연 (40fps 로 가정)
        else:  # 프레임 읽기 False 이면 납(장치의 문제가 있거나, 파일의 끝에 도달함)
            break  # 반복문 나가기

else:
    print("can't open video.")  # 캡처 객체 초기화 실패
cap.release()  # 캡처 자원 반
cv2.destroyAllWindows()

# -----------------------------------------------------------------------------

# 카메라(웹캠) 프레임 읽기

cap = cv2.VideoCapture(0)  # 0번 카메라 장치 연결
if cap.isOpened():
    while True:
        ret, img = cap.read()  # 카메라 프레임 읽기 | return : Boolean 변수 & 프레임 이미지 Numpy 배열을 쌍으로 갖는 튜플
        if ret:
            cv2.imshow('camera', img)  # 프레임 이미지 표시
            if cv2.waitKey(1) != -1:  # 1ms 동안 키 입력 대기 | return : 지정한 대기 시간동안 키 입력이 없으면 -1
                break  # 키 입력이 들어오면 반복문 중지
        else:
            print('no frame')
            break
else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows()

# -----------------------------------------------------------------------------

# OpenCV 카메라 비디오 속성 제어, fps, delay
video_file = 'video/samplevideo.mov'  # 동영상 파일 경로

cap = cv2.VideoCapture(video_file)  # 동영상 캡쳐 객체 생성
if cap.isOpened():  # 캡쳐 객체 초기화 확인
    fps = cap.get(cv2.CAP_PROP_FPS)  # 해당 속성(fps)의 값을 받아오기
    delay = int(1000/fps)  # 지연 시간 구하기
    print("FPS : %f, Delay : %dms" % (fps, delay))

    while True:
        ret, img = cap.read()  # 카메라 프레임 읽기 | return : Boolean 변수 & 프레임 이미지 Numpy 배열을 쌍으로 갖는 튜플
        if ret:  # 프레임 읽기가 정상이라면
            cv2.imshow(video_file, img)  # 화면에 표시
            cv2.waitKey(delay)  # fps 에 맞게 시간 지연
        else:
            break  # 프레임 읽기 실패, 다음 프레임 읽을 수 없음, 재생 완료
else:
    print("can't open video.")  # 캡처 객체 초기화 실패
cap.release()  # 캡처 자원 반납
cv2.destroyAllWindows()  # 창 닫기

# -----------------------------------------------------------------------------

# OpenCV 카메라 속성 제어, width, height 조절 (프레임 크기 재지정)
cap = cv2.VideoCapture(0)  # 카메라 0번 장치 연결 | 동영상 파일에 프레임 크기를 재지정하는 것은 적용되지 않

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 프레임 가로, 폭 값 속성 받아오기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 프레임 세로, 높이 값 속성 받아오기

print("Original width : %d, height : %d" % (width, height))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # 프레임 가로, 폭 값 320 으로 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # 프레임 세로, 높이 값을 240으로 설정
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 재지정한 프레임 가로, 폭 값 속성 받아오기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 재정한 프레임 세로, 높이 값 속성 받아오기

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

# -----------------------------------------------------------------------------

# OpenCV 비디오 파일 저장하기 1 (프레임 저장)
cap = cv2.VideoCapture(0)  # 0번 카메라 연결
if cap.isOpened():
    while True:
        ret, frame = cap.read()  # 카메라 프레임 읽기
        if ret:
            cv2.imshow('camera', frame)  # 프레임 화면에 표시
            if cv2.waitKey(1) != -1:  # 아무키나 누르면
                cv2.imwrite('img/capture.jpg', frame)  # 해당 프레임을 img 폴더의 'capture,jpg' 로 저장
                break
        else:
            print("no frame")
            break
else:
    print("no camera!")

cap.release()
cv2.destroyAllWindows()

# -----------------------------------------------------------------------------

# OpenCV 비디오 파일 저장하기 2 (영상 저장)
cap = cv2.VideoCapture(0)  # 0번 카메라 연결
if cap.isOpened():
    file_path = "video/recode.mov"  # 저장할 파일 경로 이름
    fps = 25.40  # fps, 초당 프레임 수 변수 생성
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # 인코딩 포맷 문자 (mov - mp4v)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))  # 프레임 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size)  # VideoWriter 객체 생성

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recoding', frame)
            out.write(frame)  # 파일 저장
            if cv2.waitKey(int(1000/fps)) != -1:  # 아무키나 누르면
                break  # 저장
        else:
            print("no frame!")
            break
    out.release()  # VideoWriter 객체 자원 반납
else:
    print("can't open camera")

cap.release()  # 캡처 자원 반납
cv2.destroyAllWindows()  # 창 닫기
