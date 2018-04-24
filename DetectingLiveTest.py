'''
A live detecting program.
Still in test!
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    frame = cap.read()
    img = cv2.medianBlur(frame,5)
    cimg = img
    # Our operations on the frame come here
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        
    '''For color conversion, we use the function cv2.cvtColor(input_image, flag)
    where flag determines the type of conversion.'''
    #For BGR -> Gray conversion we use the flags cv2.COLOR_BGR2GRAY.
    #For BGR -> HSV, we use the flag cv2.COLOR_BGR2HSV.

    # Display the resulting frame
    cv2.imshow('frame',cimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
