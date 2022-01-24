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
    #check slope
    for i in range(len(lines)):
        print(lines[0][0][1])
        x1 = lines[0][i]
        y1 = lines[1][i]
        x2 = lines[2][i]
        y2 = lines[3][i]
        print(x1)
        if (x2-x1) == 0:
            pass
        elif slope_threshold > abs((y2 - y1) / (x2 - x1)):
            print(abs((y2 - y1) / (x2 - x1))) 
            np.delete(lines, i, axis=0)
     
    return lines
    
