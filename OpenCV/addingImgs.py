# import openCV
import cv2 as cv
from pathlib import Path

images: list[Path] = list((Path(__file__).parent / 'img').glob('*'))
index = 0

while True:
    img1 = cv.imread('img/aizen.jpg')
    img2 = cv.imread('img/ichigo.jpg')
    height_im1 = img1.shape[0]
    width_im1 = img1.shape[1]
    height_im2 = img2.shape[0]
    width_im2 = img2.shape[1]
    
    min_height = min(height_im1, height_im2)
    min_width = min(width_im1, width_im2)
    
    cropped_im1 = img1[0:min_height, 0:min_width]
    cropped_im2 = img2[0:min_height, 0:min_width]
    
    cv.imshow('aizen', img1)
    cv.waitKey(0)
    cv.imshow('ichigo', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    img3 = cv.add(cropped_im1, cropped_im2)
    cv.imshow('add', img3)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
#     key = cv.waitKey(0)
#     if key ==  ord('q'):
#             cv.destroyAllWindows()
#     elif key ==  ord('d'):
#             index += 1
#     elif key == ord('a'):
#             index -= 1
#     index += len(images)
#     index %= len(images)