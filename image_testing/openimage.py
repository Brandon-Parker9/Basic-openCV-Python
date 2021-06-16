from cv2 import cv2
import random
import numpy as np

img = cv2.imread("Avengers2.jpg")

width = int(img.shape[1]*.5)
height = int(img.shape[0]*.5)

img = cv2.resize(img, (width,height))

# cv2.imshow('Blank', img)

# 2. Draw a Rectangle
cv2.rectangle(img, (0,0), (img.shape[1]//2, img.shape[0]//2), (0,255,0), thickness=2)
# cv2.imshow('Rectangle', img)

# 3. Draw A circle
cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 40, (0,0,255), thickness=1)
# cv2.imshow('Circle', img)

# 4. Draw a line
cv2.line(img, (100,250), (300,400), (255,255,255), thickness=3)
# cv2.imshow('Line', img)

# 5. Write text
cv2.putText(img, 'Hello', (600,225), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv2.imshow('Text', img)

# 6. Crop image
cropped = img[100:200, 0:500]
cv2.imshow("cropped", cropped)

# 7. Flip image 0 - flip image vertically, 1 - flip image horizontally, -1 - flip both directions
flipped = cv2.flip(img,0)
cv2.imshow("flipped", flipped)

testing_img = img

for height in range(1, testing_img.shape[0]):
    for width in range(1, testing_img.shape[1]):
        if (random.randint(0,100) == 34):
            testing_img[height, width] = (255,255,255)


testing_img[0,600] = (255,255,255)

cv2.imshow("tesing image", testing_img)

print(testing_img.shape)
img2 = np.zeros((3,10),dtype = int)
img = ([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]])
#cv2.imshow("black image" , img)
print(img)
print(img2)
cv2.waitKey(0)