from cv2 import cv2
import numpy as np

def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame, dimensions)


def tanslate(img, x, y):
    trans_matrix = np.float([1,0,x],[0,1,y])

    #width, height
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, trans_matrix, dimensions)


def draw_rectangle(img, x, y, width, height):
    cv2.rectangle(img, (x,y), (x+width,y+height), (0,255,0), thickness=2)
    #print("done")

