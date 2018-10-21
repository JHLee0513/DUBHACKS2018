import cv2 as cv
import serial as ser
import numpy as np

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
kernel = np.ones((15,15),np.uint8)
cameraPan = 0
cameraTilt = 0
line = ' '
cam = cv.VideoCapture(0)
ser = ser.Serial('/dev/ttyACM0', baudrate = 115200, timeout = .05)
ser.write('a')
ser.reset_input_buffer()


while(True):
    
    retriv, frame = cam.read()
    if(retriv):
        
        blurred = cv.GaussianBlur(frame, (11, 11), 0)
        hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv, greenLower, greenUpper)
        mask = cv.erode(mask, kernel, iterations=2)
        mask = cv.dilate(mask, kernel, iterations=2)
        image, contours, hier = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


        cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[1]
        center = None
        currentx = 320
        currenty = 240

        if len(cnts) > 0:

            c = max(cnts, key=cv.contourArea)
            ((x, y), radius) = cv.minEnclosingCircle(c)
            M = cv.moments(c)
            currentx = int(M["m10"] / M["m00"])
            currenty = int(M["m01"] / M["m00"])
            center = (currentx, currenty)

            if radius > 5:

                cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv.circle(frame, center, 5, (0, 0, 255), -1)
 

        cameraPan = currentx - 320
        cameraTilt = currenty - 240
        #print str(cameraPan) + ' ' + str(cameraTilt)
        cv.imshow('mask',mask)
        cv.imshow('my camera',frame)
    #ser.reset_output_buffer()    
    meg = str(cameraPan) + 'b' + str(cameraTilt) + '\n'
    print meg
    ser.write(meg)
    #line = ser.readline()
    #if(ser.in_waiting > 10):
    #    ser.reset_input_buffer()
    #print line
    
        
    if(cv.waitKey(1) == 27):
        break
    

cam.release()
cv.destroyAllWindows()
