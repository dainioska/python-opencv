import cv2 
import numpy as np 

cap = cv2.VideoCapture(0) 

_, threshold = cv2.threshold(cap, 200, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret ==True:

        for cnt in contours:
            #cv2.drawContours(img, [cnt], 0, (0), 5)
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            cv2.drawContours(img, [approx], 0, (0), 2)
            x = (approx.ravel()[0])
            y = (approx.ravel()[1])
    

        cv2.imshow("shapes", img)
        cv2.imshow('Treshold', threshold)


        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
    else:
        break

cap.realease()
cv2.destroyAllWindows()
