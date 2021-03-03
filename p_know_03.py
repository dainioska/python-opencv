#paint goemetric to image and  numpy field
import cv2
import numpy as np

#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img =cv2.line(img, (0,0), (255, 255), (255,0,0), 5)
img = cv2.circle(img, (475, 65),65, (0, 255,0), -1)
cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()