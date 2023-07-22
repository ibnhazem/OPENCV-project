import cv2
import os

def capture_and_save_image(output_folder, image_name):
    # Create a VideoCapture object to access the webcam (0 is usually the default camera index)
    cap = cv2.VideoCapture(0)

    # TODO: Capture a frame from the webcam
    ret, frame = cap.read()

    # TODO: Check if the frame was read successfully
    if ret : return
    else : print("Frame not read")

    # TODO: Save the captured frame as an image in the output_folder
    image_file = os.path.join(output_folder, image_name) # This was the trick in the whole assignment. os.path,join() kills two birds with one stone: it saves the file in a specified dir and with the assigned name
    cv2.imwrite(image_file, frame)
    cv2.imshow(image_file, frame)

    # TODO: Release the VideoCapture object
    cap.release()

if __name__ == "__main__":
    # Set the output folder path where the image will be saved
    output_folder = "C:/Users/bashe/OneDrive - The University of Western Ontario/Desktop/Bashe/Projects/copencvtest"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    print(os.path.exists("C:/Users/bashe/OneDrive - The University of Western Ontario/Desktop/Bashe/Projects/copencvtest"))

    # Set the image name (e.g., "captured_image.jpg")
    image_name = "firstcapturedimg.jpg"

    # Capture and save the image
    capture_and_save_image(output_folder, image_name)
