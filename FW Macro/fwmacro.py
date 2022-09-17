import time
import keyboard
import pyautogui
import win32api
import win32con

time.sleep(6)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(5)


while not keyboard.is_pressed('q'):
    mine = pyautogui.locateCenterOnScreen('mine.PNG', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.95)
    ok = pyautogui.locateCenterOnScreen('ok.PNG', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.75)
    if mine is not None:
        pyautogui.moveTo(mine) 
        click()
    if mine is None:
        pyautogui.moveTo(ok) 
        click()
    
