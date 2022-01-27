import numpy as np
import cv2

def reg_of_interest(image) :
    image_height = image.shape[0]
    image_width = image.shape[1]
    polygons = np.array( [[ (int(image_width/4), int(image_height*2/3)) , (int(image_width*3/4), int(image_height*2/3)), (int(image_width*5/6), image_height),(int(image_width/6),image_height) ]] )
    image_mask = np.zeros_like(image)
    cv2.fillPoly(image_mask, polygons, (255,255,255))
    #image_mask = cv2.cvtColor(image_mask,cv2.COLOR_BGR2GRAY)
    image_mask = cv2.threshold(image_mask,100,255,cv2.THRESH_BINARY)
    image_mask2 = image_mask[1]
    masking_image = cv2.bitwise_and(image,image, mask = image_mask2)
    return masking_image
