#usb_video stream parameters
import cv2

cap = cv2.VideoCapture(0)   # usb port number
cap.set(3, 1208)
cap.set(4, 720)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret ==True:

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)
    
       if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    else:
        break

cap.realease()
cv2.destroyAllWindows()


