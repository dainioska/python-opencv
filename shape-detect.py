import cv2 
import numpy as np 

img = cv2.imread("shapes.png",cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_COMPLEX

for cnt in contours:
    #cv2.drawContours(img, [cnt], 0, (0), 5)
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = (approx.ravel()[0])
    y = (approx.ravel()[1])
    
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x ,y), font, 1, (0))
    elif len(approx) ==4:
        cv2.putText(img, "Reactangle", (x ,y), font, 1, (0))
    elif len(approx) ==5:
        cv2.putText(img, "Pentagon", (x ,y), font, 1, (0))
    elif len(approx) < 15:
        cv2.putText(img, "Ellipse", (x ,y), font, 1, (0))
    else:
        cv2.putText(img, "Circle", (x ,y), font, 1, (0))
        
        
        







cv2.imshow("shapes", img)
cv2.imshow('Treshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
