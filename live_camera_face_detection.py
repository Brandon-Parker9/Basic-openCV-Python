from cv2 import cv2
from functions import rescale_frame, draw_rectangle

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#capture = cv2.VideoCapture("watch.mp4")

# isTrue, frame = capture.read()
# print(isTrue)
# cv2.imshow("frame",frame)

count = 0

harr_cascade = cv2.CascadeClassifier('haar_cascade_face.xml')

while True:
    isTrue, frame = capture.read()
    
    resized = rescale_frame(frame)

    resized = cv2.flip(resized,1)

    grey_img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    faces_rectangles = harr_cascade.detectMultiScale(grey_img)

    for (x,y,width,height) in faces_rectangles:
        print(x,y,width,height)
        draw_rectangle(resized,x, y, width, height)

    #print(faces_rectangles)

    cv2.imshow("frame",resized)

    count += 1


    if cv2.waitKey(30) == ord('q') or count == 500:
        break

    if cv2.getWindowProperty('frame',cv2.WND_PROP_VISIBLE) < 1:        
        break  
    


capture.release()

cv2.waitKey(1000)

cv2.destroyAllWindows()