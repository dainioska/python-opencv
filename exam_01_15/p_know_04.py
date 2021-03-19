#usb_video stream parameters and text insert
import cv2

cap = cv2.VideoCapture(0)   # usb port number
cap.set(3, 1000)
cap.set(4, 700)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret ==True:

       #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       #cv2.imshow('frame', gray)

       font = cv2.FONT_HERSHEY_SIMPLEX
       text = 'Width: '+ str(cap.get(3)) + 'Height: ' + str(cap.get(4))
       frame = cv2.putText(frame, text, (10, 50), font, 1, (0,255,255), 2, cv2.LINE_AA)
       cv2.imshow('frame', frame)
    
       if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    else:
        break

cap.realease()
cv2.destroyAllWindows()


