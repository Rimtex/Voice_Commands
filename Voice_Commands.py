import os

try:
    import requests
    import traceback
    import re
    import time
    import random
    import keyboard
    import pyautogui
    import py_win_keyboard_layout
    import pyaudio
    import pyttsx3
    import vosk
    import win32com.client
    from vosk import Model, KaldiRecognizer
    import win32com.client as wincl
    from colorama import Fore, Style, init, Back
    from python_translator import Translator
    from datetime import date, datetime
    import webbrowser
    import win32api
    import win32clipboard
    import ctypes
except ImportError:
    print("Trying to Install required modules: requirements.txt")
    os.system('pip install --upgrade -r "requirements.txt"')
    import requests
    import traceback
    import re
    import time
    import random
    import keyboard
    import pyautogui
    import py_win_keyboard_layout
    import pyaudio
    import pyttsx3
    import vosk
    import win32com.client
    from vosk import Model, KaldiRecognizer
    import win32com.client as wincl
    from colorama import Fore, Style, init, Back
    from python_translator import Translator
    from datetime import date, datetime
    import webbrowser
    import win32api
    import win32clipboard
    import ctypes

from keyboard_scripts import key_press, keyhot, key_down, key_write, key_up, click_print, keyrus_write, \
    keytrans_write, words_num

import loader
from loader import loader_screen_rimtex
from converter import convert_paint, convert_trans, convert_delete

from address_config import assistant_window, path_to_shortcut, ideas, reminder, dir_path, model1, model2, model3, model4

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX,
          Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]

RCC = random.choice(colors)
RED = Fore.RED
LRE = Fore.LIGHTRED_EX
YEL = Fore.YELLOW
LYE = Fore.LIGHTYELLOW_EX
#  BLU = Fore.BLUE  # слишком тёмные цвета
LBL = Fore.LIGHTBLUE_EX
CYA = Fore.CYAN
LCY = Fore.LIGHTCYAN_EX
GRE = Fore.GREEN
LGR = Fore.LIGHTGREEN_EX
#  MAG = Fore.MAGENTA
LMA = Fore.LIGHTMAGENTA_EX
WHI = Fore.WHITE
BLA = Fore.BLACK
BWH = Back.WHITE
SRA = Style.RESET_ALL

init(convert=True)  # активация покраски


def printt(textt):
    for char in textt:
        print(char, end='', flush=True)
        time.sleep(0.015)


# функция выключения Caps Lock и Num Lock
def turn_off_locks():
    # Проверить, включена ли клавиша Caps Lock
    caps_lock_state = win32api.GetKeyState(0x14)  # 0x14 - код клавиши Caps Lock
    if caps_lock_state == 1 or caps_lock_state == -127:  # Если клавиша включена
        # Нажать клавишу Caps Lock, чтобы выключить её
        win32api.keybd_event(0x14, 0x45, 0x1, 0)
        win32api.keybd_event(0x14, 0x45, 0x3, 0)
    # Проверить, включена ли клавиша Num Lock
    num_lock_state = win32api.GetKeyState(0x90)  # 0x90 - код клавиши Num Lock
    if num_lock_state == 1 or num_lock_state == -127:  # Если клавиша включена
        # Нажать клавишу Num Lock, чтобы выключить её
        win32api.keybd_event(0x90, 0x45, 0x1, 0)
        win32api.keybd_event(0x90, 0x45, 0x3, 0)


turn_off_locks()
py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)  # переключение на английскую раскладку
tts = pyttsx3.init()


#: направление курсора: третье слово
def cursor_direction():
    if re.match(r'^.{0,3}прав.{0,3}$', words[2]):
        pyautogui.moveRel(numss, 0)
    if re.match(r'^.{0,3}низ.{0,3}$', words[2]):
        pyautogui.moveRel(0, numss)
    if re.match(r'^.{0,3}лев.{0,3}$', words[2]):
        pyautogui.moveRel(-numss, 0)
    if re.match(r'^.{0,3}верх.{0,3}$', words[2]):
        pyautogui.moveRel(0, -numss)


# для проигрывания случайной музыки
def play_music():
    music_files = []
    for root, dirs, files_op in os.walk(dir_path):
        for file_op in files_op:
            if file_op.endswith(".mp3") or file_op.endswith(".wav"):
                file_path_op = os.path.join(root, file_op)
                music_files.append(file_path_op)
    if not music_files:
        print("The directory is empty.")
    else:
        random_file_op = random.choice(music_files)
        os.startfile(random_file_op)
        print(f" {LGR}Playing: {WHI}{random_file_op}{LGR}", end='')


#: повтор нажатий клавиш плюс цифры
def numbers_key():  # назначаем kps клавишу в скрипте например:
    if len(words) == 1:
        if len(kps) == 1:
            key_press(*kps)  # kps = ['shift']
        elif len(kps) > 1:
            keyhot(*kps)  # kps = ['shift', 'ctrl', 'z']
    elif len(words) > 1 and words[1] in words_num:
        try:
            if len(kps) == 1:
                one_num = sum(words_num[word] for word in words[1:])
                print(f"{YEL}*{LYE}{one_num}{LCY}", end="")
                for ione in range(one_num):
                    key_press(*kps)
            elif len(kps) > 1:
                one_num = sum(words_num[word] for word in words[1:])
                print(f"{YEL}*{LYE}{one_num}{LCY}", end="")
                for ione in range(one_num):
                    keyhot(*kps)
        except KeyError:
            print(f"\b {WHI}({GRE}{words[0]} {YEL}+ {GRE}число{WHI}) {YEL}!={LRE}", end="")


print(Fore.RESET, end='')

vosk.SetLogLevel(-1)  # удаляем логи

# Инициализация распознавателя с основной моделью


model_urls = [
    "https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip",
    "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
]

models_directory = "voskmodels"

try:
    current_model = Model(model1)
except Exception as e:
    print("Exception:", str(e))
    printt(LRE + "Не удалось открыть модель.\n")
    loader.download_generator()
    printt("Идет загрузка и распаковка моделей распознования подождите...\n")

    import zipfile

    os.makedirs(models_directory, exist_ok=True)

    for model_url in model_urls:
        # Извлечь имя файла из URL
        filename = model_url.split("/")[-1]

        # Загрузите ZIP-файл модели
        response = requests.get(model_url)
        with open(os.path.join(models_directory, filename), "wb") as file:
            file.write(response.content)

        # Извлеките ZIP-файлы
        with zipfile.ZipFile(os.path.join(models_directory, filename), "r") as zip_ref:
            zip_ref.extractall(models_directory)

        # Удалить ZIP-файлы
        os.remove(os.path.join(models_directory, filename))
    printt(LGR + "Модели скачались и распаковались успешно.")
    current_model = Model(model1)
    rec = KaldiRecognizer(current_model, 48000)
rec = KaldiRecognizer(current_model, 48000)

# Инициализация распознавателя с английской моделью
english_model = Model(model2)
receng = KaldiRecognizer(english_model, 48000)

# Инициализация аудио потока
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    frames_per_buffer=4000
)
stream.start_stream()

# Определение функции, которая будет озвучивать текст
speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()
speak.Volume = 100  # громкость
speakrate_set = 4  # скорость


# Функция для смены модели
def change_model(new_model):
    vosk.SetLogLevel(1)
    global current_model, rec
    # Закрытие текущей модели и распознавателя
    current_model = None
    rec = None
    # Инициализация новой модели и распознавателя
    print(" ")
    loader.download_generator()
    current_model = Model(new_model)
    rec = KaldiRecognizer(current_model, 48000)
    print(LCY + "\r Модель распознавания изменена на -" + SRA, LGR + new_model)


current_voice = "Microsoft Pavel Mobile"


def speak_irina_tts(speak_text):  # для озвучки ириной
    for voice in voices:
        if voice.GetAttribute("Name") == "Microsoft Irina Desktop":
            speak.Rate = speakrate_set
            speak.Voice = voice
            speak.speak(speak_text)
            tts.runAndWait()


def speak_pavel_tts(speak_text):  # для озвучки Павлом
    for voice in voices:
        if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
            speak.Rate = speakrate_set
            speak.Voice = voice
            speak.speak(speak_text)
            tts.runAndWait()


def switch_voice(voice_name):  # переключение голоса
    global current_voice
    current_voice = voice_name


def speak_tts(speak_text):  # стандартная озвучка с текущим голосом
    for voice in voices:
        if voice.GetAttribute("Name") == current_voice:
            speak.Rate = speakrate_set
            speak.Voice = voice
            speak.speak(speak_text)
            tts.runAndWait()


def set_speak_rate(speak_rate):  # установка скорости озвучивания
    global speakrate_set
    speakrate_set = speak_rate


random_voice = [speak_pavel_tts, speak_irina_tts]


def pause_mode():
    print(LCY + '\n ʕ℗•ᴥ•℗ʔ' + SRA, end='')
    speak_tts("режим паузы!")
    while True:
        if rec.AcceptWaveform(stream.read(4000)):
            paumpt = rec.Result()[13:-2]
            if paumpt in ('"стена"', '"стенка"', '"стену"', '"строй"', '"стройка"', '"построй"'):
                loader.waal_generator()
            elif paumpt in ('"бред"', '"умом"'):
                loader.smile_generator()
                loader.letters_random()
            elif paumpt in ('"ассистент"', '"помощник"', '"запуск"', '"запустить"', '"запусти"', '"обычный режим"'):
                print(f'\n{LGR} \ʕ•ᴥ•ʔ/{SRA}')
                speak_tts("запускаю обычный режим!")
                break
            elif paumpt == '"громкость"':
                print(LCY + '♪' + SRA, end='')
                key_press('volumemute')
            elif paumpt == '"тест"':
                os.startfile(f"{path_to_shortcut}тест")
            elif paumpt in ('"пауза"', '"паузы"', '"блокировка"', '"остановка"', '"режим паузы"'):
                speak_tts("я итак на паузе!")
            elif paumpt in ('"слушай"', '"слышь"', '"слышь ты"', '"слышишь"', '"слэш"'):
                speak_tts("я на паузе если что!")
            elif paumpt in ('"перезапуск"', '"рестарт"'):
                print(LRE + '\n ʕ/·ᴥ·ʔ/ Bye! ' + SRA)
                os.startfile(f"\\{path_to_shortcut}{assistant_window}")
                exit()
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("win"):
            assistant.minimize()
            assistant.restore()
            print(f'\n{LGR} \ʕ•ᴥ•ʔ/{SRA}')
            speak_tts("обычный режим!")
            break


if __name__ == '__main__':

    # Находим окно с именем 'ассистент'
    assistant = None
    try:
        assistant = pyautogui.getWindowsWithTitle(assistant_window)[0]
        assistant.moveTo(-8, 0)
        assistant.resizeTo(849, 327)
    except Exception as e:
        printt(f"\r                                                   (!o_O) ярлык --> {assistant_window}\r")
        # Получить путь к текущему скрипту
        script_path = os.path.abspath(__file__)

        # Получить путь к папке, в которой находится скрипт
        script_directory = os.path.dirname(script_path)

        # Проверить наличие ярлыка ассистента
        assistant_link_path = os.path.join(script_directory, path_to_shortcut + assistant_window + ".lnk")
        if not os.path.isfile(assistant_link_path):
            # Создать объект ярлыка
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(assistant_link_path)
            # Установить путь к исходному скрипту в ярлыке
            shortcut.TargetPath = script_path
            # Установить имя ярлыка
            shortcut.Description = assistant_window
            # Установить рабочую папку
            shortcut.WorkingDirectory = script_directory
            # Сохранить ярлык
            shortcut.Save()
        print(e)
        os.startfile(path_to_shortcut + assistant_window)
        exit()

    #: состав словаря из названий ярлыков
    file_list = os.listdir(path_to_shortcut)
    lnk_files = [f for f in file_list if f.endswith(".lnk") or f.endswith(".url")]
    labels = []  # словарь названий ярлыков
    for lnk_file in lnk_files:
        full_path = os.path.join(path_to_shortcut, lnk_file)
        label = lnk_file[:-4]  # удаляем последние четыре символа
        labels.append(label)

    translator = Translator()
    tts.runAndWait()  # ! иногда наверно помогает от отключения микрофона
    loader_screen_rimtex()
    print(LGR + "\n ʕ/•ᴥ•ʔ/ Hi! " + SRA)

    while True:
        # конвертер команд старт
        caps_lock_state_check = win32api.GetKeyState(0x14)
        num_lock_state_check = win32api.GetKeyState(0x90)

        # -: режим паузы
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("win"):
            pause_mode()

        #: Запись на русском # при включённом Caps Lock
        elif (caps_lock_state_check == 1 or caps_lock_state_check == -127) and \
                (num_lock_state_check != 1 and num_lock_state_check != -127):
            time.sleep(.2)
            print(LYE + "›", end="")
            while True:
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("win"):
                    pause_mode()
                if rec.AcceptWaveform(stream.read(4000)):
                    prompt = rec.Result()[13:-2]
                    if prompt != '""':
                        keyrus_write(prompt[1:-1])
                if keyboard.is_pressed("numlock") or keyboard.is_pressed("capslock"):
                    print(LRE + "‹" + SRA, end="")
                    break
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt"):
                    assistant.minimize()
                    assistant.restore()
                    turn_off_locks()
                    print(LRE + "‹" + SRA, end="")
                    break

        #: Запись на английском # при включённом Num Lock
        elif (num_lock_state_check == 1 or num_lock_state_check == -127) and \
                (caps_lock_state_check != 1 and caps_lock_state_check != -127):
            time.sleep(.2)
            print(YEL + f"›", end="")
            while True:
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("win"):
                    pause_mode()
                if receng.AcceptWaveform(stream.read(4000)):
                    prompteng = receng.Result()[13:-2]
                    if prompteng != '""':
                        key_write(prompteng[1:-1])
                if keyboard.is_pressed("numlock") or keyboard.is_pressed("capslock"):
                    print(LRE + "‹" + SRA, end="")
                    break
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt"):
                    assistant.minimize()
                    assistant.restore()
                    turn_off_locks()
                    print(LRE + "‹" + SRA, end="")
                    break

        #: Запись с переводом # при включённом Caps Lock и Num Lock
        elif (num_lock_state_check == 1 or num_lock_state_check == -127) and \
                (caps_lock_state_check == 1 or caps_lock_state_check == -127):
            time.sleep(.2)
            print(LGR + "»", end="")
            while True:
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("win"):
                    pause_mode()
                if rec.AcceptWaveform(stream.read(4000)):
                    prompt = rec.Result()[13:-2]
                    if prompt != '""':
                        prompttrans = str(prompt[1:-1])
                        try:
                            trans = translator.translate(prompttrans, "english", "russian")
                            keytrans_write(f"{trans}")
                        except Exception as e:
                            print(f" {LRE}! переводчик: ", e)
                if keyboard.is_pressed("numlock") or keyboard.is_pressed("capslock"):
                    print(LRE + "«" + SRA, end="")
                    break
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt"):
                    assistant.minimize()
                    assistant.restore()
                    turn_off_locks()
                    print(LRE + "«" + SRA, end="")
                    break

        elif rec.AcceptWaveform(stream.read(4000)):  # - {   "text" : "распознавание голоса" }
            try:
                prompt = rec.Result()[13:-2]  # - "распознавание голоса"
                words = prompt[1:-1].split()  # - ['распознавание', 'голоса'] - words[0], words[1]

                #: для команд
                if prompt in ('"показать команды"', '"покажи команды"'):
                    print(f'\n{convert_paint()}')
                elif prompt in ('"команды на русском"', '"покажи на русском"', '"команды перевод"'):
                    print(f'\n{convert_trans()}')
                elif prompt in ('"покажи"', '"покажешь"'):
                    print(f'\n{convert_delete()}')
                elif prompt in ('"показать"', '"показывай"'):
                    assistant.resizeTo(1170, 1407)
                    print(f'\n{convert_delete()}')

                #: смена модели распознавания
                elif len(words) == 2 and any(words in prompt[1:-1] for words in ('модель', 'model')):
                    try:
                        if any(words in prompt[1:-1] for words in ('один', 'one')):
                            change_model(model1)
                        if any(words in prompt[1:-1] for words in ('два', 'two', 'to')):
                            change_model(model2)
                        if any(words in prompt[1:-1] for words in ('три', 'free', 'three')):
                            change_model(model3)
                            speak_pavel_tts("тяжёлая русская модель загружена!")
                        if any(words in prompt[1:-1] for words in ('четыре', 'four', 'for')):
                            change_model(model4)
                            speak_irina_tts("тяжёлая английская модель загружена!")
                    except Exception as e:
                        change_model(model1)
                        print(LRE, e)

                #: режим паузы # также можно зажать комбинацию ctrl-win
                elif prompt in ('"пауза"', '"паузы"', '"блокировка"', '"остановка"', '"режим паузы"'):
                    pause_mode()

                #: для быстрого поиска
                elif len(words) > 0 and words[0] in ('поиск', 'команду', 'команда', 'погнали', 'поехали'):
                    if len(words) == 1:
                        keyhot('ctrl', 'f')
                    if len(words) > 1:  # -: поиск из буфера
                        # os.startfile(f"{path_to_shortcut}питон")  # - стартуем нужную прогу
                        keywrite = prompt[len(words[0]) + 2:-1]  # - минус первое слово
                        print(f"{LGR}˃{LCY} п {LMA}? ", end='')
                        time.sleep(.1)
                        click_print()
                        keyhot('ctrl', 'f')
                        keyboard.write(f"{keywrite}")
                        key_press('enter')

                #: найти найди пуск
                elif len(words) == 1 and words[0] in ('найти', 'найди'):
                    keyhot("ctrl", "f")
                elif len(words) == 1 and words[0] == 'пуск':
                    key_press("win")
                elif len(words) > 1 and words[0] == 'найти':
                    write_prompt = prompt[6:-1]  # - убираем первое слово и кавычки из фразы
                    key_press("win")  # - Открываем окно найти в пуске
                    time.sleep(0.2)  # - Ждем, пока окно загрузится
                    keyboard.write(write_prompt)  # - Вводим слова
                    time.sleep(0.2)  # - Ждем на всякий случай
                    key_press("enter")  # - Нажимаем Enter
                elif len(words) > 1 and words[0] == 'найди':  # с переводом на английский
                    trans_prompt = prompt[6:-1]
                    try:
                        trans = translator.translate(trans_prompt, "english", "russian")
                        keyhot("win", "q")
                        time.sleep(0.2)
                        keyboard.write(f"{trans}")
                        print(f"{YEL} {trans}", end=' ')
                        time.sleep(0.2)
                        key_press("enter")
                    except Exception as e:
                        print(f" {LRE}! переводчик: ", e)

                #: окей гугл
                elif re.match('"окей гугл', prompt):  # + слова
                    try:
                        webbrowser.open('https://www.google.com/search?q=' + prompt[11:-1])
                        print(LGR + "G" + LCY, end='')
                    except OSError:
                        print(LRE + "G" + SRA, end='')

                #: установка скорости озвучивания голоса # + числа
                elif len(words) >= 2 \
                        and re.match(r'скорост\w?\b|озвуч\w{0,5}\b|голос\w{0,3}\b', words[0]) \
                        and words[1] in words_num:
                    speak_num = words_num[words[1]]
                    speakrate_set = speak_num
                    print(f'{LRE}ϟ{LYE}♪{LGR}☼ ', end='')
                    sk_show = '⁞'
                    for i in range(speak_num):
                        print(sk_show, sep='', end='', flush=True)
                        time.sleep(0.03)
                    print(f' {GRE}{speak_num}{LCY}', end='')
                    speak_tts(f'скорость озвучки {speak_num}')

                #: переключение голоса
                elif prompt == '"павел"':
                    switch_voice("Microsoft Pavel Mobile")
                    print(f' {LRE}ϟ{LYE}♪{LGR}☼{LYE}Pavel{LCY}', end='')
                    speak_pavel_tts("Microsoft Pavel Mobile")
                elif prompt == '"ирина"':
                    switch_voice("Microsoft Irina Desktop")
                    print(f' {LRE}ϟ{LYE}♪{LGR}☼{LYE}Irina{LCY}', end='')
                    speak_irina_tts("Microsoft Irina Desktop")

                #: нажатие клавиш # + число для повторений
                elif 7 > len(words) > 0 and words[0] in ('контрол', 'контур', 'контр', 'контроль'):
                    kps = ['Control']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('альт', 'аль'):
                    kps = ['alt']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('шифт', 'шрифт'):
                    kps = ['shift']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('пробел', 'робел ', 'спэйс'):
                    kps = ['Space']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('стереть', 'стирание', 'сотри'):
                    kps = ['backspace']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('энтер', 'эндер', 'интер', 'нтр'):
                    kps = ['enter']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('эскейп', 'выход', 'выйти'):
                    kps = ['Escape']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('делит', 'удали', 'удалить', 'удаления', 'удали', 'удаление'):
                    kps = ['delete']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('таб', 'тоб', 'смена', 'сменить', 'поменять'):
                    kps = ['tab']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('взад', 'назад'):
                    kps = ['browserback']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('вперёд', 'перед', 'наперёд'):
                    kps = ['browserforward']
                    numbers_key()
                #: клавиши стрелки # + число для повторений
                elif 7 > len(words) > 0 and re.match(r'^.{0,3}лев.{0,3}$', words[0]):
                    kps = ['left']
                    numbers_key()
                elif 7 > len(words) > 0 and re.match(r'^.{0,3}прав.{0,3}$', words[0]):
                    kps = ['right']
                    numbers_key()
                elif 7 > len(words) > 0 and re.match(r'^.{0,3}верх.{0,3}$', words[0]):
                    kps = ['up']
                    numbers_key()
                elif 7 > len(words) > 0 and re.match(r'^.{0,3}низ.{0,3}$', words[0]):
                    kps = ['down']
                    numbers_key()
                #: комбинации клавиш # + число для повторений
                elif 7 > len(words) > 0 and words[0] in ('уничтожь', 'уничтожить', 'уничтожать', 'уничтожает'):
                    kps = ['shift', 'delete']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('отмени', 'отмена', 'отменить', 'отменил', 'отмена'):
                    kps = ['ctrl', 'z']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('верни', 'вернул', 'вернуть', 'вернуть'):
                    kps = ['shift', 'ctrl', 'z']
                    numbers_key()
                elif 7 > len(words) > 0 and words[0] in ('вставь', 'ставка', 'вставка', 'вставить', 'ставь'):
                    kps = ['ctrlleft', 'v']
                    numbers_key()
                elif re.match('"вкладку|"вкладка|"крестик', prompt):  # закрытие вкладки Chrome
                    kps = ['ctrlleft', 'w']
                    numbers_key()
                #: одноразовое нажатие
                elif re.match(r'"\w?копир\w{0,6}\b"', prompt):
                    keyhot('ctrlleft', 'c')
                elif re.match(r'"\w{0,2}хран\w{0,5}\b"', prompt):
                    keyhot('ctrlleft', 's')
                elif re.match(r'"буфер\w?\b"|"спис\w{0,2}\b"', prompt):
                    keyhot('win', 'v')
                elif re.match(r'"раскладк\w?\b"|"клавиатур\w{0,2}\b"', prompt):
                    keyhot('win', 'space')
                elif prompt in ('"снимок"', '"скрин"', '"снимок экрана"'):
                    key_press('printscreen')

                #: работа с окнами
                elif len(words) == 1 and re.match(r'разв\w{0,6}\b', words[0]):
                    keyhot('win', 'Up')
                elif len(words) == 1 and re.match(r'свер\w{0,4}\b', words[0]):
                    keyhot('win', 'Down')
                elif len(words) == 1 and re.match(r'закр\w{0,4}\b', words[0]):
                    keyhot('altleft', 'F4')
                elif prompt in ('"окна"', '"окошки"', '"вин таб"', '"показать окна"', '"режим окон"'):
                    keyhot('win', 'tab')
                elif prompt in ('"свернуть все"', '"сверни все"', '"чисто"'):
                    keyhot('win', 'd')
                elif prompt in ('"свернуть лишнее"', '"свернуть лишнее"', '"лишнее"'):
                    keyhot('win', 'Home')
                elif prompt in ('"обновить"', '"обнови"', '"об нова"', '"эф пять"'):
                    key_press("f5")
                elif 3 > len(words) > 0 and words[0] == 'окно':
                    if 2 >= len(words) > 1 and re.match(r'^.{0,3}прав.{0,3}$', words[1]):
                        keyhot('win', 'Right')
                    if 2 >= len(words) > 1 and re.match(r'^.{0,3}лев.{0,3}$', words[1]):
                        keyhot('win', 'Left')
                    if 2 >= len(words) > 1 and re.match(r'^.{0,3}верх.{0,3}$', words[1]):
                        keyhot('win', 'Up')
                    if 2 >= len(words) > 1 and re.match(r'^.{0,3}низ.{0,3}$', words[1]):
                        keyhot('win', 'Down')

                #: закрывание всех окон
                elif prompt in ('"убей всех"', '"растрелли"', '"расстрел"', '"застрели"', '"расстрел окон"'
                                , '"расстреле"', '"расстрелять"'):
                    print(f"""{LRE} ({LGR}√{LRE}¬_¬)ԅ⌐╦╦═─‒=═≡Ξ{SRA}""", end='')
                    assistant.minimize()
                    assistant.restore()
                    os.startfile(f"{path_to_shortcut}{assistant_window}")
                    key_down('alt')  # ! не забыть отжать альт
                    key_press('tab')
                    key_press('right')
                    for i in range(10):
                        for ici in range(100):
                            key_press('delete')
                        key_press('right')

                #: для записи чисел # просто говорим числа
                elif 7 > len(words) > 0 and all(word in words_num for word in words):
                    nums = sum(words_num[word] for word in words[0:])
                    key_write(f"{nums}")

                #: подсчёт длинны строки - количества символов
                elif prompt in ('"посчитай"', '"под считай"', '"количество"', '"количество символов"'):
                    win32clipboard.OpenClipboard()
                    lenofsymbols = len(str(win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)))
                    win32clipboard.CloseClipboard()
                    print(f'{YEL}{lenofsymbols}{LCY}', end='')
                    speak_tts(f"{lenofsymbols}")

                #: запись даты
                elif prompt == '"дата"' or prompt == '"дату"':
                    keyboard.write(date.today().strftime("%d.%m.%Y "))
                    keyboard.write(datetime.now().strftime("%H,%M,%S")[0:5])  # - убрал секунды

                #: озвучка выделенного текста
                elif prompt in ('"озвучь"', '"озвучка"', '"озвучить"', '"озвучивает"', '"озвучивать"'):
                    print(f"{LYE}♪", end='')
                    keyhot('ctrlleft', 'c')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    speak_tts(f"{text}")

                #: озвучка выделенного текста с переводом
                elif prompt in ('"зачитай"', '"прочитай"', '"прочти"', '"прочитать"'):
                    keyhot('ctrlleft', 'c')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    if re.search('[a-zA-Z]', text):
                        print(f"{LGR}♪", end='')
                        trans = translator.translate(text, "russian")
                        speak_tts(f"{trans}")
                    elif re.search('[а-яА-Я]', text):
                        print(f"{LGR}♪", end='')
                        trans = translator.translate(text, "russian", "uk")
                        speak_tts(f"{trans}")
                    else:
                        print(f"{LYE}♪", end='')
                        speak_tts(f"{text}")

                #: вставка из буфера # с авто переводом english\русский
                elif re.match(r'"перев\w{0,3}\b"', prompt):
                    print(f"{LGR}♫", end='')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    if re.search('[а-яА-Я]', text):
                        trans = translator.translate(text, "english")
                    else:
                        trans = translator.translate(text, "russian")
                    keyboard.write(f"{trans}")

                #: вставка из буфера # з перекладом на українську
                elif re.match(r'"украинск\w{0,2}\b"', prompt):
                    print(f"{LGR}♫", end='')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    if re.search('[а-яА-Я]', text):
                        trans = translator.translate(text, "uk", "russian")
                    else:
                        trans = translator.translate(text, "uk", "english")
                    keyboard.write(f"{trans}")

                #: вставка из буфера # с переводом на русский
                elif re.match(r'"русск\w{0,2}\b"', prompt):
                    print(f"{LGR}♫", end='')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    if re.search('[а-яА-Я]', text):
                        trans = translator.translate(text, "russian", "uk")
                    else:
                        trans = translator.translate(text, "russian", "english")
                    keyboard.write(f"{trans}")

                #: одноразовое нажатие # если слово последнее
                elif 7 > len(words) > 0 and words[-1] in ('капс', 'пиши', 'пишем', 'напиши', 'букве', 'буквы'):
                    key_press('CapsLock')
                elif 7 > len(words) > 0 and words[-1] in ('цифры', 'цифра', 'инглиш', 'английски', 'английским'):
                    key_press('numlock')
                elif 7 > len(words) > 0 and words[-1] in ('переведи', 'переводи', 'переводом', 'переводчик'):
                    key_press('CapsLock')
                    key_press('numlock')

                #: Управление системой
                elif re.match(r'"компьютер перезагруз\w{0,4}\b', prompt):
                    os.system('shutdown /r /t 1')
                elif re.match(r'"компьютер выключ\w{0,4}\b', prompt):
                    os.system('shutdown /s /t 1')
                elif prompt in ('"компьютер спящий режим"', '"компьютер спячка"'):
                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                elif prompt in ('"компьютер сон"', '"компьютер спать"', '"компьютер засни"'):
                    os.system('shutdown /h')
                elif prompt in ('"тьма"', '"закат"'):
                    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)
                elif prompt in ('"свет"', '"расцвет"', '"рассвет"'):
                    key_press('ctrl')
                    # - ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)

                #: установка громкости системы
                elif any(words in prompt[1:-1] for words in
                         ('заткнись на хрен', 'не так громко', 'слишком громко', 'минус громкость')) \
                        or prompt[1:-1] in ('громко', 'громкость', 'мут'):
                    key_press('volumemute')
                elif 3 >= len(words) >= 2 and words[0] == 'громкость' and words[1] in words_num:
                    on_num = sum(words_num[word] for word in words[1:]) // 2
                    print(LCY + '♪', end='')
                    for i in range(50):  # - ! костыль
                        pyautogui.press('volumedown')
                    for i in range(on_num):
                        pyautogui.press('volumeup')

                #: перезагрузка ассистента
                elif prompt in ('"тихо"', '"тихa"', '"старт"'):
                    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
                    os.startfile(f"{path_to_shortcut}{assistant_window}")
                    exit()
                elif prompt == '"рестарт"' or re.match(r'"переза\w{0,6}\b"', prompt):
                    assistant.moveRel(0, 20)
                    print(LRE, end="")
                    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
                    os.startfile(f"{path_to_shortcut}{assistant_window}")
                    for i in range(15):
                        printt('\n')
                    printt(' ʕ/·ᴥ·ʔ/')
                    loader.download_bye()
                    time.sleep(2)
                    exit()

                #: идеи
                elif len(words) == 2 and words[1] in ('идеи', 'идея', 'идею', 'идейку', 'идей'):
                    if words[0] in ('озвучь', 'зачитай', 'прочти', 'озвучить'):  # озвучка идей
                        file = open(ideas, "r", encoding='utf-8')
                        contents = file.read()
                        speak_tts(contents)
                    elif words[0] in ('какие', 'покажи', 'где', 'показывай'):  # отображение идей
                        file = open(ideas, "r", encoding='utf-8')
                        contents = file.read()
                        print(contents)
                    elif words[0] in ('записать', 'запиши', 'запись', 'записывай'):  # записать идею
                        print(LMA + "\n (?o_O) " + SRA)
                        keyhot('alt', 'tab')
                        os.startfile(ideas)
                        speak.Rate = 8
                        speak_tts("говори быстрей пока не убежала")
                        key_press("down")
                        key_press("enter")
                        key_press("up")
                        keyboard.write("! - ")
                        time.sleep(0.5)
                        key_press('CapsLock')

                #: напоминалка
                elif len(words) == 1 and words[0] in ('напомнить', 'вспомнить'):
                    print(LMA + "\n (!o_O) " + SRA)
                    keyhot('alt', 'tab')
                    os.startfile(reminder)
                    speak_tts("главное не забыть!")
                    key_press("down")
                    key_press("enter")
                    key_press("up")
                    keyboard.write("! - ")
                    time.sleep(0.5)
                    key_press('CapsLock')
                elif prompt in ('"напомни"', '"вспомни"', '"напоминай"', '"вспоминай"'):
                    file = open(reminder, "r", encoding='utf-8')
                    contents = file.read()
                    loader.download_generator()
                    print(f"{SRA}({LGR}√{SRA}¬_¬)ԅ⌐╦╦═─")
                    print(contents)
                    speak_tts(contents)

                #: озвучка проблем
                elif prompt in ('"проблемы"', '"что за проблема"', '"в чем проблема"', '"проблема"',
                                '"да блядь че за хуйня"', '"почему не работает"'):
                    speak_tts(""
                              "1 ! переводчик может не работать с впн"
                              "2 ! иногда ассистент морозица. возможно помогает tts"
                              "3 ! при старте на русской раскладке некоторые команды могут не работать"
                              )

                #: ♫ включение случайной музыки
                elif prompt in ('"радио"', '"включи радио"'):
                    print(f"{RED}Ϟ{LMA}?{GRE}♫{CYA} ˃˃˃{GRE}", end='')
                    play_music()

                #: ♫ включение случайной музыки в одной папке
                elif prompt in ('"включи музыку"', '"включить музыку"', '"музычка"', '"музыку"'):
                    files = os.listdir(dir_path)
                    print(f" {RED}Ϟ{YEL}♪{GRE}♫{CYA} ˃˃˃ {WHI}{dir_path}{LGR}", end='')
                    if not files:
                        print("The directory is empty.")
                    else:
                        random_file = random.choice(files)
                        file_path = os.path.join(dir_path, random_file)
                        os.startfile(file_path)

                #: ♫ включение случайной музыки в другой папке
                elif prompt in ('"автомата"', '"мир автомата"', '"нир автомата"'):
                    dir_path = rf"{dir_path}\NieR Automata OST"
                    files = os.listdir(dir_path)
                    filtered_files = [f for f in files if "NieR Automata" in f and f.endswith(".mp3")]
                    print(f"{RED}Ϟ{CYA}Ǽ{GRE}♫{CYA} ˃˃˃{GRE}", end='')
                    if not filtered_files:
                        print("There are no files that match the filter criteria.")
                    else:
                        random_file = random.choice(filtered_files)
                        file_path = os.path.join(dir_path, random_file)
                        os.startfile(file_path)

                #: работа с мышкой
                elif prompt == '"координаты"':
                    x, y = pyautogui.position()
                    print(f"{LYE}({x}, {y}){LCY}", end='')
                elif prompt in ('"тэк"', '"клик"', '"кликни"', '"кликай"', '"кликнуть"'):
                    click_print()

                #: зажать - отпустить
                elif len(words) == 1 and words[0] in ('зажми', 'зажать', 'зажал', 'зажимать', 'схвати', 'схватить'):
                    print(f"{LCY}∆{LGR}▼{LCY}", end='')
                    pyautogui.mouseDown()
                elif len(words) == 1 and words[0] in ('отпусти', 'отпускай', 'отпустить', 'пусти', 'отпускай', 'отжал'):
                    print(f"{LCY}∆{LGR}▲{LCY}", end='')
                    pyautogui.mouseUp()

                #: клик # + число
                elif 7 > len(words) > 1 and re.match(r'клик\w{0,4}\b', words[0]):
                    try:
                        num = sum(words_num[word] for word in words[1:])
                        for i in range(num):
                            click_print()
                    except KeyError:
                        print(f"{LGR}{words[0]} {YEL}+ {LCY}число {YEL}!={LRE}", end="")

                #: курсор в центр экрана
                elif prompt in ('"центр"', '"в центр"', '"на центр"'):
                    print(f"{LCY}∆{LGR}○{LCY}", end='')
                    screen_width, screen_height = pyautogui.size()
                    pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=0.25)

                #: промотка колеса # + число
                elif 5 > len(words) > 0 and words[0] in ('промотай', 'мотай'):  # ↓
                    if len(words) == 1:
                        print(f"{LGR}↓{LCY}∆ ", end="")
                        pyautogui.scroll(-1500)
                    elif len(words) > 1 and words[1] in words_num:
                        num = sum(words_num[word] for word in words[1:])
                        for i in range(num):
                            pyautogui.scroll(-1500)
                        print(f"{LGR}↓{GRE}{num}{LCY}∆ ", end="")
                elif 5 > len(words) > 0 and re.match(r'колес\w{0,3}\b', words[0]):  # ↑
                    if len(words) == 1:
                        print(f"{LGR}↑{LCY}∆ ", end="")
                        pyautogui.scroll(1500)
                    elif len(words) > 1 and words[1] in words_num:
                        num = sum(words_num[word] for word in words[1:])
                        for i in range(num):
                            pyautogui.scroll(1500)
                        print(f"{LGR}↑{GRE}{num}{LCY}∆ ", end="")

                #: ctrl плюс промотка колеса # + число
                elif 5 > len(words) > 0 and words[0] in ('дальше', 'подальше', 'меньше', 'поменьше'):
                    if len(words) == 1:
                        key_down('ctrl')
                        pyautogui.scroll(-1500)
                        key_up('ctrl')
                    elif len(words) > 1 and words[1] in words_num:
                        num = sum(words_num[word] for word in words[1:])
                        key_down('ctrl')
                        for i in range(num):
                            pyautogui.scroll(-1500)
                        key_up('ctrl')
                elif 5 > len(words) > 0 and words[0] in ('ближе', 'поближе', 'больше', 'побольше'):
                    if len(words) == 1:
                        key_down('ctrl')
                        pyautogui.scroll(1500)
                        key_up('ctrl')
                    elif len(words) > 1 and words[1] in words_num:
                        num = sum(words_num[word] for word in words[1:])
                        key_down('ctrl')
                        for i in range(num):
                            pyautogui.scroll(1500)
                        key_up('ctrl')

                #: курсор + 1-2 направление(я) # + числа
                elif 7 > len(words) > 1 and words[0] in ('курсор', 'корсар', 'курсора', 'курсором'):
                    try:
                        if re.match(r'^.{0,3}прав.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:] * 10)
                                pyautogui.moveRel(nums, 0)
                            if words[2] not in words_num:
                                numss = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(numss, 0)
                                cursor_direction()
                        if re.match(r'^.{0,3}низ.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:] * 10)
                                pyautogui.moveRel(0, nums)
                            if words[2] not in words_num:
                                numss = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(0, numss)
                                cursor_direction()
                        if re.match(r'^.{0,3}лев.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:] * 10)
                                pyautogui.moveRel(-nums, 0)
                            if words[2] not in words_num:
                                numss = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(-numss, 0)
                                cursor_direction()
                        if re.match(r'^.{0,3}верх.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:] * 10)
                                pyautogui.moveRel(0, -nums)
                            if words[2] not in words_num:
                                numss = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(0, -numss)
                                cursor_direction()
                    except IndexError:
                        print(f" {WHI}({LGR}{words[0]} + направление(я) + числа{WHI}) {YEL}!= {LRE}", end='')
                    except Exception as e:
                        print(f"{LRE}{e} {WHI}({LGR}{words[0]} + направление(я) + числа{WHI}) {YEL}!= {LRE}", end='')

                #: рисование квадрата # + числа
                elif 7 > len(words) > 1 and words[0] in ('нарисуй', 'рисуй', 'рисунок', 'рисования', 'рисование') and \
                        words[1] == 'квадрат':
                    try:
                        repeat_num = sum(words_num[word] for word in words[2:])
                        num_ns = repeat_num
                        pyautogui.mouseDown()
                        pyautogui.moveRel(num_ns, 0)
                        pyautogui.moveRel(0, num_ns)
                        pyautogui.moveRel(-num_ns, 0)
                        pyautogui.moveRel(0, -num_ns)
                        pyautogui.mouseUp()
                        print(f"{LGR}□{YEL}*{LYE}{num_ns}{LCY}", end='')
                    except Exception as e:
                        print(f"{LRE}■ {LGR}{words[0]} + {words[1]} + {LCY}числа {YEL}!= {LRE}", e, end='')

                #: для раздупления
                elif len(words) == 1 and words[0] == 'пук':  # альт таб
                    print(LRE + "↔1 ", end='')
                    keyhot('alt', 'tab')
                elif len(words) == 1 and words[0] == 'бах':  # вин таб х2
                    print(LRE + "↕2 ", end='')
                    keyhot('win', 'tab')
                    time.sleep(.5)
                    keyhot('win', 'tab')
                elif len(words) == 1 and words[0] == 'бабах':  # альт таб х2 - вин таб х2
                    print(LRE + "↔2↕2 ", end='')
                    keyhot('alt', 'tab')
                    time.sleep(.5)
                    keyhot('alt', 'tab')
                    time.sleep(.5)
                    keyhot('win', 'tab')
                    time.sleep(.5)
                    keyhot('win', 'tab')
                elif len(words) > 1 and words[0] == 'раз':  # альт таб равен количеству слов после 'раз'
                    print(LRE + "↔+w▸ ", end='')
                    puk_length = len(words)
                    key_down('alt')
                    for i in range(puk_length):
                        time.sleep(.1)
                        key_press('tab')
                    key_up('alt')
                elif prompt in ('"эй"', '"ты где"', '"ты тут"', '"себя"', '"в себя"', '"покажись"', '"панель"'):
                    assistant.minimize()  # - сворачивание
                    assistant.restore()  # - раздупляем восстанавливанием
                    print(LGR + "ø", end="")

                # -: встроенные команды из keyboard_scripts.py
                elif prompt != '""':
                    from keyboard_scripts import \
                        key_symbols, rimtex_pycharm, rimtex_personal, rimtex_reactions, scripts_others

                    key_symbols(prompt)
                    scripts_others(words)

                    rimtex_pycharm(prompt)
                    rimtex_personal(prompt)
                    rimtex_reactions(prompt, words)

                # -: открываем все своё с ярлыков
                if prompt != '""' and 9 > len(words) > 0 and prompt[1:-1] in labels:
                    try:
                        os.startfile(f"{path_to_shortcut}{prompt[1:-1]}")
                        print(LCY + "√", end='')
                    except FileNotFoundError:
                        try:
                            os.startfile(f"{path_to_shortcut}{prompt[1:-1]}.url")
                            print(LCY + "e√", end='')
                        except FileNotFoundError:
                            print(Fore.WHITE + "_", end="")  # - индикатор попытки открытия файла

                if prompt != '""':  # - голос в консоль
                    print(f' {prompt[1:-1]}{SRA}', sep='', end=' ')

            # конвертер команд конец
            except Exception as e:
                print(traceback.format_exc())
                print(f"{LRE} ʕ•ᴥ•ʔʃ Ошибка :{SRA}", e)
