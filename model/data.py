#NOTE: FROM ABHISHEK
import cv2
import os
import time

# Prompt the user to enter the name of the person
person_name = input("Enter the name of the person: ")

# Create a folder named "data_images" to store the images if it doesn't exist
data_images_folder = "data_images"
os.makedirs(data_images_folder, exist_ok=True)

# Create a folder inside "data_images" with the name of the person
person_folder = os.path.join(data_images_folder, person_name)
os.makedirs(person_folder, exist_ok=True)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Set the width and height of the camera frame (adjust as needed)
cap.set(3, 640)
cap.set(4, 480)

# Initialize pic_count
pic_count = 1

# Main loop to capture images
while pic_count <= 20:  # Capture 20 images
    # Capture a frame
    ret, frame = cap.read()

    # Display a red dot along with the pic_count on the frame
    cv2.putText(frame, f"Pic {pic_count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Capture', frame)

    # Wait for 1 second with a red dot
    for _ in range(20):  # 20 frames (1 second at 20 frames per second)
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)
        cv2.imshow('Capture', frame)
        cv2.waitKey(50)  # 50 milliseconds

    # Save the captured frame in the person's folder
    #timestamp = time.strftime("%Y%m%d%H%M%S")
    #image_name = f"{person_name}_{timestamp}.jpg"
    image_name = f"{person_name}_{pic_count}.jpg"
    image_path = os.path.join(person_folder, image_name)
    cv2.imwrite(image_path, frame)

    # Increment pic_count
    pic_count += 1

    # Press 'q' to quit the loop prematurely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()
