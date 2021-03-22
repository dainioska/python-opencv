# programmingKnowlege  hough transformations LINE probablistic
import numpy as np 
import cv2 as cv 

#img = cv.imread('samples/sudoku.png')
img = cv.imread('samplesH/lines.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('edges', edges)

lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
cv.imshow('output', img)
cv.waitKey(0)
cv.destroyAllWindows()