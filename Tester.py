"""
import os
import requests
import re
import time
import random
import keyboard
import pyautogui
import pyaudio
import py_win_keyboard_layout
from datetime import date, datetime
import vosk
import pyttsx3
import win32api
import win32clipboard
import win32com.client
import ctypes
from vosk import Model, KaldiRecognizer
import win32com.client as wincl
from colorama import Fore, Style, init, Back
import webbrowser
from urllib.parse import quote  # import urllib.parse
    """
import time

from colorama import Fore, Style, init, Back
import random

import loader

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX,
          Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]
RCC = random.choice(colors)
RED = Fore.RED
LRE = Fore.LIGHTRED_EX
YEL = Fore.YELLOW
LYE = Fore.LIGHTYELLOW_EX
# BLU = Fore.BLUE
LBL = Fore.LIGHTBLUE_EX
CYA = Fore.CYAN
LCY = Fore.LIGHTCYAN_EX
GRE = Fore.GREEN
LGR = Fore.LIGHTGREEN_EX
# MAG = Fore.MAGENTA
LMA = Fore.LIGHTMAGENTA_EX
WHI = Fore.WHITE
BLA = Fore.BLACK
BWH = Back.WHITE
SRA = Style.RESET_ALL
init(convert=True)
loader.download_generator()

# в операционной системе Windows на языке Python
""" Для получения названий открытых приложений: """
import win32gui


def get_window_titles():
    titles = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            titles.append(win32gui.GetWindowText(hwnd))
        return True

    win32gui.EnumWindows(callback, None)
    return titles


print(get_window_titles())

""" получить список запущенных процессов и их названий: """
import psutil

process_list = []
for proc in psutil.process_iter(['name']):
    try:
        # Получаем название процесса
        process_name = proc.info['name']
        process_list.append(process_name)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print(process_list)

"""открыть приложение и сделать его активным"""
import pyautogui
import subprocess
import time

# Запускаем блокнот
subprocess.Popen('notepad.exe')

# Даем приложению время для запуска
time.sleep(1)

# Получаем позицию
window_position = pyautogui.getWindowsWithTitle('ассистент')[0].topleft

# Делаем окно блокнота активным
pyautogui.click(window_position)

from python_translator import Translator

translator = Translator()
result = translator.translate("Hello world!"
                              "Tell me an interesting fact about space."
                              "What is a surprising fact about animals?"
                              "Give me a fascinating historical fact."
                              "Tell me something intriguing about technology."
                              "What is an unusual fact about the human body?"
                              "Give me a surprising fact about the natural world."
                              "Tell me a fun fact about a famous person."
                              "What is an interesting fact about the brain?"
                              "Give me a unique fact about art or literature."
                              "Tell me something remarkable about ancient civilizations."
                              "What is a little-known fact about the ocean?"
                              ""
                              ""
                              ""
                              ""
                              ""
                              "", "russian", "english")

print(result)

try:
    loader.download_generator()
    loader.down_generator()
    print('')
    loader.smile_gen_erator()
    loader.waal_generator()
except Exception as e:
    print(f"{RED} !1! :{SRA}", e)
