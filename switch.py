import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("Trackbar")
def nothing(x):
    print(x)

cv2.createTrackbar('B','Trackbar',0,255,nothing)
cv2.createTrackbar('G','Trackbar',0,255,nothing)
cv2.createTrackbar('R','Trackbar',0,255,nothing)

switch="0:OFF\n 1:ON"
cv2.createTrackbar(switch,'Trackbar',0,1,nothing)


while (1):

    cv2.imshow("Trackbar",img)

    k=cv2.waitKey(1) & 0xff
    if k==27:
        break

    b=cv2.getTrackbarPos('B','Trackbar')
    g=cv2.getTrackbarPos('G','Trackbar')
    r=cv2.getTrackbarPos('R','Trackbar')
    switchVal= cv2.getTrackbarPos(switch,'Trackbar')

    if switchVal==0:
        img[:]=0
    else:
         img[:]=[b,g,r]




   


cv2.destroyAllWindows()