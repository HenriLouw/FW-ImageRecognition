import time
import keyboard
import pyautogui
import win32api
import win32con

time.sleep(6)


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(5)

def energy():
    step1_plus = pyautogui.moveTo(1700, 167)
    pyautogui.click()
    time.sleep(3)

    step2_plusbutton = pyautogui.moveTo(1098, 552)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(3)
    
    step3_exchange = pyautogui.moveTo(962, 629)
    pyautogui.click()
    time.sleep(9)

def ok():
    ok_button = pyautogui.moveTo(959, 675)
    pyautogui.click()
    time.sleep(10)

def repair():
    repair_button = pyautogui.moveTo(1204, 682)
    pyautogui.click()
    time.sleep(8)

while not keyboard.is_pressed('q'):
    mine = pyautogui.locateCenterOnScreen('mine.PNG', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
    if mine is not None:
        pyautogui.moveTo(mine) 
        left_click()
        time.sleep(10)
        ok()
        repair()
        energy()