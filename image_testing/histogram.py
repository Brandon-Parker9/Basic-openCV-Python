from cv2 import cv2
import random
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Avengers2.jpg")

width = int(img.shape[1]*.5)
height = int(img.shape[0]*.5)

img = cv2.resize(img, (width,height))

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circle = np.zeros(img.shape[:2], "uint8")
mask = cv2.circle(circle.copy(), (circle.shape[1]//2+50, circle.shape[0]//2), 50 ,color = 255, thickness=-1)

masked = cv2.bitwise_and(img_grey, img_grey, mask = mask)

hist = cv2.calcHist([img_grey], [0], None, [256], [0,256])

hist2 = cv2.calcHist([img_grey], [0], mask, [256], [0,256])
hist3 = cv2.calcHist([masked], [0], mask, [256], [0,256])

# cv2.imshow("initial", img)
cv2.imshow("Gery Image" ,img_grey)
# cv2.imshow("Mask", mask)
cv2.imshow("Masked", masked)

plt.figure()
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist3)
#plt.plot(hist2)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)