import numpy as np
import cv2

img=cv2.imread("cat.jpg")

_,th1=cv2.threshold(img, 120,255,cv2.THRESH_BINARY)#This is the type of thresholding to apply. In binary thresholding, each pixel in the image is converted to either 0 or the maximum value (255) based on the threshold value.
_,th2=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV) 
_,th3=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)#This is the type of thresholding to apply. In truncation thresholding, any pixel value above the threshold value is set to the threshold value, and all other pixel values remain unchanged.
_,th4=cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
cv2.imshow("Image",th1)
cv2.imshow("Image2",th2)
cv2.imshow("Image3",th3)
cv2.imshow("Imag4",th4)

b,g,r= cv2.split(img)

_,b_th=cv2.threshold(b,120,255,cv2.THRESH_BINARY)
_,g_th=cv2.threshold(g,120,255,cv2.THRESH_BINARY)
_,r_th=cv2.threshold(r,120,255,cv2.THRESH_BINARY)

merged_channel=cv2.merge([b_th,g_th,r_th])
cv2.imshow("merged_image",merged_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()