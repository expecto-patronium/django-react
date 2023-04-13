import random

import win32api
import win32con
import time
import pyautogui

with open("ser.txt", "r") as f:
    data = f.read()
# dt = input("")
for k in data:
    pyautogui.press(k)
    # pyautogui.moveTo(900, 500)
    # win32api.mousfe_event(win32con.MOUSEEVENTF_LEFTDOWN, 100, 100, 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 100, 100, 0, 0)
    time.sleep(random.uniform(0.5, 3))
    time.sleep(0.5)
