import cv2
import numpy as np

#except inclination
slope_threshold = 0.3

def line_error(img):
    text="Not Found Line!" 
    org=(int(img.shape[1]/3),int(img.shape[0]/2)) 
    font=cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(img,text,org,font,2,(0,0,255),5)
    return img

def draw_line(img,lines):
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,255),2)
    return img

def draw_line2(img,lines):
    print(lines,type(lines))
    x1,y1,x2,y2 = lines
    print(x1,y1,x2,y2)
    cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
    return img

def separate_line(lines):
    for i in range(len(lines)):

    return 
    
