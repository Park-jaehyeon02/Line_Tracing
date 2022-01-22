import cv2
import numpy as np
from matplotlib import pyplot as plt
from canny import *
from roi import *
from line import *
from showline import *
from color import *

#print(cv2.__version__) check cv2 version ->test version is 4.5.5


cap = cv2.VideoCapture('./video/test1.mp4')
print("Wating for a moment.....")

while True:
    retval, frame = cap.read() # frame capture
    if not retval:
        break
    white_frame,yellow_frame = color_detection(frame)
    """ for test detection video
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('frame', 0, 0) 
    cv2.resizeWindow('frame', 680, 400)
    cv2.namedWindow('white', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('white', 0, 400) 
    cv2.resizeWindow('white', 680, 400)
    cv2.namedWindow('yellow', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('yellow', 680, 0) 
    cv2.resizeWindow('yellow', 680, 400)
    cv2.imshow('white',white_frame)
    cv2.imshow('yellow',yellow_frame)
    cv2.imshow('frame',frame)
    """
    key = cv2.waitKey(25)
    if key == 27:
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()

