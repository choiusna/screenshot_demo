# screenshot.py
import os
import time
from PIL import ImageGrab 

def main():
    # Save to a folder the user owns (AppData)
    save_path = os.path.join(os.getenv('LOCALAPPDATA'), "Temp", "LabScreenshots")
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Filename with current time
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"capture_{now}.png"

    # Capture and Save
    img = ImageGrab.grab()
    img.save(os.path.join(save_path, file_name))

if __name__ == "__main__":
    main()
