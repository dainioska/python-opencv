#matplotlib filtering
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('samples/smarties.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

titles = ['image']
images = [img]

for i in range(1):
    plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
