import cv2

def canny_edge(image) :
    gray_conversion = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_conversion = cv2.GaussianBlur(gray_conversion, (5,5), 0)
    canny_conversion = cv2.Canny(blur_conversion, 50, 150)
    after_blur = cv2.GaussianBlur(canny_conversion, (5,5), 0)
    after_canny = cv2.Canny(after_blur,50,150)
    return canny_conversion,after_blur,after_canny
    