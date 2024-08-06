import cv2

img=cv2.imread('C:\\Users\\91981\\Desktop\\opencv\\cat.jpg')

def clickEvent(event, x,y,flags,params):
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        if x<img.shape[1] and y<img.shape[0]:
            strBGR=str(blue)+", "+str(green)+", "+str(red)
            cv2.putText(img,strBGR,(x,y),font,0.5,(198,200,123),2)
            
        else:
            cv2.putText(img,"Error",(x,y),font,0.2,(0,0,255),1)
        cv2.imshow("Image",img)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image",clickEvent)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()