import cv2

img=cv2.imread("C:\\Users\\91981\\Desktop\\opencv\\cat.jpg")
cv2.imshow("Image", img)


def clickEvent(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        strXY= str(x)+" "+str(y)
        cv2.putText(img,strXY, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
        cv2.imshow("Image",img)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image",clickEvent)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

