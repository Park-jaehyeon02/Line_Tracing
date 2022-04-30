#-*-coding:CP949-*-

import cv2
import datetime

class recorder:
    def __init__(self,file_name,frame):
        fourcc = cv2.VideoWriter_fourcc(*'FMP4')
        self.video = cv2.VideoWriter("C:/Users/박재현\source/repos/Park-jaehyeon02/Line_Tracing/video/"+str(datetime.datetime.now().strftime("%d_%H-%M-%S"))+file_name+".mp4",fourcc,20.0,(frame.shape[1],frame.shape[0]))

    def write(self,frame):
        self.video.write(frame)

    def release(self):
        self.video.release()