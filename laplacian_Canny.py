import cv2 as cv
import numpy as np

webCam = cv.VideoCapture(0)

while True:
    # Turns out we do not need the "ref" value. If we use '_' it basically means ignore.
    # The reason why we can't just "not write ref" is because VideoCapture() returns two values, one boolean(if successful) and the actual frame.
    _, frame = webCam.read()
    # frame = cv.flip(frame, 0)
        
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert BGR to RGB
    gray = cv.cvtColor(rgb_frame, cv.COLOR_RGB2GRAY)  # Convert RGB to grayscale
    
    # _, thresholded_image = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    
    # cv.imshow("control_gray", gray)
    
    # CV_64F: 64-bits floating. Each pixel is represented by a 64-bit floating value.
    # laplacian_64 = cv.Laplacian(frame, cv.CV_64F)
    # uint8() converts the bits in an array(the frame) to an 8-bit unsigned value. So now each pixel is represented by 8-bits.
    # laplacian_8 = np.uint8(laplacian_64)
    # cv.imshow("Laplacian 8bit", laplacian_8)

    edgeDet = cv.Canny(gray, 20, 50)
    cv.imshow("Canny_Gray", edgeDet)
    
    # rgb_Canny = cv.Canny(frame, 20, 50)
    # cv.imshow("rgb canny", rgb_Canny)
    
    
    # The waitKey() function takes the value from the keyboard. It converts each input to an ASCII value.
    # The ord() function only accepts characters. It then converts that char to its corresponding ASCII value.
    # If the key pressed is the same as the char in ord (both have same ASCII value), then the If statement breaks out from the inf while loop.
    if cv.waitKey(5) == ord('q') :
        break

# When leaving the while loop, the camera is disconnected and all windows are closed.
webCam.release()
cv.destroyAllWindows()
    
    