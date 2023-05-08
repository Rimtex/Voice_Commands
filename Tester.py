import time

import pyautogui


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    time.sleep(1)



assistant = pyautogui.getWindowsWithTitle('ассистент')[0]
# position.restore()
assistant.moveTo(-8, 1)  # двигаем ассистента в угол
assistant_bottomright = pyautogui.getWindowsWithTitle('ассистент')[0].bottomright
pyautogui.mouseDown()
pyautogui.moveTo(-98, 18)  # настраиваем размер окна
pyautogui.mouseUp()