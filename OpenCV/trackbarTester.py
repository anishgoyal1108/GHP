import numpy as np
import cv2 as cv

def nothing(x):
    pass

img = np.zeros((640, 480, 3), np.uint8)
cv.namedWindow('color')

cv.createTrackbar('R', 'color', 0, 255, nothing)
cv.createTrackbar('G', 'color', 0, 255, nothing)
cv.createTrackbar('B', 'color', 0, 255, nothing)

while True:
    cv.imshow('color', img)
    redValue = cv.getTrackbarPos('R', 'color')
    greenValue = cv.getTrackbarPos('G', 'color')
    blueValue = cv.getTrackbarPos('B', 'color')
    img[:] = [blueValue, greenValue, redValue]
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()