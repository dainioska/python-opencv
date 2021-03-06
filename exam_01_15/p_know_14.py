#thresholding examples
import cv2

img = cv2.imread('samples/gradient.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV) 
_, th3 = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC) 
_, th4 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO) 

cv2.imshow('Image', img)
cv2.imshow('Th1', th1)
cv2.imshow('Th2', th2)
cv2.imshow('Th3', th3)
cv2.imshow('Th4', th4)

cv2.waitKey(0)
cv2.destroyAllWindows()
