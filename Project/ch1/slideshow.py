import sys
import os
import cv2
import glob

files = os.listdir('ch1/images/')
img_files = [file for file in files if file.endswith('.jpg')]

# img_files = glob.glob('.\\images\\*.jpg')

for f in img_files:
    print(f)

cv2.namedWindow('slideshow', cv2.WINDOW_NORMAL)
cv2.setWindowProperty(
    'slideshow', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread('ch1/images/' + img_files[idx])

    if img is None:
        print('Image load failed')
        break

    cv2.imshow('slideshow', img)

    if cv2.waitKey(1000) == 27:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
