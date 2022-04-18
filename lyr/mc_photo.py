import numpy as np
import cv2


while(True):
    frame = cv2.imread("C:/Users/Lenovo/Desktop/R-C.jpg")

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imwrite('C:/Users/Lenovo/Desktop/qtarget.png',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()