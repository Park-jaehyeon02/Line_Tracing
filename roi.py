import numpy as np
import cv2

def reg_of_interest(image) :
    image_height = image.shape[0]
    polygons = np.array( [[ (200, image_height) , (1100, image_height), (550, 250) ]] )
    image_mask = np.zeros_like(image)
    cv2.fillPoly(image_mask, polygons, 255)
    masking_image = cv2.bitwise_and(image, image_mask)
    return masking_image
