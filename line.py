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

def fit_line(img,r_lines,l_lines): 
    #tranform 4*n mat to 2*2n mat for fitLine func
    r_lines = np.squeeze(r_lines)
    r_lines = r_lines.reshape(r_lines.shape[0]*2,2)
    l_lines = np.squeeze(l_lines)
    l_lines = l_lines.reshape(l_lines.shape[0]*2,2)
    #fitLine Func
    r_lines = cv2.fitLine(r_lines,cv2.DIST_L2,0,0.01,0.01,line = None)
    l_lines = cv2.fitLine(l_lines,cv2.DIST_L2,0,0.01,0.01)
    print(r_lines,l_lines)
    #calculate line x,y points
    r_m = r_lines[1]/r_lines[0]
    l_m = l_lines[1]/l_lines[0]
    r_x , r_y = r_lines[2], r_lines[3]
    l_x , l_y = l_lines[2], l_lines[3]
    y1 = int(img.shape[0])
    y2 = int(img.shape[0]/2)
    rx_line1 = int(((y1-r_y)/r_m)+r_x)
    print(y2,r_y,y2-r_y)
    rx_line2 = int(((y2-r_y)/r_m)+r_x)
    lx_line1 = int(((y1-l_y)/l_m)+l_x)
    lx_line2 = int(((y2-l_y)/l_m)+l_x)

    #return val r,l
    points = []
    points.append([rx_line1,y1,rx_line2,y2])
    points.append([lx_line1,y1,lx_line2,y2])
    print(points)
    return points
