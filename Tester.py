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

import pyautogui
from colorama import Fore, Style, init, Back
import random
import loader
from keyboard_scripts import key_press

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

loader.waal_generator()

try:
    loader.download_generator()
    loader.down_generator()
    print('')
    loader.smile_gen_erator()
    loader.waal_generator()
except Exception as e:
    print(f"{RED} !1! :{SRA}", e)
