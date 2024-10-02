from config import EXCEL_PW
import os
import pyautogui
import threading
import time


# Function used for the handling of the file and generation of the data from linked .xlsx workbooks
def handle_file(file_path):

    def open_excel_thread():
        # Open the Excel file
        os.startfile(file_path)

    thread = threading.Thread(target=open_excel_thread)
    thread.start()

    time.sleep(5)
    print("Done Sleeping")
    print("Typing")
    pyautogui.typewrite(EXCEL_PW)
    pyautogui.press("enter")
    # Wait for Excel to open and load the file
    time.sleep(5)
    # Close the Excel window (Alt + F4)
    pyautogui.hotkey('alt', 'f4')
    # Wait
    time.sleep(2)
    # Press the 'Enter' key to save changes
    pyautogui.press('enter')
