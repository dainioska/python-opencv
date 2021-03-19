#matplotlib thresholding examples
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('samples/gradient.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV) 
_, th3 = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC) 
_, th4 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO) 

titles = ['Original Images','BINARY','BINARY_INV','BINARY_TRUNC','BINARY_TOREZO']
images = [img, th1, th2, th3, th4]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

#cv2.imshow('Image', img)
#cv2.imshow('Th1', th1)
#cv2.imshow('Th2', th2)
#cv2.imshow('Th3', th3)
#cv2.imshow('Th4', th4)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
