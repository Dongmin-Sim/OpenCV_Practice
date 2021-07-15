from matplotlib import cm
import matplotlib.pyplot as plt
import cv2

# matplot으로 컬러 영상 출력 , BGR -> RGB 변환
imgBGR = cv2.imread('ch01/cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# matplot으로 그레이 영상 출력
imgGray = cv2.imread('images/ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
