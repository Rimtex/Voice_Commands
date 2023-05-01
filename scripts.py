"""
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
from colorama import Fore, Style, init  # , Back
from googletrans import Translator
import webbrowser
from urllib.parse import quote  # import urllib.parse
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
from googletrans import Translator
import webbrowser
from urllib.parse import quote  # import urllib.parse
import loader
import vocabulary
from Voice_Commands import key_up, key_press, print_click
from loader import smile_generator

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
init(convert=True)












# ! основной движок распознавания
# ! basic recognition engine
rec = KaldiRecognizer(Model(r"F:\Rimtex\Projects\Main\vosk-model-small-ru-0.22"), 48000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,  # частота дискретизации должна быть такой же, как и в системе!
    input=True,  # звуки > запись > микрофон > свойства > дополнительно > выставляем также и выше
    frames_per_buffer=4000

)
stream.start_stream()


def key_write(string):
    key_write('#')


def key_press(string):
    key_press('alt')


def key_down(string):
    key_down('shift')


def key_up(string):
    key_up('shift')


def hotkey(*keys):
    hotkey('alt', 'tab')
    hotkey('winleft', 'tab')

    keyboard.press('enter')
    keyboard.release('enter')
    keyboard.press_and_release('enter')


# Инициализация TTS
tts = pyttsx3.init()
init(convert=True)
pyttsx3.speak.Rate = 5
color = random.choice(colors)
while True:
    tts.runAndWait()

    data = stream.read(4000)
    if rec.AcceptWaveform(data):
        prompt = rec.Result()
        words = prompt[14:-3].split()
        prompt = prompt[13:-2]
        print(Fore.LIGHTCYAN_EX + prompt + Style.RESET_ALL, sep=' ', end=' ')
        print(Fore.LIGHTCYAN_EX + words + Style.RESET_ALL, sep=' ', end=' ')
        words = prompt[14:-3].split()  # words = " слова разделённые пробелом "

        if len(words) > 0 and words[-1] in ('согласен', 'согласись'):  # ! это  для последнего слова
            keywrite = prompt[len(words[0]) + 1:-1]  # минус первое слово
            print_click()
        if 3 > len(words) > 1 and words[0] in ('курсор', 'кликни', 'кликай', 'кликнуть', 'бешенства'):
            print(f"{LGR} число !={LRE}", end="")

        #: !2 слова! _ стартуем  первым словом _ вторым  говорим количество раз
        elif prompt in ('"курсор"', '"кликни"', '"кликай"', '"кликнуть"'):
            print_click()
            print_click()
        elif 3 > len(words) > 1 and words[0] in ('курсор', 'кликни', 'кликай', 'кликнуть', 'бешенства'):

            print(f"{LMA}\nдавай без агрессии")
            for c in "без агрессии": print(f"{random.choice(colors)}{c}", end='')


        if len(words) == 1 and re.match(r'(пизд\w{0,5}\b)|(сук\w{0,5}\b)|(охуел)', words[0]):

            if re.search(r'созда[а-я]{0,2}\s*команд[а-я]?', prompt):

                if re.match(r'^.{0,3}лев.{0,3}$', words[2]):

                    if re.match(r'бля\w{0,5}\b', words[0]):

                        file = open("F:\\Rimtex\\блокнот\\идеи.txt", "r", encoding='utf-8')

                        print(f"""
                               """, sep='', end='')

            print(f"{LMA}\nдавай без агрессии")
            print("давай без агрессии")
            try:
                hotkey('alt', 'tab')
                hotkey('winleft', 'tab')
                key_down('alt')
                key_press('tab')
                key_up('alt')

                for i in range(10):  # Цикл
                    time.sleep(1.5)





            except Exception as e:
                print(f" ", e, end='')
        elif 3 > len(words) > 1 and words[0] in ('курсор', 'кликни', 'кликай', 'кликнуть', 'бешенства'):
            print("давай без агрессии")  # стартовое слово
        elif any(word in prompt[1:-1] for word in ('сука', 'сучара', 'охуел', 'ты что бля')):
            print("давай без агрессии")  # turn_off_locks()

        elif prompt in ('"  "', '" "'):
            print(f"{LMA}\nдавай без агрессии")

            print(f"""
                """, sep='', end='')

        print(f"""{Fore.LIGHTCYAN_EX} 
        {Style.RESET_ALL}""", sep='', end='')

        print("давай без агрессии")

        pyautogui.keyDown('alt')
        # hotkey('alt', 'tab')




        print("R", sep='', end='')
        print(random.choice(colors) + "r"
              + Style.RESET_ALL, sep='', end='')
        print(Fore.LIGHTCYAN_EX + "√" + Style.RESET_ALL, sep='', end='')

    #  обернуть _ печать

    print(f"""{Fore.LIGHTCYAN_EX} {random.choice(colors)} + random.choice(colors) + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.RED} + Fore.RED + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.LIGHTRED_EX} + Fore.LIGHTRED_EX + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.YELLOW} + Fore.YELLOW + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.LIGHTYELLOW_EX} + Fore.LIGHTYELLOW_EX + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.BLUE} + Fore.BLUE + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.LIGHTBLUE_EX} + Fore.LIGHTBLUE_EX + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.CYAN} + Fore.CYAN + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.LIGHTCYAN_EX} + Fore.LIGHTCYAN_EX + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.GREEN} + Fore.GREEN + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.LIGHTGREEN_EX} + Fore.LIGHTGREEN_EX + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.MAGENTA} + Fore.MAGENTA + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.LIGHTMAGENTA_EX} + Fore.LIGHTMAGENTA_EX + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.WHITE} + Fore.WHITE + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Fore.BLACK} + Fore.BLACK + \
    {Style.RESET_ALL} + Style.RESET_ALL + \
    {Back.WHITE} + Back.WHITE + \
    {Style.RESET_ALL} + Style.RESET_ALL +                   """, sep='', end='')

    """

                    elif len(words) == 1 and re.match(r'бля\w{0,5}\b', words[0]):  
                        print(random.choice(colors) + "(._.)", sep='', end='')
                        speak_tts(vocabulary.sp_rec_reaction_Fuck())
                    elif len(words) == 1 and re.match(r'(пизд\w{0,5}\b)|(сук\w{0,5}\b)|(охуел)', words[0]):
                        print(random.choice(colors) + "(´•_•`)", sep='', end='')
                        speak_tts("давай без агрессии")






    """

    """

numbers_dict = numbers() # вызвать функцию только один раз и сохранить результат в переменной
print(numbers_dict)
words = numbers_dict.keys() # получить ключи словаря с числительными в виде слов
print(words)
nums = numbers_dict.values() # получить значения словаря с числами в виде цифр
print(nums)




from pygpt4all.models.gpt4all import GPT4All

def new_text_callback(text):
print(text, end="")

model = GPT4All('./models/ggml-gpt4all-j.bin')
model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)





















О, я понимаю, что вы хотите создать словарь, где ключи - это слова, а значения - это соответствующие числа. Вот как можно создать такой словарь на Python:

python
Copy code
словарь = {
'ноль': 0,
'один': 1,
'два': 2,
'три': 3,
'четыре': 4,
'пять': 5,
'шесть': 6,
'семь': 7,
'восемь': 8,
'девять': 9,
'десять': 10
}
Вы можете продолжать добавлять слова и числа в этот словарь, если нужно. Например, если вы хотите добавить слово "одиннадцать" с числовым значением 11, вы можете сделать это следующим образом:

python
Copy code
словарь['одиннадцать'] = 11
Надеюсь, это поможет вам создать словарь для вашего проекта!





Rimtex _


как вызывать в скрипте
elif prompt == '"четыре"':
keyboard.press_and_release('4')

Предположим, что вы хотите использовать этот код в своем Python-скрипте. Чтобы вызвать его внутри блока elif, вам нужно будет сначала импортировать модуль keyboard, который является сторонней библиотекой для управления клавиатурой на Python. Для этого вы можете использовать следующую команду:

python
Copy code
import keyboard
Затем вы можете вызвать keyboard.press_and_release() внутри блока elif, чтобы эмулировать нажатие и отпускание клавиши на клавиатуре. Вот как может выглядеть код в вашем случае:

python
Copy code
import keyboard

prompt = input("Введите команду: ")

if prompt == "четыре":
keyboard.press_and_release('4')
elif prompt == "пять":
keyboard.press_and_release('5')
# Добавьте другие блоки elif для других команд
else:
print("Неправильная команда")
Когда вы запустите этот код и введите "четыре", то он должен вызвать функцию keyboard.press_and_release('4') и эмулировать нажатие и отпускание клавиши "4" на клавиатуре.





Rimtex _
сократить скрипт и сделать его одним вызывая функцию можно  ?

Да, вы можете сделать скрипт более компактным и создать функцию, которая будет эмулировать нажатие и отпускание клавиши на клавиатуре в зависимости от введенной команды. Вот пример такой функции:

python
Copy code
import keyboard

def нажать_клавишу_на_клавиатуре(команда):
elif prompt == "ноль":
keyboard.press_and_release('0')
elif prompt == "один":
keyboard.press_and_release('1')
elif prompt == "два":
keyboard.press_and_release('2')
elif prompt == "три":
keyboard.press_and_release('3')
elif prompt == "четыре":
keyboard.press_and_release('4')
elif prompt == "пять":
keyboard.press_and_release('5')
elif prompt == "шесть":
keyboard.press_and_release('6')
elif prompt == "семь":
keyboard.press_and_release('7')
elif prompt == "восемь":
keyboard.press_and_release('8')
elif prompt == "девять":
keyboard.press_and_release('9')
elif prompt == "десять":
keyboard.press_and_release('10')
else:
print("Неправильная команда")
Затем, чтобы использовать эту функцию в вашем скрипте, вы можете вызвать ее и передать в нее введенную команду:

python
Copy code
команда = input("Введите команду: ")
нажать_клавишу_на_клавиатуре(команда)
Таким образом, вы можете уменьшить размер вашего скрипта, создав функцию для эмуляции нажатия клавиши и вызвать ее с помощью введенной команды.







python:
change and improve:
in my code:

speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()

# # Definition of the function that will voice the text from the TTS
def speak_tts(speak_text):
for voice in voices:
if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
speak.Voice = voice
speak.speak(speak_text)
tts.runAndWait()
speak.Rate = 5


def speak_Irina_tts(speak_text):
for voice in voices:
if voice.GetAttribute("Name") == "Microsoft Irina Desktop":
speak.Voice = voice
speak.speak(speak_text)
tts.runAndWait()
speak.Rate = 5



python:
change and improve:
in my code:

#! basic recognition engine
while True:
tts.runAndWait()
speak.Rate = 5
data = stream.read(4000)
if rec.AcceptWaveform(data):
prompt = rec.Result()  # rec.Result() выдает - {   "text" : "слова" }
words = prompt[14:-3].split()  # words = " слова разделённые пробелом "
prompt = prompt[13:-2]  # prompt = "слова"




need to make the following script work!:
prompt = prompt[13:-2]  # prompt = "слова"
elif prompt in ('"павел"', '"мужской"'):
voice switch to Microsoft Pavel Mobile

elif prompt in ('"ирина"', '"женский"'):
voice switch to Microsoft Irina Desktop


python:
change and improve:
in my code:


python:

#  the functions need to be changed
def speak_tts(speak_text):
speak = wincl.Dispatch("SAPI.SpVoice")

voices = speak.GetVoices()
for voice in voices:
if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
speak.Voice = voice
speak.speak(speak_text)
tts.runAndWait()
speak.Rate = 5

#  the functions need to be changed
def speak_Irina_tts(speak_text):
speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()
for voice in voices:

if voice.GetAttribute("Name") == "Microsoft Irina Desktop":
speak.Voice = voice
speak.speak(speak_text)
tts.runAndWait()
speak.Rate = 5

rec = KaldiRecognizer(Model(r"F:\Rimtex\Projects\Main\vosk-model-small-ru-0.22"), 48000)
p = pyaudio.PyAudio()
stream = p.open(
format=pyaudio.paInt16,
channels=1,
rate=48000,  # частота дискретизации должна быть такой же, как и в системе!
input=True,  # звуки > запись > микрофон > свойства > дополнительно > выставляем также и выше
frames_per_buffer=4000

)
stream.start_stream()

tts = pyttsx3.init()
init(convert=True)
pyttsx3.speak.Rate = 5
color = random.choice(colors)

while True:
tts.runAndWait()
speak.Rate = 5
data = stream.read(4000)
if rec.AcceptWaveform(data):
prompt = rec.Result()  # rec.Result() выдает - {   "text" : "слова" }
words = prompt[14:-3].split()  # words = " слова разделённые пробелом "
prompt = prompt[13:-2]  # prompt = "слова"

how do I switch voice
a function should be made to switch the voice

elif prompt in (''Pavel'', ''male''):
the voice is switched to Microsoft Pavel Mobile

elif prompt in (''Irina'', ''female''):
voice switch to Microsoft Irina Desktop




























import win32com.client as wincl

def get_voice(name):
speak = wincl.Dispatch("SAPI.SpVoice")
for voice in speak.GetVoices():
if voice.GetAttribute("Name") == name:
speak.Voice = voice
break
return speak

# Получение голосов для Microsoft Pavel Mobile и Microsoft Irina Desktop
pavel_voice = get_voice("Microsoft Pavel Mobile")
irina_voice = get_voice("Microsoft Irina Desktop")

# Определите функцию для произнесения заданного текста заданным голосом
def speak_tts(speak, speak_text):
speak.speak(speak_text)
speak.runAndWait()
speak.Rate = 5

# Используйте функции для проговаривания текста нужными голосами
speak_tts(pavel_voice, "Этот текст будет произнесен голосом Павла.")
speak_tts(irina_voice, "Этот текст будет произнесен голосом Ирины.")


Переведено с помощью www.DeepL.com/Translator (бесплатная версия)







rimvoc_





speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()
for voice in voices:
if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":  # Microsoft Irina Desktop  файлы реестра в папке
speak.Voice = voice  # - need install for pavel voice
break


# Определение функции, которая будет озвучивать текст с TTS
def speak_tts(speak_text):
for voice in voices:
if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
speak.Voice = voice
speak.speak(speak_text)
tts.runAndWait()
speak.Rate = 5


def speak_Irina_tts(speak_text):
for voice in voices:
if voice.GetAttribute("Name") == "Microsoft Irina Desktop":
speak.Voice = voice
speak.speak(speak_text)
tts.runAndWait()
speak.Rate = 5

















from colorama import Fore, Style

print(
f"{Fore.LIGHTCYAN_EX}˃˃ {Fore.LIGHTYELLOW_EX}♪-♫ {Style.RESET_ALL}== {Fore.LIGHTGREEN_EX}а-я {Style.RESET_ALL} ",
sep='', end='')


def speak_tts(param):
pass


speak_tts("запись отключена! ")

# speak = wincl.Dispatch("SAPI.SpVoice")
# voices = speak.GetVoices()









#  elif len(words) == 2 and words[1] in ('библиотека', 'библиотеку', 'модуль', 'пип', 'модуля', 'модули'):

#  Здесь [ау]{0,1} означает, что может присутствовать ноль или одна буква "а" или "у".
#  elif len(words) == 2 and re.match(r'(библиотек[ау]{0,1})|(модул[ьи]?.{0,1})|(пип.{0,1})', words[1]):

#  Здесь [ау]?.{0,1}) означает, что может присутствовать ноль или одна любая буква.
#  elif len(words) == 2 and re.match(r'(библиотек[ау]?.{0,1})|(модул[ьи]?.{0,1})|(пип.{0,1})', words[1]):

# (библиотек[ау]?) будет соответствовать только таким строкам за которым может следовать символ "а" или "у".




"""
