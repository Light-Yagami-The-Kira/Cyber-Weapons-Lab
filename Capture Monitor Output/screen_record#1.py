import pyautogui
import cv2
import numpy as np

# Specify the dimensions of the screen
screen_width, screen_height = pyautogui.size()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('screen_record.avi', fourcc, 20.0, (screen_width, screen_height))

try:
    while True:
        # Capture the screen and convert it to a numpy array
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)

        # Convert RGB to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)


finally:
    # Release the VideoWriter and close the OpenCV windows
    out.release()
    cv2.destroyAllWindows()
