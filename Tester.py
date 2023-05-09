# уличный дэнсер


import os

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

import psutil

for proc in psutil.process_iter():
    try:
        print(proc.name())  # название процесса
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


# printt("\n----------------конец теста----------------")
# input("")
