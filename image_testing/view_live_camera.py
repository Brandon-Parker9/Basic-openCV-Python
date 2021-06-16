from cv2 import cv2
from functions import rescale_frame

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#capture = cv2.VideoCapture("watch.mp4")

# isTrue, frame = capture.read()
# print(isTrue)
# cv2.imshow("frame",frame)

count = 0

while True:
    isTrue, frame = capture.read()
    
    resized = rescale_frame(frame)

    resized = cv2.flip(resized,1)

    cv2.imshow("frame",resized)

    count += 1


    if cv2.waitKey(30) == ord('q') or count == 500:
        break

    if cv2.getWindowProperty('frame',cv2.WND_PROP_VISIBLE) < 1:        
        break  
    


capture.release()

cv2.waitKey(1000)

cv2.destroyAllWindows()