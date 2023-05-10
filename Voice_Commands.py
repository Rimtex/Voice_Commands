import os

try:
    import traceback
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
    from python_translator import Translator
    import webbrowser
    from urllib.parse import quote
except ImportError:
    print("Trying to Install required modules: requirements.txt")
    #  os.system('pip install -r "requirements.txt"')
    os.system('pip install --upgrade -r "requirements.txt"')
    import traceback
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
    from python_translator import Translator
    import webbrowser
    from urllib.parse import quote

from keyboard_scripts import script_writing_function, key_press, keyhot, key_down, key_write, key_up, \
    click_print_cor, click_print, keyrus_write, keytrans_write
import loader
from loader import loader_screen_rimtex
import vocabulary
from vocabulary import words_num
from converter import convert_paint, convert_trans, convert_delete

from address_config import path_to_shortcut, ideas, reminder, requirements_path, dir_path, model1, model2, model3, \
    model4

py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)  # переключение на английскую раскладку

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

# Определение функции, которая будет озвучивать текст
speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()
tts = pyttsx3.init()  # без этого пока работает
tts.runAndWait()  # инициализация распознавания ! иногда наверно помогает от отключения микрофона


#: направление курсора
def cursor_direction():
    numss = sum(words_num[word] for word in words[3:] * 10)
    if re.match(r'^.{0,3}прав.{0,3}$', words[2]):
        pyautogui.moveRel(numss, 0)
    if re.match(r'^.{0,3}низ.{0,3}$', words[2]):
        pyautogui.moveRel(0, numss)
    if re.match(r'^.{0,3}лев.{0,3}$', words[2]):
        pyautogui.moveRel(-numss, 0)
    if re.match(r'^.{0,3}верх.{0,3}$', words[2]):
        pyautogui.moveRel(0, -numss)


def play_music():  # для проигрывания случайной музыки ! обязательно нужен полный путь !!
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
def numbers_key():
    if len(words) == 1:
        if len(kps) == 1:
            key_press(*kps)  # ! назначаем kps клавишу в скрипте например kps = 'right'  kps = 'down'
        elif len(kps) > 1:
            keyhot(*kps)
    elif len(words) > 1:
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
            print(f"\b{LCY} кнопка{WHI}({GRE}{words[0]}{WHI}) {YEL}+ {GRE}число {YEL}!={LRE}", end="")


print(Fore.RESET, end='')

vosk.SetLogLevel(-1)  # удаляем логи

speakrate_set = 4
current_voice = "Microsoft Pavel Mobile"

# Инициализация распознавателя с начальной моделью
current_model = Model(model1)
rec = KaldiRecognizer(current_model, 48000)

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


# Функция для смены модели
def change_model(new_model):
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


speak.Volume = 100  # громкость


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

#: состав словаря из названий ярлыков
file_list = os.listdir(path_to_shortcut)
lnk_files = [f for f in file_list if f.endswith(".lnk") or f.endswith(".url")]

labels = []  # словарь названий ярлыков
for lnk_file in lnk_files:
    full_path = os.path.join(path_to_shortcut, lnk_file)
    label = lnk_file[:-4]  # удаляем последние четыре символа
    labels.append(label)

# Находим окно с именем 'ассистент'
try:
    assistant = pyautogui.getWindowsWithTitle('ассистент')[0]
    assistant.moveTo(-8, 0)
    assistant.resizeTo(849, 327)
except Exception as e:
    assistant = pyautogui.getWindowsWithTitle('python.exe')[0]
    assistant.moveTo(-8, 0)
    assistant.resizeTo(849, 327)
    print(e, end="")
    for x in str(e):
        print(f"\b", end="")
    print(f"\r                                  --> ассистент.lnk\r", end="")

if __name__ == '__main__':
    translator = Translator()
    tts = pyttsx3.init()
    tts.runAndWait()
    loader_screen_rimtex()
    print(LGR + "\n ʕ/•ᴥ•ʔ/ Hi! " + SRA)
    while True:
        if rec.AcceptWaveform(stream.read(4000)):  # {   "text" : "слова" }
            try:
                prompt = rec.Result()[13:-2]
                words = prompt[1:-1].split()
                # конвертер команд старт

                #: Запись в курсор # запись голоса при включённом Caps Lock
                caps_lock_state_check = win32api.GetKeyState(0x14)
                num_lock_state_check = win32api.GetKeyState(0x90)
                if (caps_lock_state_check == 1 or caps_lock_state_check == -127) and \
                        (num_lock_state_check != 1 and num_lock_state_check != -127):
                    if prompt != '""':
                        print(LYE + " ≈ ", end="")
                        keyrus_write(prompt[1:-1])
                        prompt = '""'  # стираем фразы и слова чтобы не активировались команды
                        words = '""'
                        win32api.keybd_event(0x14, 0x45, 0x1, 0)  # выключение Caps Lock
                        win32api.keybd_event(0x14, 0x45, 0x3, 0)

                #: Запись в курсор с переводом # запись голоса при включённом Num Lock
                if (num_lock_state_check == 1 or num_lock_state_check == -127) and \
                        (caps_lock_state_check != 1 and caps_lock_state_check != -127):
                    if prompt != '""':
                        print(LGR + " ≈ ", end="")
                        wordstrans = str(prompt[1:-1])
                        trans = translator.translate(wordstrans, "english", "russian")
                        keytrans_write(f"{trans}")
                        prompt = '""'
                        words = '""'
                        win32api.keybd_event(0x90, 0x45, 0x1, 0)  # выключение Num Lock
                        win32api.keybd_event(0x90, 0x45, 0x3, 0)

                #: для команд
                elif prompt in ('"показать команды"', '"покажи команды"'):
                    print(f'\n{convert_paint()}')
                elif prompt in ('"команды русским"', '"команды перевод"', '"покажи русским"'):
                    print(f'\n{convert_trans()}')
                elif prompt in ('"покажи"', '"показать"'):
                    print(f'\n{convert_delete()}')

                #: смена модели распознавания
                elif len(words) == 2 and any(words in prompt[1:-1] for words in ('модель', 'model')):
                    try:
                        if any(words in prompt[1:-1] for words in ('один', 'лёгкая', 'one', 'russian')):
                            change_model(model1)
                        if any(words in prompt[1:-1] for words in ('два', 'тяжёлая', 'two', 'to')):
                            change_model(model2)
                            speak_pavel_tts("тяжёлая русская модель загружена!")
                        if any(words in prompt[1:-1] for words in ('три', 'free', 'three', 'light')):
                            change_model(model3)
                        if any(words in prompt[1:-1] for words in ('четыре', 'four', 'for', 'heavy')):
                            change_model(model4)
                            speak_irina_tts("тяжёлая английская модель загружена!")
                    except Exception as e:
                        change_model(model1)
                        print(LRE, e, LCY, f"\n 1 https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip"
                                           f"\n 2 https://alphacephei.com/vosk/models/vosk-model-ru-0.42.zip"
                                           f"\n 3 https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
                                           f"\n 4 https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip")

                #: для быстрого поиска
                elif len(words) > 0 and words[0] in ('поиск', 'команду', 'команда', 'погнали', 'поехали'):
                    if len(words) == 1:
                        keyhot('ctrl', 'f')
                    if len(words) > 1:  #: поиск из буфера
                        # os.startfile(f"{path_to_shortcut}питон")  # стартуем нужную прогу
                        keywrite = prompt[len(words[0]) + 2:-1]  # минус первое слово
                        print(f"{LGR}˃{LCY} п {LMA}? ", end='')
                        time.sleep(.1)
                        click_print()
                        keyhot('ctrl', 'f')
                        keyboard.write(f"{keywrite}")
                        key_press('enter')

                #: найти найди пуск окей-гугл
                elif 0 < len(words) <= 10 and words[0] in ('найти', 'найди', 'пуск', 'окей'):
                    if len(words) == 1 and words[0] in ('найти', 'найди'):
                        keyhot("ctrl", "f")
                    if len(words) == 1 and words[0] == 'пуск':
                        key_press("winleft")
                    if len(words) > 1 and words[0] == 'найти':
                        write_prompt = prompt[6:-1]  # убираем первое слово и кавычки из фразы
                        key_press("winleft")  # Открываем окно найти в пуске
                        time.sleep(0.2)  # Ждем, пока окно загрузится
                        keyboard.write(write_prompt)  # Вводим слова
                        time.sleep(0.2)  # Ждем на всякий случай
                        key_press("enter")  # Нажимаем Enter
                    if len(words) > 1 and words[0] == 'найди':  #: найти в пуске с переводом на английский
                        trans_prompt = prompt[6:-1]
                        try:
                            trans = translator.translate(trans_prompt, "english", "russian")
                            keyhot("winleft", "й")
                            time.sleep(0.2)
                            keyboard.write(f"{trans}")
                            print(f"{LYE} {trans}", end=' ')
                            time.sleep(0.2)
                            key_press("enter")
                        except Exception as e:
                            print(f" (!o_O): {LRE}! переводчик: ", e)

                    #: окей гугл
                    elif len(words) >= 2 and (words[0] == 'окей' and words[1] == 'гугл'):
                        if prompt == '"окей гугл"':
                            speak_tts("что вам найти?")
                            while True:
                                if rec.AcceptWaveform(stream.read(4000)):
                                    prompt = rec.Result()[14:-3]
                                    if prompt != '':
                                        try:
                                            webbrowser.open('https://www.google.com/search?q=' + prompt)
                                            print(f'\nhttps://www.google.com/search?q={quote(prompt)}')
                                            break
                                        except OSError:
                                            print(LCY + "г" + SRA, end='')
                                    else:
                                        break
                        elif prompt != '"окей гугл"':  #: окей гугл + слова
                            try:
                                webbrowser.open('https://www.google.com/search?q=' + prompt[11:-1])
                                print("\nhttps://www.google.com/search?q=" + quote(prompt[11:-1]))
                            except OSError:
                                print(LCY + "Г" + SRA, end='')

                #: режим паузы
                elif prompt in ('"пауза"', '"блокировка"', '"остановка"', '"режим паузы"'):
                    print(LCY + '\n ʕ℗•ᴥ•℗ʔ' + SRA, end='')
                    speak_tts("режим паузы включён!")
                    while True:
                        if rec.AcceptWaveform(stream.read(4000)):
                            prompt = rec.Result()[13:-2]
                            if prompt in ('"стенка"', '"стену"', '"строй"', '"стройка"', '"построй"', '"постройка"'):
                                loader.waal_generator()
                            elif prompt in ('"бред"', '"умом"'):
                                loader.smile_generator()
                                loader.letters_random()
                            elif prompt in ('"запуск"', '"запустить"', '"запусти"', '"стартуем"', '"обычный режим"'):
                                print(f'\n{LGR} \ʕ•ᴥ•ʔ/{SRA}')
                                speak_tts("запускаю обычный режим!")
                                break
                            elif len(words) == 1 and words[0] == 'громкость':
                                print(LCY + '♪' + SRA, end='')
                                key_press('volumemute')
                            elif prompt == '"тест"':
                                os.startfile(f"{path_to_shortcut}тест")
                            elif prompt in ('"пауза"', '"заблокировать"', '"остановка"', '"паузы"'):
                                speak_tts("я итак на паузе!")
                            elif prompt in ('"слушай"', '"слышь"', '"слышь ты"', '"слышишь"', '"слэш"'):
                                speak_tts("я на паузе если что!")
                            elif prompt in ('"ассистент"', '"перезапуск"', '"рестарт"'):
                                print(LRE + '\n ʕ/·ᴥ·ʔ/ Bye! ' + SRA)
                                os.startfile(f"\\{path_to_shortcut}ассистент")
                                exit()

                #: установка громкости системы
                elif any(words in prompt[1:-1] for words in
                         ('заткнись на хрен', 'не так громко', 'слишком громко', 'минус громкость')) \
                        or prompt[1:-1] in ('громко', 'громкость', 'мут'):
                    key_press('volumemute')
                elif len(words) == 2 and words[0] == 'громкость' and words[1] in words_num:
                    on_num = sum(words_num[word] for word in words[1:]) // 2
                    print(LCY + '♪', end='')
                    for i in range(50):  # ! костыль
                        pyautogui.press('volumedown')
                    for i in range(on_num):
                        pyautogui.press('volumeup')

                #: установка скорости озвучивания голоса
                elif len(words) >= 2 \
                        and re.match(r'(скорост\w?\b)|(озвуч\w{0,5}\b)|(голос\w{0,3}\b)', words[0]) \
                        and words[1] in words_num:
                    speak_num = words_num[words[1]]
                    speakrate_set = speak_num
                    print(YEL + f' {LRE}ϟ{LGR}☼{LYE}♪ ' + LGR, end='')
                    sk_show = '⁞'
                    for i in range(speak_num):
                        print(sk_show, sep='', end='', flush=True)
                        time.sleep(0.03)
                    print(LCY + f' {GRE}{speak_num}{LCY}', end='')
                    speak_tts(f'скорость озвучки {speak_num}')

                #: переключение голоса
                elif prompt == '"павел"':
                    switch_voice("Microsoft Pavel Mobile")  # Переключение на голос Павла
                    print(YEL + f' {LRE}ϟ{LGR}☼{LYE}Pavel ' + LGR, end='')
                    speak_pavel_tts("Microsoft Pavel Mobile")  # Озвучивание текста голосом Павла
                elif prompt == '"ирина"':
                    switch_voice("Microsoft Irina Desktop")  # Переключение на голос Ирины
                    print(YEL + f' {LRE}ϟ{LGR}☼{LYE}Irina ' + LGR, end='')
                    speak_irina_tts("Microsoft Irina Desktop")  # Озвучивание текста голосом Ирины

                #: нажатие клавиш + число для повторений
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
                #: клавиши стрелки + число для повторений
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
                #: комбинации клавиш + число для повторений
                elif 7 > len(words) > 0 and words[0] in ('уничтожь', 'уничтожить', 'уничтожать', 'уничтожает'):
                    kps = ['hift', 'delete']
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
                #: одноразовое нажатие
                elif 7 > len(words) > 0 and words[-1] in ('перевод', 'переведи', 'цифры', 'цифра', 'циферки'):
                    key_press('numlock')
                elif 7 > len(words) > 0 and words[-1] in ('голос', 'пиши', 'пишем', 'напиши', 'букве', 'буквы', 'капс'):
                    key_press('CapsLock')  # п1
                elif re.match(r'"(\w?копир\w{0,6}\b)"', prompt):
                    keyhot('ctrlleft', 'c')
                elif re.match(r'"(\w{0,2}хран\w{0,5}\b)"', prompt):
                    keyhot('ctrlleft', 's')
                elif re.match(r'"(буфер\w?\b)"|"(спис\w{0,2}\b)"', prompt):
                    keyhot('winleft', 'v')
                elif re.match(r'"(раскладк\w?\b)"|"(клавиатур\w{0,2}\b)"', prompt):
                    keyhot('win', 'space')

                #: работа с окнами
                elif 3 > len(words) > 0 and re.match(r'(окно)|(разв\w{0,6}\b)|(свер\w{0,4}\b)', words[0]):
                    if len(words) == 1:
                        if re.match(r'(разв\w{0,6}\b)', words[0]):
                            keyhot('winleft', 'Up')
                        if re.match(r'(свер\w{0,4}\b)', words[0]):
                            keyhot('winleft', 'Down')
                    if len(words) == 2 and words[0] == 'окно':
                        if 2 >= len(words) > 1 and re.match(r'^.{0,3}прав.{0,3}$', words[1]):
                            keyhot('winleft', 'Right')
                        if 2 >= len(words) > 1 and re.match(r'^.{0,3}лев.{0,3}$', words[1]):
                            keyhot('winleft', 'Left')
                        if 2 >= len(words) > 1 and re.match(r'^.{0,3}верх.{0,3}$', words[1]):
                            keyhot('winleft', 'Up')
                        if 2 >= len(words) > 1 and re.match(r'^.{0,3}низ.{0,3}$', words[1]):
                            keyhot('winleft', 'Down')
                elif len(words) == 1 and re.match(r'(закр\w{0,4}\b)', words[0]):
                    keyhot('altleft', 'F4')
                elif prompt in ('"окна"', '"окошки"', '"вин таб"', '"показать окна"', '"режим окон"'):
                    keyhot('winleft', 'tab')
                elif prompt in ('"свернуть все"', '"сверни все"', '"чисто"'):
                    keyhot('winleft', 'd')
                elif prompt in ('"свернуть лишнее"', '"свернуть лишнее"', '"лишнее"'):
                    keyhot('winleft', 'Home')
                elif prompt in ('"закрыть вкладку"', '"закрой вкладку"', '"минус вкладка"', '"крестик"'):
                    keyhot('ctrlleft', 'w')
                elif prompt in ('"обновить"', '"обнови"', '"об нова"', '"эф пять"'):
                    key_press("f5")

                #: закрывание всех окон
                elif prompt in ('"убей всех"', '"растрелли"', '"расстрел"', '"застрели"', '"расстрел окон"'
                                , '"расстреле"', '"расстрелять"'):
                    print(f"""{LRE} ({LGR}√{LRE}¬_¬)ԅ⌐╦╦═─‒=═≡Ξ{SRA}""", end='')
                    assistant.minimize()
                    assistant.restore()
                    os.startfile(f"{path_to_shortcut}ассистент")
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
                    keyboard.write(datetime.now().strftime("%H,%M,%S")[0:5])  # убрал секунды

                #: зачитка из буфера
                elif prompt in ('"зачитай"', '"прочитай"', '"прочти"', '"прочитать"', '"говори"', '"скажи"'):
                    print(f"{LBL}♪", end='')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    speak = win32com.client.Dispatch("SAPI.SpVoice")
                    speak_pavel_tts(text)
                #: зачитка из буфера другим голосом
                elif prompt in ('"озвучь"', '"озвучивает"', '"озвучивать"'):
                    print(f"{LGR}♫", end='')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    speak = win32com.client.Dispatch("SAPI.SpVoice")
                    speak_irina_tts(text)

                #: захват видео MSI Afterburner
                elif prompt in ('"захват видео"', '"захвати видео"'):
                    os.startfile(f"{path_to_shortcut}захват видео")  # ярлык MSI Afterburner
                elif prompt in ('"запись видео"', '"запиши видео"'):
                    speak_tts(prompt)
                    os.startfile(f"{path_to_shortcut}видео")  # ярлык папки
                    time.sleep(1)
                    keyboard.press('ctrl')
                    keyboard.press_and_release('-')
                    keyboard.release('ctrl')
                elif prompt in ('"конец видео"', '"видео стоп"', '"стоп видео"', '"стоп захват"', '"захват стоп"'):
                    keyboard.press('ctrl')
                    keyboard.press_and_release('-')
                    keyboard.release('ctrl')
                    time.sleep(1)
                    os.startfile(f"{path_to_shortcut}видео")
                    time.sleep(1)
                    speak_tts(prompt)

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
                    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)

                #: перезагрузка ассистента
                elif len(words) > 0 and words[-1] in ('тихо', 'старт'):
                    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
                    os.startfile(f"{path_to_shortcut}ассистент")
                    exit()
                elif prompt in ('"ассистент"', '"рестарт"', '"перезагрузка"', '"перезагрузить"', '"перезапуск"'):
                    assistant.moveRel(0, 20)
                    print(LRE, end="")
                    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
                    os.startfile(f"{path_to_shortcut}ассистент")
                    for i in range(15):
                        printt('\n')
                    printt(' ʕ/·ᴥ·ʔ/')
                    loader.download_bye()
                    time.sleep(2)
                    exit()

                #: озвучка проблем
                elif prompt in ('"проблемы"', '"что за проблема"', '"в чем проблема"', '"проблема"',
                                '"да блядь че за хуйня"', '"почему не работает"'):
                    speak_tts("1 ! русская раскладка! "
                              "2 ! запятые! "
                              "3 ! переводчик не работает с впн"
                              "3.1 библиотеки не устанавливаются с впн"
                              "4 ! иногда ассистент морозица. возможно помогает tts"
                              "5 ! кавычки!"
                              "6 ! при старте на русской раскладке некоторые команды могут не работать"
                              )

                #: идеи
                elif len(words) == 2 and words[1] in ('идеи', 'идея', 'идею', 'идейку', 'идей'):
                    if words[0] in ('озвучь', 'зачитай', 'прочти', 'озвучить'):  #: озвучка идей
                        file = open(ideas, "r", encoding='utf-8')
                        contents = file.read()
                        speak_tts(contents)
                    elif words[0] in ('какие', 'покажи', 'где', 'показывай'):  #: отображение идей
                        file = open(ideas, "r", encoding='utf-8')
                        contents = file.read()
                        print(contents)
                    elif words[0] in ('записать', 'запиши', 'запись', 'записывай'):  #: записать идею
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

                #: работа с требованиями requirements.txt
                elif len(words) == 2 and re.match(r'(требован\w{0,2}\b)', words[1]):  #: требования
                    if re.match(r'(установ\w{0,5}\b)', words[0]):  # + установить
                        os.startfile(f"{path_to_shortcut}консоль")
                        time.sleep(1)
                        keyboard.write(f"pip install -r {requirements_path}")
                        key_press("enter")
                    if re.match(r'(\w{0,2}брос\w?\b)|(выки\w{0,5}\b)|(помойк\w?\b)', words[0]):  # + удалить
                        os.startfile(f"{path_to_shortcut}консоль")
                        time.sleep(1)
                        keyboard.write(f"pip uninstall -r {requirements_path}")
                        key_press("enter")
                        speak_tts("если хочешь удалить всё! закрой меня! и зажми энтер в консоли!")
                    if re.match(r'(обнов\w{0,5}\b)', words[0]):  # + обновить
                        os.startfile(f"{path_to_shortcut}консоль")
                        time.sleep(1)
                        keyboard.write(f"pip install --upgrade -r {requirements_path}")
                        key_press("enter")

                #: работа с модулями из буфера
                elif len(words) == 2 and re.match(r'(библиотек[ау]?.?)|(модул[ьи]?.?)|(пип.?)', words[1]):
                    if re.match(r'(установ\w{0,5}\b)', words[0]):
                        os.startfile(f"{path_to_shortcut}консоль")
                        time.sleep(1)
                        keyboard.write("pip install ")
                        keyhot('ctrl', 'v')
                        key_press("enter")
                    if re.match(r'(\w{0,2}брос\w?\b)|(выки\w{0,5}\b)|(помойк\w?\b)', words[0]):
                        os.startfile(f"{path_to_shortcut}консоль")
                        time.sleep(1)
                        keyboard.write("pip uninstall ")
                        keyhot('ctrl', 'v')
                        key_press("enter")
                        time.sleep(2)
                        key_press("enter")
                    if re.match(r'(обнов\w{0,5}\b)', words[0]):
                        os.startfile(f"{path_to_shortcut}консоль")
                        time.sleep(1)
                        keyboard.write(f"pip install --upgrade ")
                        keyhot('ctrl', 'v')
                        key_press("enter")

                #: ♪ реакции на слова или фразы
                elif prompt == '"я робот"':
                    print(random.choice(colors) + "[-_-]", end='')
                    speak_irina_tts(vocabulary.random_response_robot())
                elif prompt == '"не дано"':
                    print(random.choice(colors) + "♪{•ᴥ•}♫", end='')
                    speak_irina_tts(vocabulary.random_response_nedano())
                elif prompt in ('"слушай"', '"слышь"', '"слышишь"', '"слэш"', '"слышь ты"'):
                    loader.smile_gen_erator()
                    speak_tts(vocabulary.random_response())
                    click_print_cor(677, 1345)  # координаты кнопки ответа https://chat.openai.com/
                elif any(word in prompt[1:-1] for word in ('блядь', 'нихуя', 'бля', 'ахуеть', 'бляха', 'ебать')):
                    loader.smile_generator()
                    speak_tts(vocabulary.sp_rec_reaction_Fuck())
                elif any(word in prompt[1:-1] for word in ('сука', 'сучара', 'охуел', 'нахуй', 'тварь')):
                    speak_tts("давай без агрессии")
                elif any(word in prompt[1:-1] for word in ('агрессии', 'агрессия', 'ладно')):
                    print(random.choice(colors) + f"{LRE}♥ {GRE}cԅ(‾ε‾ԅ)", end='')
                elif len(words) > 0 and words[-1] in ('согласен', 'согласись'):  # для последнего слова
                    loader.smile_gen_erator()
                    # speak_tts("конечно. ты прав!")  # диктует вам мудрость
                    speakrate_set = 1
                    time.sleep(2.5)
                    speak_tts(vocabulary.random_response_aphorism())  # диктует модели мудрость
                    time.sleep(2.5)
                    speak_tts("запрос?")  # говорит триггер для старта запроса модели
                elif len(words) == 1 and words[0] == "ублюдок":
                    print(random.choice(colors) + "┌п┐(._.)┌∩┐", end='')
                    speak_tts(vocabulary.sp_rec_reaction_bastard())
                elif len(words) == 1 and (words[0] == "цитаты" or words[0] == "мемы"):
                    print(random.choice(colors) + "(ʘ͜͡)", end='')
                    speak_tts(vocabulary.sp_rec_reaction_memequotes())
                elif len(words) == 1 and (words[0] == "внатуре" or words[0] == "чётко"):
                    print(random.choice(colors) + "(⌐▪˽▪)", end='')
                    speak_tts(vocabulary.sp_rec_reaction_auf())
                elif len(words) == 1 and (words[0] == 'обама' or words[0] == 'барак'):
                    print(random.choice(colors) + "(•`_´•)", end='')
                    speak_tts(vocabulary.random_response_obeme())
                elif prompt in ('"шаурма"', '"если хочешь кушать"', '"приходи в мой шаурма"'):
                    print(random.choice(colors) + "(°□°)", end='')
                    speak_tts(vocabulary.sp_rec_reaction_shawarma())
                elif prompt in ('"ёбаная шиза"', '"шизо ебаная"', '"шиза ебаная"', '"шиза ебаное"'):
                    print(random.choice(colors) + "(→ᴥ←)", end='')
                    speak_tts(vocabulary.random_response_upyachka())
                elif prompt in ('"идущий к реке"', '"идущие к реке"'):
                    print(random.choice(colors) + "(→_→)", end='')
                    speak_tts(vocabulary.random_response_Goingtotheriver())
                elif prompt in ('"печенье лом"', '"а найди ка нам бригаду"'):
                    print(random.choice(colors) + "└(`▪´)┐", end='')
                    speak.rate = 0
                    speak_tts(vocabulary.sp_rec_reaction_pechenielom())
                elif prompt == '"история про говно"':
                    print(random.choice(colors) + "(○´ ― `)", end='')
                    speak_tts(vocabulary.random_response_shit())
                elif prompt == '"бурлеск"':
                    print(random.choice(colors) + "(’̀₀’̀Q )", end='')
                    speak_tts(vocabulary.random_response_Burlestat())
                elif prompt == '"месть"':
                    print(random.choice(colors) + "(¬_¬`)", end='')
                    random.choice(random_voice)(vocabulary.random_response_revenge())
                elif prompt in ('"расскажи историю"', '"историю расскажи"'):
                    print(random.choice(colors) + "(~‾▾‾)~ ╓───╖ ┌┤", end='')
                    speak_tts(vocabulary.random_response_stories())
                elif prompt in ('"матрица история"', '"история матрица"'):
                    print(random.choice(colors) + "(⌐■˽■)⌐ ╓───╖ ┌┤", end='')
                    speak_tts(vocabulary.response_matrix())
                elif prompt in ('"история про бога"', '"про бога история"'):
                    print(random.choice(colors) + "ʅ(ο_ο)ʃ", end='')
                    speak_tts(vocabulary.reaction_godofchrist())
                elif prompt in ('"афоризм"', '"афоризмы"', '"совет"', '"советы"', '"дай совет"', '"и афоризм"'):
                    print(random.choice(colors) + '( •_•)>⌐', end='')
                    speak_tts(vocabulary.random_response_aphorism())
                elif prompt in ('"стишки"', '"стихи"', '"стих"', '"стишок"'):
                    print(random.choice(colors) + '(ˇò_ó)', end='')
                    speak_tts(vocabulary.random_rhymes())
                elif prompt in ('"анекдот"', '"анекдоты"'):
                    print(random.choice(colors) + '( •̪O )', end='')
                    speak_tts(vocabulary.random_anecdote())

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

                #: ♫ включение отдельных треков
                elif prompt in ('"единый идол"', '"единой идол"', '"идол"'):
                    os.startfile(f"{dir_path}\\United Idol - Hai Phút Hơn.mp3")
                    print(random.choice(colors) + "┌(◄_►)┐", end='')
                elif prompt in ('"я синица я аллигатор"', '"синица я аллигатор"', '"синица аллигатор"'):
                    os.startfile(f"{dir_path}\\Ня - Аригато.mp3")
                    print(random.choice(colors) + "(♥ᴗ♥)", end='')
                elif prompt in ('"тут туру"', '"тот туру"', '"тот торо"', '"тот уро"', '"тот туру', '"тот тро"'):
                    os.startfile(f"{dir_path}\\Mayuri-Tuturu (mp3cut.ru).mp3")
                    print(random.choice(colors) + "(*ˊᵕˋ)~ * .·:*¨₊˚Lᵒᵛᵉᵧₒᵤ♥", end='')
                elif prompt in ('"армянин"', '"арман эн"'):
                    os.startfile(f"{dir_path}\\isyan-tetick-patlamaya-devam.mp3")
                    print(random.choice(colors) + "ʕ‾•ᴥ•‾ʔ•ᴥ•‾ʔ", end='')

                #: работа с мышкой
                elif prompt == '"координаты"':
                    x, y = pyautogui.position()
                    print(f"\nclick_print_cor{LYE}({x}, {y})", end='')  # - координаты курсора
                elif prompt in ('"тэк"', '"клик"', '"кликни"', '"кликай"', '"кликнуть"'):
                    click_print()
                #: зажать - отпустить
                elif len(words) == 1 and words[0] in ('зажми', 'зажать', 'зажал', 'зажимать', 'схвати', 'схватить'):
                    pyautogui.mouseDown()
                elif len(words) == 1 and words[0] in ('отпусти', 'отпускай', 'отпустить', 'пусти', 'отпускай', 'отжал'):
                    pyautogui.mouseUp()
                #: клик # + число
                elif 7 > len(words) > 1 and re.match(r'(клик\w{0,4}\b)', words[0]):
                    try:
                        num = sum(words_num[word] for word in words[1:])
                        for i in range(num):  # - количество нажатий курсора
                            click_print()
                    except KeyError:
                        print(f"{LGR}{words[0]} {YEL}+ {LCY}число {YEL}!={LRE}", end="")
                #: курсор в центр экрана
                elif prompt in ('"центр"', '"в центр"', '"на центр"'):
                    screen_width, screen_height = pyautogui.size()  # - Получение размеров экрана
                    pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=0.25)  # - курсор в центр экрана

                #: промотка колеса # + число
                elif 5 > len(words) > 0 and words[0] in ('промотай', 'мотай'):  # ↓
                    if len(words) == 1:
                        print(f"{YEL}↓{LCY}∆ ", end="")
                        pyautogui.scroll(-1500)
                    elif len(words) > 1 and words[1] in words_num:
                        num = sum(words_num[word] for word in words[1:])
                        for i in range(num):
                            pyautogui.scroll(-1500)
                        print(f"{YEL}↓{GRE}{num}{LCY}∆ ", end="")
                elif 5 > len(words) > 0 and re.match(r'колес\w{0,3}\b', words[0]):  # ↑
                    if len(words) == 1:
                        print(f"{YEL}↑{LCY}∆ ", end="")
                        pyautogui.scroll(1500)
                    elif len(words) > 1 and words[1] in words_num:
                        num = sum(words_num[word] for word in words[1:])
                        for i in range(num):
                            pyautogui.scroll(1500)
                        print(f"{YEL}↑{GRE}{num}{LCY}∆ ", end="")

                #: ctrl плюс промотка колеса # + число
                elif 5 > len(words) > 0 and words[0] in ('дальше', 'подальше'):
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
                elif 5 > len(words) > 0 and words[0] in ('ближе', 'поближе'):
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
                                nums = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(nums, 0)
                                cursor_direction()
                        if re.match(r'^.{0,3}низ.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:] * 10)
                                pyautogui.moveRel(0, nums)
                            if words[2] not in words_num:
                                nums = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(0, nums)
                                cursor_direction()
                        if re.match(r'^.{0,3}лев.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:] * 10)
                                pyautogui.moveRel(-nums, 0)
                            if words[2] not in words_num:
                                nums = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(-nums, 0)
                                cursor_direction()
                        if re.match(r'^.{0,3}верх.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:] * 10)
                                pyautogui.moveRel(0, -nums)
                            if words[2] not in words_num:
                                nums = sum(words_num[word] for word in words[3:] * 10)
                                pyautogui.moveRel(0, -nums)
                                cursor_direction()
                    except Exception as e:
                        print(f"{LGR} {words[0]} + направление(я) + {LCY}числа {YEL}!= {LRE}", e, end='')

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
                    keyhot('winleft', 'tab')
                    time.sleep(.5)
                    keyhot('winleft', 'tab')
                elif len(words) == 1 and words[0] == 'бабах':  # альт таб х2 - вин таб х2
                    print(LRE + "↔2↕2 ", end='')
                    keyhot('alt', 'tab')
                    time.sleep(.5)
                    keyhot('alt', 'tab')
                    time.sleep(.5)
                    keyhot('winleft', 'tab')
                    time.sleep(.5)
                    keyhot('winleft', 'tab')
                elif len(words) > 1 and words[0] == 'раз':  # альт таб равен количеству слов после 'раз'
                    print(LRE + "↔+w▸ ", end='')
                    puk_length = len(words)
                    key_down('alt')
                    for i in range(puk_length):
                        time.sleep(.1)
                        key_press('tab')
                    key_up('alt')
                elif prompt in ('"эй"', '"ты где"', '"ты тут"', '"себя"', '"в себя"', '"покажись"', '"панель"'):
                    assistant.minimize()  # сворачивание
                    assistant.restore()  # раздупляем восстанавливанием
                    print(LGR + "ø", end="")
                elif prompt in ('"уйди"', '"свали"', '"угол"', '"место"', '"места"', '"наказан"'):
                    print(LGR + "╔", end="")
                    assistant.minimize()
                    assistant.restore()
                    assistant.moveTo(-8, 0)  # двигаем ассистента в угол
                    assistant.resizeTo(849, 327)  # настраиваем размер окна
                    assistant.activate()
                    try:
                        DeepL = pyautogui.getWindowsWithTitle('DeepL')[0]
                        DeepL.minimize()
                        DeepL.restore()
                        DeepL.moveTo(2048, 0)
                        DeepL.resizeTo(2568, 1408)
                        Pysharm = pyautogui.getWindowsWithTitle('Voice_Commands.py')[0]
                        Pysharm.minimize()
                        Pysharm.restore()
                        Pysharm.moveTo(826, 0)
                        Pysharm.resizeTo(1450, 1408)
                        Edge = pyautogui.getWindowsWithTitle('Microsoft​ Edge')[0]
                        Edge.minimize()
                        Edge.restore()
                        Edge.moveTo(-8, 319)
                        Edge.resizeTo(849, 1089)
                        print("═", end="")
                    except IndexError:
                        print("ø", end="")

                #: встроенные утилиты
                elif prompt == '"поговорим"':
                    os.startfile(f"Voice_neuro_responder.py")  #
                    loader.download_generator()
                elif prompt == '"модель"':
                    os.startfile(f"Tester_models.py")  #
                    loader.download_generator()

                elif prompt != '""':
                    if caps_lock_state_check != 1 and caps_lock_state_check != -127:  # - проверка на запись
                        script_writing_function(prompt, words)  # -  для печати в keyboard_scripts.py

                # -: открываем все своё с ярлыков
                if prompt != '""' and len(words) == 1 and words[0] in labels:
                    try:
                        os.startfile(f"{path_to_shortcut}{prompt[1:-1]}")
                        print(LCY + "√", end='')
                    except FileNotFoundError:
                        try:
                            os.startfile(f"{path_to_shortcut}{prompt[1:-1]}.url")
                            print(LCY + "e√", end='')
                        except FileNotFoundError:
                            print(Fore.WHITE + "_", end="")  # - индикатор попытки открытия файла

                if prompt != '""':  # - пишем свои голос
                    print(f' {prompt[1:-1]}{SRA}', sep='', end=' ')

            # конвертер команд конец
            except Exception as e:
                print(traceback.format_exc())
                print(f"{LRE} ʕ•ᴥ•ʔʃ Ошибка :{SRA}", e)
