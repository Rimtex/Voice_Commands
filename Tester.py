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


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)



print("\nchar")
import psutil

processes = []
for proc in psutil.process_iter():
    try:
        if proc.name() not in processes:
            processes.append(proc.name())
            print(proc.name())
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# printt("\n----------------конец теста----------------")
# input("")
