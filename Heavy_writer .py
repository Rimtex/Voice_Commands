
import time

import pyautogui
from colorama import Fore, Style, init, Back
import random
import loader

from address_config import model2
from vosk import Model, KaldiRecognizer
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

# Инициализация распознавателя с начальной моделью
current_model = Model(model2)
rec = KaldiRecognizer(current_model, 48000)

# Инициализация аудиопотока
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    frames_per_buffer=4000
)
stream.start_stream()


try:
    loader.download_generator()
    loader.down_generator()
    print('')
    loader.smile_gen_erator()
    loader.waal_generator()
except Exception as e:
    print(f"{RED} !1! :{SRA}", e)
