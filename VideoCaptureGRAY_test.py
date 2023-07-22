import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

frame_count = 0
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert BGR to RGB
    gray = cv.cvtColor(rgb_frame, cv.COLOR_RGB2GRAY)  # Convert RGB to grayscale
    gray = cv.flip(gray, 1)  # Flip the frame horizontally

    # Display the resulting frame
    cv.imshow('frame', gray)

    frame_count += 1
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1.0:
        fps = frame_count / elapsed_time
        print("Frame rate:", round(fps, 2))
        frame_count = 0
        start_time = time.time()

    if cv.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()