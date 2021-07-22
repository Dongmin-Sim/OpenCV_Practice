import sys
import cv2

img = cv2.imread('ch2/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('img load failed!')
    sys.exit()


cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    key = cv2.waitKey()
    if key == 27:
        break
    if key == ord('i') or key == ord('I'):
        img = ~img
        cv2.imshow('image', img)


cv2.destroyAllWindows()
