import cv2
import numpy as np
from canny import *
from roi import *
from line import *
from showline import *


#print(cv2.__version__) check cv2 version ->test version is 4.5.5


#이미지 가져오기
image = cv2.imread('img/sample1.jpg')
lanelines_image = image.copy()

# Canny Edge Processing
#흰 검으로 변환해서 라인 검출함.
canny_conversion = canny_edge(lanelines_image)
roi_conversion = reg_of_interest(canny_conversion)

#interim check img conversion
cv2.imshow('Caany', canny_conversion)
cv2.imshow('Canny_roi', roi_conversion)
cv2.waitKey()
cv2.destroyAllWindows()

#라인 이어주기
lines = cv2.HoughLinesP(roi_conversion, 1, np.pi/180, 100, minLineLength = 40, maxLineGap = 5)
averaged_lines = average_slope_intercept(lanelines_image, lines)

#선을 기울기 평균값으로 적용
lines_image = show_lines(lanelines_image, averaged_lines)

#원본 이미지에 라인 그리기
combine_image = cv2.addWeighted(lanelines_image, 0.8, lines_image, 1, 1)

cv2.imshow('ori', lanelines_image)
cv2.imshow("roi", lines_image)
cv2.imshow("combined", combine_image)
cv2.waitKey()
cv2.destroyAllWindows()