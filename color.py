import cv2

white_lower = (130,130,130)
white_upper = (255,255,255)
yellow_lower = (10,100,100)
yellow_upper = (40,255,255)

def color_detection(frame):
    whilte_frame = cv2.inRange(frame,white_lower,white_upper)
    yellow_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    yellow_frame = cv2.inRange(yellow_frame,yellow_lower,yellow_upper)
    return whilte_frame,yellow_frame

def color_add(yellow,white):
    dst1= cv2.bitwise_or(yellow,white)
    return dst1