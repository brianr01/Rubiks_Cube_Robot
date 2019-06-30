import numpy as np
import cv2

print('setting up cameras')
cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
print('finished setting up cameras')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret, frame1 = cap1.read()


    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('frame1',frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()