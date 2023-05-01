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
from googletrans import Translator
import webbrowser
from urllib.parse import quote  # import urllib.parse

import loader
import vocabulary
from Voice_Commands import key_up, key_press, rec, stream
from loader import smile_generator
from vocabulary import sp_rec_suckadick

colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX,
          Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]

RCC = random.choice(colors)
RED = Fore.RED
LRE = Fore.LIGHTRED_EX
YEL = Fore.YELLOW
LYE = Fore.LIGHTYELLOW_EX
BLU = Fore.BLUE
LBL = Fore.LIGHTBLUE_EX
CYA = Fore.CYAN
LCY = Fore.LIGHTCYAN_EX
GRE = Fore.GREEN
LGR = Fore.LIGHTGREEN_EX
MAG = Fore.MAGENTA
LMA = Fore.LIGHTMAGENTA_EX
WHI = Fore.WHITE
BLA = Fore.BLACK
BWH = Back.WHITE
SRA = Style.RESET_ALL


def speak_tts(speak_text):
    for voice in voices:
        if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
            speak.Voice = voice
            speak.speak(speak_text)
            tts.runAndWait()
            speak.Rate = 5


speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()
tts = pyttsx3.init()

init(convert=True)


try:

    loader.download_generator()
    print('')
    loader.smile_gen_erator()
    loader.waal_generator()



except Exception as e:
    print(f"{RED} !1! :{SRA}", e)
    if __name__ == '__main__':
        while True:
            if rec.AcceptWaveform(stream.read(4000)):
                try:
                    prompt = rec.Result()
                    words = prompt[14:-3].split()
                    prompt = prompt[13:-2]
                    eng_prompt = str(prompt)
                    if keyboard.is_pressed('caps lock'):  # если клавиша нажата тогда выход
                        print('\a')
                        time.sleep(1.1)
                        exit()
                    elif prompt in ('"тест"', '"тестируем"', '"тестем"', '"тестем"'):
                        exit()
                    elif prompt != '""':
                        try:
                            print(f' {LYE}{prompt}{SRA} ', end='')
                        except TypeError:
                            print(f"{LRE}_{SRA}", sep='', end='')
                except Exception as e:
                    print(f"{RED} !1! :{SRA}", e)
