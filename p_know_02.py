#usb_video stream show and write to file
import cv2

cap = cv2.VideoCapture(1)   # usb port number
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#cap = cv2.VideoCapture('output.avi')

#print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret ==True:
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

       out.write(frame)

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)
    
       if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    else:
        break

cap.realease()
out.realease()
cv2.destroyAllWindows()


