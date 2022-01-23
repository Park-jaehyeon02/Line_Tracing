import cv2
import numpy as np
Rho = 1 # 0~1 r value(real)
Theta = np.pi / 180 #0~180 theta value
Threshold = 20 #meet point number
MinLineLength = 10 
MaxLineGap = 20 #Between Lines,Max Gap limit

def houghLines(edges):
    lines = cv2.HoughLinesP(edges, Rho, Theta , 10, None, 20, 2)
    return lines