from cv2 import cv2
from functions import rescale_frame, draw_rectangle



harr_cascade = cv2.CascadeClassifier('haar_cascade_face.xml')

frame = cv2.imread("group-photo-family-group-outdoors-grass-hill-generations.jpg")
    
# resized = rescale_frame(frame)

# resized = cv2.flip(resized,1)

grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces_rectangles = harr_cascade.detectMultiScale(grey_img)

for (x,y,width,height) in faces_rectangles:
    print(x,y,width,height)
    draw_rectangle(frame,x, y, width, height)

#print(faces_rectangles)

cv2.imshow("frame",frame)


cv2.waitKey(0)

cv2.destroyAllWindows()