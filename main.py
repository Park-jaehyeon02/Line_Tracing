#-*-coding:CP949-*-

import cv2
import numpy as np
from roi import *
from line import *
from hough import *
from preprocess import *
from record import *
from set_window import *

RECORDING = False
if RECORDING:
    r_fin_frame = True
else:
    r_fin_frame = False



print("Loading......")
cap = cv2.VideoCapture('./video/test2.mp4')
#cap = cv2.VideoCapture(0)
print("Finish Video Loading!")

if not(cap.isOpened()):
    print("Video Loading Error!")


while True:
    retval, frame = cap.read() # frame capture
    if not retval:
        break

    white_frame,yellow_frame = color_detection(frame)

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

    
    if lines is None:
        cv2.imshow('hough_frame',line_error(frame))
    else:
        right_lines , left_lines, lines = separate_line(lines,frame.shape[1])
        cv2.imshow('hough_frame',draw_line2(frame,lines))
        
        #fit right and left line
        cv2.namedWindow('Line_frame', cv2.WINDOW_NORMAL)

        cv2.resizeWindow('Line_frame', 680, 400)
        if right_lines.size < 12 or left_lines.size < 12:
            Fin_frame = line_error(frame)
        else:
           detected_line = fit_line(frame, right_lines , left_lines)
           Fin_frame = draw_line3(frame,detected_line)
        cv2.imshow("Line_frame",Fin_frame)
        img_show(Fin_frame,Fin_frame,Fin_frame,roi_frame,roi_frame)
        #Fin_frame_Recording
        if r_fin_frame:
            Fin_recorder = recorder("Fin_frame",Fin_frame)
            r_fin_frame = False
        
        if RECORDING:
            Fin_recorder.write(Fin_frame)
        
    #End method
    key = cv2.waitKey(25)
    if key == 27:
        break
    


if RECORDING:
    Fin_recorder.release()


if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()

