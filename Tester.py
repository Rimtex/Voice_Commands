# уличный дэнсер


import os

from address_config import path_to_shortcut

try:
    import time
    import random
    import pygetwindow
    import pyautogui
except ImportError:
    print("Trying to Install required modules:")
    os.system('pip install psutil pyautogui win32gui')
    import time
    import random
    import pygetwindow
    import pyautogui

print("----------------начало теста----------------\n")

DeepL = pyautogui.getWindowsWithTitle('DeepL')[0]
DeepL.minimize()
DeepL.restore()
DeepL.moveTo(1200, 319)
DeepL.resizeTo(849, 1089)

# printt("\n----------------конец теста----------------")
# input("")
