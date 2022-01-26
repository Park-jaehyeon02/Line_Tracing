import cv2
import numpy as np
import math

#except inclination
slope_threshold = 0.3

def line_error(img):
    text="Not Found Line!" 
    dst = img.copy()
    org=(int(img.shape[1]/3),int(img.shape[0]/2)) 
    font=cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(dst,text,org,font,2,(0,0,255),5)
    return dst

#To test all lines func 
def draw_line(img,lines):
    dst = img.copy()
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            cv2.line(dst,(x1,y1),(x2,y2),(0,255,255),2)
    return dst

#Real active func
def draw_line2(img,lines):
    dst = img.copy()
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            cv2.line(dst,(x1,y1),(x2,y2),(255,0,255),3)
    return dst

def separate_line(lines,width):
    del_list = []
    #check slope
    for i in range(len(lines)):
        x1 = lines[i][0][0]
        y1 = lines[i][0][1]
        x2 = lines[i][0][2]
        y2 = lines[i][0][3]
        if x2-x1 != 0:
            slope = math.sqrt((y2 - y1)**2 / (x2 - x1)**2)
        if (x2-x1) == 0:
            pass
        elif slope_threshold > slope:
            del_list.append(i)
    cnt=0
    for i in del_list:
        lines = np.delete(lines,i-cnt,axis=0)
        cnt += 1
    right_line = np.empty((0,1,4), int)
    left_line = np.empty((0,1,4), int)
    for i in range(len(lines)):
        x1 = lines[i][0][0]
        x2 = lines[i][0][2]
        if (x1+x2)/2 > width/2:
            right_line = np.append(right_line,[lines[i]],axis=0)
        else:
            left_line = np.append(left_line,[lines[i]],axis=0)
    return right_line, left_line, lines

def fit_line(r_lines,l_lines): 
    r_lines = np.squeeze(r_lines)
    r_lines = r_lines.reshape(r_lines.shape[0]*2,2)
    print(r_lines)
    """
    r_line = []
    l_line = []
    print('r',r_lines)
    print('l',l_lines)
    for i in range(len(r_lines)):
        x1 = r_lines[i][0][0]
        y1 = r_lines[i][0][1]
        x2 = r_lines[i][0][2]
        y2 = r_lines[i][0][3]
        r_line.append([x1,y1,x2,y2])
    for i in range(len(l_lines)):
        x1 = l_lines[i][0][0]
        y1 = l_lines[i][0][1]
        x2 = l_lines[i][0][2]
        y2 = l_lines[i][0][3]
        l_line.append([x1,y1,x2,y2])
    print('r',r_line[0])
    print('l',l_line)
    """
    r_lines = cv2.fitLine(r_lines[0],cv2.DIST_L2,0,0.01,0.01,line = None)
    l_lines = cv2.fitLine(l_lines,cv2.DIST_L2,0,0.01,0.01)
    return r_lines,l_lines
