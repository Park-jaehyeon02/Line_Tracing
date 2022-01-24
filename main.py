import cv2
import numpy as np
from canny import *
from roi import *
from line import *
from hough import *
from color import *

#print(cv2.__version__) check cv2 version ->test version is 4.5.5

print("Loading......")
cap = cv2.VideoCapture('./video/test1.mp4')
#cap = cv2.VideoCapture(0)
print("Finish Video Loading!")

if not(cap.isOpened()):
    print("Video Loading Error!")



while True:
    retval, frame = cap.read() # frame capture
    if not retval:
        break
    
    #original frame
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('frame', 0, 0) 
    cv2.resizeWindow('frame', 680, 400)
    cv2.imshow('frame',frame)

    #yellow, white detected frame
    white_frame,yellow_frame = color_detection(frame)

    """ To check yellow or white area
    cv2.namedWindow('white', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('white', 1360, 400) 
    cv2.resizeWindow('white', 680, 400)
    cv2.namedWindow('yellow', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('yellow', 1360, 0) 
    cv2.resizeWindow('yellow', 680, 400)
    cv2.imshow('white',white_frame)
    cv2.imshow('yellow',yellow_frame)
    """

    # white & yellow mask frame
    detected_frame = color_add(yellow_frame,white_frame)
    masked_frame = cv2.bitwise_and(frame,frame, mask = detected_frame)
    cv2.namedWindow('mask_frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('mask_frame', 680, 400) 
    cv2.resizeWindow('mask_frame', 680, 400)
    cv2.imshow('mask_frame',masked_frame)

    #Canny Edge and Gaussian Filtering
    #canny_frame,dcanny = canny_edge(masked_frame) test!
    canny = canny_edge(masked_frame)
    cv2.namedWindow('canny_frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('canny_frame', 680, 0) 
    cv2.resizeWindow('canny_frame', 680, 400)
    cv2.imshow('canny_frame',canny)
    #cv2.imshow('one canny',canny_frame)

    #ROI Setting
    roi_frame = reg_of_interest(canny)
    
    #Hough Transform
    lines = houghLines(roi_frame)
    cv2.namedWindow('hough_frame', cv2.WINDOW_NORMAL) 
    cv2.moveWindow('hough_frame', 0, 400) 
    cv2.resizeWindow('hough_frame', 680, 400)
    if lines is None:
        cv2.imshow('hough_frame',line_error(frame))
    else:
        cv2.imshow('hough_frame',draw_line(frame,lines))
        #Average_slope_intercept
        print(lines)
        """lines = separate_line(lines)
        cv2.namedWindow('hough_frame2', cv2.WINDOW_NORMAL)  
        cv2.resizeWindow('hough_frame2', 680, 400)
        cv2.imshow('hough_frame2',draw_line(frame,lines))
        """
    key = cv2.waitKey(25)
    if key == 27:
        break


#if real cam is operated,Turn off cam
if cap.isOpened():
    cap.release()
#cv windows delete
cv2.destroyAllWindows()

