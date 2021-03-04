import cv2 as cv 
import numpy as np 
import lanes

video = cv.VideoCapture("road.mp4")

if not video.isOpened():
    print('error while opennig the video')

cv.waitKey(1)

while video.isOpened():
    _, frame = video.read()
    #cv.resizeWindow("Video", 1000, 800)
    cv.imshow("Video", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv.destroyAllWindows()

video.release()
cv.destroyAllWindows()
