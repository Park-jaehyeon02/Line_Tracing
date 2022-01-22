import cv2
import numpy as np
from canny import *
from roi import *
from line import *
from showline import *
from color import *

#print(cv2.__version__) check cv2 version ->test version is 4.5.5

print("Loading......")
cap = cv2.VideoCapture('./video/test1.mp4')
print("Finish Video Loading!")

while True:
    retval, frame = cap.read() # frame capture
    if not retval:
        break
    
    #original frame
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('frame', 0, 0) 
    cv2.resizeWindow('frame', 680, 400)
    cv2.imshow('frame',frame)

    #ROI Setting
    cv2.imshow('roi',reg_of_interest(frame))

    #yellow, white detected frame
    white_frame,yellow_frame = color_detection(frame)
    cv2.namedWindow('white', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('white', 0, 400) 
    cv2.resizeWindow('white', 680, 400)
    cv2.namedWindow('yellow', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('yellow', 1360, 0) 
    cv2.resizeWindow('yellow', 680, 400)
    cv2.imshow('white',white_frame)
    cv2.imshow('yellow',yellow_frame)

    # white & yellow mask frame
    detected_frame = color_add(yellow_frame,white_frame)
    masked_frame = cv2.bitwise_and(frame,frame, mask = detected_frame)
    cv2.namedWindow('mask_frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('mask_frame', 680, 400) 
    cv2.resizeWindow('mask_frame', 680, 400)
    cv2.imshow('mask_frame',masked_frame)

    #Canny Edge and Gaussian Filtering
    canny_frame,dcanny = canny_edge(masked_frame)
    cv2.namedWindow('double_canny_frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('double_canny_frame', 680, 0) 
    cv2.resizeWindow('double_canny_frame', 680, 400)
    cv2.imshow('double_canny_frame',dcanny)
    #cv2.imshow('one canny',canny_frame)

    #


    key = cv2.waitKey(25)
    if key == 27:
        break


#if real cam is operated,Turn off cam
if cap.isOpened():
    cap.release()
#cv windows delete
cv2.destroyAllWindows()

