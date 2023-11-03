import cv2 as cv
import numpy as np

img = cv.imread('img/hollow-ichigo.jpg')

# Check if the image is grayscale or color
is_color = len(img.shape) == 3 and img.shape[2] > 1

# Define the custom kernel size
kernel_size = 9  # An odd number for a valid kernel size

# Apply the median blur with the custom kernel
if is_color:
    filtered = cv.medianBlur(img, kernel_size)
else:
    filtered = cv.medianBlur(img, kernel_size)

cv.imshow("filtered img", filtered)
cv.waitKey(0)
cv.destroyAllWindows()

# kernel = np.ones((10,10), np.float32) / 100