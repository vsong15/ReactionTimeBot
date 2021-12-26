from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import sys

# https://humanbenchmark.com/tests/reactiontime

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(648, 727)[0] == 75 or pyautogui.pixel(649, 727)[1] == 219 or pyautogui.pixel(648, 727)[2] == 106:
        click(648, 727)
        win32api.SetCursorPos((648, 727))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        sys.exit()
