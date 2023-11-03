import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera not working")
    exit()

while True:
    # capture a frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to get frame")
        break
    
    # convert our frame from BGR to HSV
    hsvConverted = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define boundaries for what we consider to be blue
    lower = np.array([80, 50, 50])
    upper = np.array([160, 255, 255])
    
    generatedMask = cv.inRange(hsvConverted, lower, upper)
    
    result = cv.bitwise_and(frame, frame, mask=generatedMask)
    
    # convert the frame from BGR to gray
    # grayConverted = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('frame', grayConverted)
    
    cv.imshow('frame', frame)
    cv.imshow('mask', generatedMask)
    cv.imshow('result', result)
    
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()