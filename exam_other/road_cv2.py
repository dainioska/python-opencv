import cv2 as cv 
import numpy as np 
import lanes

video = cv.VideoCapture("samplesH/road_01.mp4")

if not video.isOpened():
    print('error while opennig the video')

cv.waitKey(1)

while video.isOpened():
    _, frame = video.read()
    cv.resizeWindow("Video", 1300, 800)
    copy_img = np.copy(frame)

    frame = lanes.canny(frame)
    frame =lanes.mask(frame)
    lines = cv.HoughLinesP(frame, 2, np.pi/180, 100, np.array([()]), minLineLength=20, maxLineGap=5)
    average_lines = lanes.average_slope_intercept(frame, lines)
    line_image =lanes.display_lines(copy_img, average_lines)
    combo = cv.addWeighted(copy_img, 0.8, line_image, 0.5, 1)

    cv.imshow("Video", combo)

    if cv.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv.destroyAllWindows()

video.release()
cv.destroyAllWindows()
