import cv2 as cv
from pathlib import Path

cap = cv.VideoCapture(0)
images: list[Path] = list((Path(__file__).parent / 'img').glob('*'))
image_read_list = [cv.imread(str(images[index])) for index in range(len(images))]

if not cap.isOpened():
    print("Camera not working")
    exit()

fade_in = True
alpha = 0.0
fade_speed = 0.01
current_image_index = 0
fade_complete = False

while True:
    if not fade_complete:
        image = image_read_list[current_image_index]
        while True:
            img2 = image
            ret, frame = cap.read()
            if not ret:
                print("Couldn't get a frame")
                break
    
            height_im1 = frame.shape[0]
            width_im1 = frame.shape[1]
            height_im2 = img2.shape[0]
            width_im2 = img2.shape[1]
    
            min_height = min(height_im1, height_im2)
            min_width = min(width_im1, width_im2)
    
            cropped_im1 = frame[0:min_height, 0:min_width]
            cropped_im2 = img2[0:min_height, 0:min_width]

            if fade_in:
                alpha += fade_speed
                if alpha >= 1.0:
                    alpha = 1.0
                    fade_in = False
            else:
                alpha -= fade_speed
                if alpha <= 0.0:
                    alpha = 0.0
                    fade_in = True
                    fade_complete = True
    
            blended = cv.addWeighted(cropped_im1, 1.0 - alpha, cropped_im2, alpha, 0.0)
    
            cv.imshow('frame', blended)
    
            if cv.waitKey(1) == ord('q'):
                break

    if fade_complete:
        fade_complete = False
        alpha = 0.0
        fade_in = True
        current_image_index += 1
        if current_image_index >= len(image_read_list):
            break

cap.release()
cv.destroyAllWindows()