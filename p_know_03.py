#paint goemetric to image
import cv2

img = cv2.imread('lena.jpg', 1)
img =cv2.line(img, (0,0), (255, 255), (255,0,0), 5)
cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()