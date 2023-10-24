import cv2
import numpy as np




def emp(a):
    pass
cv2.namedWindow("bar")
cv2.resizeWindow("bar" , 640 , 240)
cv2.createTrackbar("hue min" , "bar" , 0 , 179 , emp)
cv2.createTrackbar("hue max" , "bar" , 179 , 179 , emp)
cv2.createTrackbar("sat min" , "bar" , 0 , 255 , emp)
cv2.createTrackbar("sat max" , "bar" , 255 , 255 , emp)
cv2.createTrackbar("val min" , "bar" , 0 , 255 , emp)
cv2.createTrackbar("val max" , "bar" , 255 , 255 , emp)
while True:
    img = cv2.imread("benz.jpg")
    img = cv2.resize(img , (300 , 200))
    h_min = cv2.getTrackbarPos("hue min" , "bar")
    h_max = cv2.getTrackbarPos("hue max" , "bar")
    s_min = cv2.getTrackbarPos("sat min" , "bar")
    s_max = cv2.getTrackbarPos("sat max" , "bar")
    v_min = cv2.getTrackbarPos("val min" , "bar")
    v_max = cv2.getTrackbarPos("val max" , "bar")
    print(h_min , h_max , s_min , s_max , v_min , v_max)
    hsvimg = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    lower  = np.array([h_min , s_min , v_min])
    upper  = np.array([h_max , s_max , v_max])
    mask = cv2.inRange(hsvimg , lower , upper)
    imgresult = cv2.bitwise_and(img , img , mask=mask)
    cv2.imshow("img" , img)
    cv2.imshow("hsvimg" , hsvimg)
    cv2.imshow("mask" , mask)
    cv2.imshow("result" , imgresult)
    if cv2.waitKey(1) & 0xFF ==ord(' '):
         cv2.destroyAllWindows()
         break
