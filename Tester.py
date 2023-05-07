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

"""                          начало теста                          """

# в операционной системе Windows на языке Python
# Для получения названий открытых приложений:
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

# получить список запущенных процессов и их названий:
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

# открыть приложение и сделать его активным
import pyautogui
import subprocess
import time

# Запускаем блокнот
# subprocess.Popen('notepad.exe')


window_position = pyautogui.getWindowsWithTitle('Commit')[0].topleft # Получаем позицию
pyautogui.moveTo(window_position)  # Делаем окно активным
pyautogui.moveRel(33, 92, duration=0.25)
pyautogui.click()


"""                            конец теста                            """
input("")
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
