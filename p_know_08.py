#events mouse colored
import numpy as np 
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        myColorImage =np.zeros((512, 512, 3), np.uint8)
        myColorImage[:] = [blue, green, red]
    cv2.imshow('color', myColorImage)
    
#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('samples/lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
