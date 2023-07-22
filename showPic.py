import cv2

def capture_image_and_display():
    # Open the default camera (usually 0) or use a specific camera by providing its index
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    # Set the camera resolution (optional, you can skip this if you want to use the default resolution)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Capture a single frame from the camera
    ret, frame = cap.read()
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    gray_img = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)  # Convert RGB to grayscale

    if not ret:
        print("Error: Unable to capture the frame.")
        cap.release()
        return

    # Display the captured frame in a window
    cv2.imshow('Captured Image', gray_img)

    # Wait for a key event (0 milliseconds) and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Release the camera
    cap.release()

if __name__ == "__main__":
    capture_image_and_display()
