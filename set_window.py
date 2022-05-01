import cv2
import numpy as np

global RECORDING

def img_show(*frame):
    mat = np.zeros((800,1920,3),dtype=np.uint8)
    if len(frame)>6:
        print("Too many frame show!")
        return False
    else:
        dst = []
        for i in range(len(frame)):
            dst.append(cv2.resize(frame[i],(640,400)))
        for i in range(len(dst)):
            if (i+1)>3:
                h = 400
            else:
                h= 0
            w = 0 + 640*((i)%3)
            try:
                mat[h:400+h,w:w+640] = dst[i]
            except:a
                mat[h:400+h,w:w+640] = cv2.cvtColor(dst[i],cv2.COLOR_GRAY2BGR)
        cv2.imshow("Result",mat)
        return True