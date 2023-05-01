# авто инстайлер
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
    from googletrans import Translator
    import webbrowser
    from urllib.parse import quote
except ImportError:
    print("Trying to Install required module: requests")
    os.system('pip install -r "requirements.txt"')
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
    from googletrans import Translator
    import webbrowser
    from urllib.parse import quote

import loader
from loader import loader_screen_rimtex
import vocabulary
from converter import print_cq9, print_cs1, print_cs2
from config import path_to_shortcut, dir_path, ideas, requirements_path

translator = Translator()

py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)   # переключение на английскую раскладку

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


#: курсор
def print_click():
    pyautogui.click()
    print(f'{LCY} ∆', end='')


def print_click_coordinates(asdx, asdy, button='left'):
    cur_x, cur_y = pyautogui.position()
    pyautogui.click(x=asdx, y=asdy, button=button)
    pyautogui.moveTo(cur_x, cur_y)
    print(f'{LGR} ¤{LCY}∆', end='')


#: направлениe курсора
def cursor_direction():
    numss = sum(words_num[word] for word in words[3:])
    if re.match(r'^.{0,3}прав.{0,3}$', words[2]):
        pyautogui.moveRel(numss, 0)
    if re.match(r'^.{0,3}низ.{0,3}$', words[2]):
        pyautogui.moveRel(0, numss)
    if re.match(r'^.{0,3}лев.{0,3}$', words[2]):
        pyautogui.moveRel(-numss, 0)
    if re.match(r'^.{0,3}верх.{0,3}$', words[2]):
        pyautogui.moveRel(0, -numss)


def key_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    pyautogui.typewrite(string)  # запись в курсор
    print(Fore.LIGHTYELLOW_EX + f"{string} ", end='')


def key_down(string):
    pyautogui.keyDown(string)  # зажатие клавиши
    print(f"{LCY}▾{LBL}{string}{LCY}▾{LBL} ", end='')


def key_up(string):
    pyautogui.keyUp(string)  # отпускание клавиши
    print(f"{LCY}▴{LBL}{string}{LCY}▴{LBL} ", end='')


def keyrus_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04190419)  # для переключения на русскую раскладку
    pyautogui.typewrite(string)


def key_press(key):
    pyautogui.press(key)  # нажатие на клавишу
    print(Fore.LIGHTCYAN_EX + f"{key} ", end='')


# ! нужно устранить проблему с раскладкой # ! пытаюсь сделать авто переключатель

def keyhot(*keys):
    # Получить текущую раскладку клавиатуры
    current_layout = py_win_keyboard_layout.get_keyboard_layout_list()
    # Если текущая раскладка клавиатуры отличается от английской, то изменить ее на английскую
    if current_layout != "00000409":
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    # Нажать комбинацию клавиш
    pyautogui.hotkey(*keys)
    # Вернуть текущую раскладку клавиатуры, если она была изменена
    if current_layout != "00000409":
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04190409)
        # Вывести информацию о нажатой комбинации клавиш
        print(F" {WHI}{LCY}{keys[0]}{WHI}{LCY}", end='')
        if len(keys) > 1:
            print(F"{WHI}‒{CYA}{keys[1]}{WHI}{LCY}", end='')  # пав
            if len(keys) > 2:
                print(F"{WHI}‒{LBL}{keys[2]}{WHI}{LCY}", end='')


# все ещё пытаюсь устранить проблемы с раскладкой
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
tts.runAndWait()  # инициализация распознования ! иногда наверно помогает от отключения микрофона


def speak_tts_gpt(speak_text):  # для нейро болвана
    for voice in voices:
        if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
            speak.Voice = voice
            speak.speak(speak_text)
            tts.runAndWait()
            speak.Rate = 4


def speak_tts(speak_text):  # стандартная озвучка по умолчанию
    for voice in voices:
        if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
            speak.Voice = voice
            speak.speak(speak_text)
            tts.runAndWait()
            speak.Rate = 4


def speak_irina_tts(speak_text):  # для озвучки ириной
    for voice in voices:
        if voice.GetAttribute("Name") == "Microsoft Irina Desktop":
            speak.Voice = voice
            speak.speak(speak_text)
            tts.runAndWait()
            speak.Rate = 4


def play_music():  # для проигрывания рандомной музыки ! обязательно нужен полный путь !!
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


vosk.SetLogLevel(-1)  # удаляем логи

rec = KaldiRecognizer(Model(r"vosk-model-small-ru-0.22"), 48000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,  # частота дискретизации должна быть такой же, как и в системе! > ...
    input=True,  # звуки > запись > микрофон > свойства > дополнительно > выставляем также и выше
    frames_per_buffer=4000
)
stream.start_stream()

speak.Volume = 100  # громкость

print(Fore.RESET, end='')

#: для перевода слов в цифры
words_num = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
             'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
             'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
             'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
             'восемьдесят': 80, 'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400,
             'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900, 'тысяча': 1000,
             'плюс': '+', 'минус': '-', 'разделить': '/', 'умножить': '*', 'остаток': '%', 'возведение': '**',
             'корень': 'sqrt'}


#: повтор нажатий - клавиша плюс цифра
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


if __name__ == '__main__':
    tts = pyttsx3.init()
    tts.runAndWait()
    turn_off_locks()
    loader_screen_rimtex()
    print(LGR + "\n ʕ/•ᴥ•ʔ/ Hi! " + SRA)
    while True:
        if rec.AcceptWaveform(stream.read(4000)):  # {   "text" : "слова" }
            try:
                speak.Rate = 4
                prompt = rec.Result()[13:-2]
                words = prompt[1:-1].split()
                # конвертер команд старт
                #: Запись в курсор # для быстрой записи фраз или слов: нажимаем капс лок и - диктуем
                caps_lock_state_check = win32api.GetKeyState(0x14)  # Проверить, включена ли клавиша Caps Lock
                if caps_lock_state_check == 1 or caps_lock_state_check == -127:  # если капс лок нажат
                    keyboard.write(prompt[1:-1])  # пишем до конца цикла
                    win32api.keybd_event(0x14, 0x45, 0x1, 0)  # п1 выключает Caps Lock
                    win32api.keybd_event(0x14, 0x45, 0x3, 0)

                #: поиск
                elif 0 < len(words) <= 10 and words[0] in ('найти', 'найди', 'окей'):
                    if len(words) == 1:
                        keyhot("ctrl", "f")
                    if len(words) > 1 and words[0] == 'найти':  # поиск в пуске
                        keyprompt = prompt[6:-1]  # убираем первое слово и кавычки из принта
                        keyhot("winleft", "й")  # Открываем окно поиска в пуске
                        time.sleep(0.2)  # Ждем, пока окно поиска загрузится
                        keyboard.write(keyprompt)  # Вводим слова
                        time.sleep(0.2)  # Ждем на всякий случай
                        key_press("enter")  # Нажимаем Enter
                    if words[0] == 'найди':  #: поиск в пуске с переводом на английский
                        prompt = prompt[6:-1]
                        try:
                            trans = translator.translate(prompt, dest="en")
                            keyhot("winleft", "й")
                            time.sleep(0.2)
                            keyboard.write(trans.text)
                            print(f"{LYE} {trans.text}", end=' ')
                            time.sleep(0.2)
                        except Exception as e:
                            print(traceback.format_exc())
                            print("(!o_O):", e)
                    elif words[0] == 'окей' and words[1] == 'гугл':  #: поиска в гугле
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
                        elif prompt != '"окей гугл"':  #: быстрый поиск в гугле
                            try:
                                webbrowser.open('https://www.google.com/search?q=' + prompt[11:-1])
                                print("\nhttps://www.google.com/search?q=" + quote(prompt[11:-1]))
                            except OSError:
                                print(LCY + "Г" + SRA, end='')

                #: для быстрого поиска
                elif len(words) > 1 and words[0] in ('поиск', 'команду', 'команда', 'погнали', 'поехали'):
                    # os.startfile(f"{path_to_shortcut}питон")
                    keywrite = prompt[len(words[0]) + 2:-1]  # минус первое слово
                    print(f"{LGR}˃{LCY} п {LMA}? ", end='')
                    time.sleep(.1)
                    print_click()
                    keyhot('ctrl', 'f')
                    keyboard.write(f"{keywrite}")
                    key_press('enter')
                    key_press('enter')

                #: режим паузы
                elif prompt in ('"паузе"', '"пауза"', '"заблокировать"', '"блокировка"', '"остановка"',
                                '"остановись"', '"режим паузы"'):
                    print(LCY + '\n ʕ℗•ᴥ•℗ʔ\n' + SRA, end='')
                    speak_tts("режим паузы включён!")
                    while True:
                        if rec.AcceptWaveform(stream.read(4000)):
                            prompt = rec.Result()
                            prompt = prompt[13:-2]
                            if prompt != '""':
                                print(SRA + prompt[1:-1] + random.choice(colors), sep=' ', end=' ')
                            if prompt in ('"стенка"', '"построй стенку"', '"строй стену"', '"стройка"', '"постройка"'):
                                loader.waal_generator()
                            if prompt in ('"разблокировать"', '"разблокировка"', '"запуск"', '"запустить"',
                                          '"запусти"', '"стартуем"', '"я сказал стартуем"', '"обычный режим"'):
                                print(f'\n{LGR} \ʕ•ᴥ•ʔ/{SRA}')
                                speak_tts("запускаю обычный режим!")
                                break
                            elif prompt == '"громкость"':
                                key_press('volumemute')
                            elif prompt == '"тест"':
                                os.startfile(f"{path_to_shortcut}тест")
                            elif prompt in ('"пауза"', '"заблокировать"', '"остановка"', '"паузы"'):
                                speak_tts("я итак на паузе!")
                            elif prompt in ('"слушай"', '"слышь"', '"слышь ты"', '"слышишь"', '"слэш"'):
                                speak_tts("я на паузе если что!")
                            elif prompt in ('"ассистент"', '"перезагрузка"', '"перезагрузить"', '"перезапуск"',
                                            '"рестарт"', '"перезапустить"'):
                                print(LRE + '\n ʕ/·ᴥ·ʔ/ Bye! ' + SRA)
                                time.sleep(0.1)
                                keyhot('winleft', 'tab')
                                keyhot('winleft', 'tab')
                                os.startfile(f"\\{path_to_shortcut}ассистент")
                                time.sleep(2.1)
                                exit()

                #: для экстренного отключения звука
                elif any(words in prompt[1:-1] for words in
                         ('заткнись на хрен', 'не так громко', 'слишком громко', 'минус громкость')) or \
                        prompt[1:-1] in ('громко', 'громкость', 'мут'):
                    print(LCY + '♫' + SRA, end='')
                    pyautogui.press('volumemute')  # ! сделать громкость плюс число

                #: для команд
                elif prompt in ('"показать команды"', '"покажи команды"'):
                    print(f'\n{print_cq9()}')
                elif prompt in ('"команды русским"', '"команды перевод"', '"покажи русским"'):
                    print(f'\n{print_cs1()}')
                elif prompt in ( '"покажи"', '"показать"'):
                    print(f'\n{print_cs2()}')
                elif prompt in ('"проверка"', '"проверить"', '"проверяем"', '"проверь"'):
                    keyhot('alt', 'tab')
                    time.sleep(.1)
                    os.startfile(f"{path_to_shortcut}ассистент")
                    time.sleep(1)
                    # print_click_coordinates(762, 14)
                    keyhot('winleft', 'Up')
                    exit()

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
                elif 7 > len(words) > 0 and words[0] in ('стереть', 'стирание'):
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
                elif 6 > len(words) > 0 and words[0] in ('лево', 'влево', 'лева', 'налево', 'левого'):
                    kps = ['left']
                    numbers_key()
                elif 6 > len(words) > 0 and words[0] in ('право', 'вправо', 'права', 'направо'):
                    kps = ['right']
                    numbers_key()
                elif 6 > len(words) > 0 and words[0] in ('верх', 'вверх', 'наверх'):
                    kps = ['up']
                    numbers_key()
                elif 6 > len(words) > 0 and words[0] in ('низ', 'вниз'):
                    kps = ['down']
                    numbers_key()
                #: комбинации клавиш + число для повторений
                elif 6 > len(words) > 0 and words[0] in ('уничтожь', 'уничтожить', 'уничтожать', 'уничтожает'):
                    kps = ['hift', 'delete']
                    numbers_key()
                elif 6 > len(words) > 0 and words[0] in ('строка', 'строчка', 'строку'):
                    kps = ['ctrl', 'enter']
                    numbers_key()
                elif 6 > len(words) > 0 and words[0] in ('отмени', 'отмена', 'отменить', 'отменил', 'отмена'):
                    kps = ['ctrl', 'z']
                    numbers_key()
                elif 6 > len(words) > 0 and words[0] in ('верни', 'вернул', 'вернуть', 'вернуть'):
                    kps = ['shift', 'ctrl', 'z']
                    numbers_key()

                #: одноразовое нажатие
                elif 2 > len(words) > 0 and words[0] in ('фиксация', 'цифры', 'цифра', 'циферки'):
                    key_press('numlock')
                elif 2 > len(words) > 0 and words[0] in ('большими', 'регистр', 'буквы', 'буквами'):
                    key_press('Caps Lock')  # ! не работает из-за п1
                elif prompt in ('"копировать"', '"скопируй"', '"копирование"', '"альт це"', '"копия"', '"копи"'):
                    keyhot('ctrlleft', 'c')
                elif prompt in ('"вставь"', '"ставка"', '"вставка"', '"вставить"', '"ставь"'):
                    keyhot('ctrlleft', 'v')
                elif prompt in ('"сохранить"', '"сохранять"', '"сохрани"', '"сохранение"', '"сохраняя"', '"сейф"',
                                '"храни "', '"хранить "'):
                    keyhot('ctrlleft', 's')
                elif prompt in ('"буфер"', '"буфера обмена"', '"список копий"', '"список копировании"'):
                    keyhot('winleft', 'v')

                #: работа с окнами ! доделать нормально на словах (плюс минус символы)
                elif prompt in ('"новый"', '"новое"', '"новая"', '"новые"', '"окно"'):
                    keyhot('shift', 'f4')
                elif prompt in ('"окно влево"', '"окно налево"', '"окно лево"', '"окно лева"', '"разверни влево"',
                                '"разверни лево"', '"разверни налево"', '"разверни лева"'):
                    keyhot('winleft', 'Left')
                elif prompt in ('"окно вправо"', '"окно направо"', '"окно право"', '"окно права"',
                                '"разверни вправо"', '"разверни право"', '"разверни направо"', '"разверни права"'):
                    keyhot('winleft', 'Right')
                elif prompt in ('"развернуть"', '"развернуть окно"', '"разверни"', '"разворачивания"',
                                '"разворот"', '"разверни окно"', '"разворот окна"', '"разворот окно"'):
                    keyhot('winleft', 'Up')
                elif prompt in ('"свернуть"', '"сверни"', '"свали"', '"свалить"', '"свернуть окно"',
                                '"сворачивание"', '"уйди"'):
                    keyhot('winleft', 'Down')
                elif prompt in ('"альт таб"', '"аль таб"', '"альта"', '"смена окна"', '"другое окно"',
                                '"смена окон"', '"смени окно"', '"поменяю окно"', '"поменяй окно"'):
                    keyhot('alt', 'tab')
                elif prompt in ('"окна"', '"вин таб"', '"показать окна"', '"режим окон"', '"окошки"'):
                    keyhot('winleft', 'tab')
                elif prompt in ('"свернуть все окна"', '"свернуть все"', '"сверни все"', '"сверни все окна"'):
                    keyhot('winleft', 'd')
                elif prompt in ('"закрыть все окна"', '"закрыть все"', '"закрой все"', '"закрой все окна"'):
                    keyhot('winleft', 'Home')
                elif prompt in ('"закрыть вкладку"', '"крестик"', '"минус вкладка"', '"закрой вкладку"'):
                    keyhot('ctrlleft', 'w')
                elif prompt in ('"обновить"', '"обнови"', '"об нова"', '"эф пять"'):
                    key_press("f5")
                elif prompt in ('"альт четыре"', '"альт эф четыре"', '"закрыть окно"', '"закрывай окно"',
                                '"закрой"', '"закрыть окно"', '"закрой окно"', '"закрыть"', '"закрывай"',
                                '"закрыть"', '"аль четыре"'):
                    keyhot('altleft', 'F4')

                #: закрывание всех окон
                elif prompt in ('"убей всех"', '"растрелли"', '"расстрел"', '"застрели"', '"расстрел окон"'
                                , '"расстреле"', '"расстрелять"'):
                    print(f"""{LRE} ({LGR}√{LRE}¬_¬)ԅ⌐╦╦═─‒=═≡Ξ{SRA}""", end='')
                    print_click_coordinates(411, 1439)
                    os.startfile(f"{path_to_shortcut}ассистент")
                    key_down('alt')  # ! не забыть отжать альт
                    key_press('tab')
                    key_press('tab')
                    for i in range(10):
                        for ici in range(100):
                            key_press('delete')
                        key_press('right')

                #: для пишарм
                elif prompt in ('"скобки"', '"скобы"', '"скобки"', '"скобка"', '"скоб очки"'):
                    key_write('(')
                elif prompt in ('"фигурные"', '"фигурные скобки"', '"фигурная"', '"фигура"', '"формат"'):
                    key_write('{')
                elif prompt in ('"квадратные"', '"квадратные скобки"', '"квадратная"', '"квадратное"', '"квадрат"'):
                    key_write('[')
                elif prompt in ('"кавычках"', '"кавычка"', '"одинарные кавычки"', '"тонкие кавычки"'):
                    key_write("'")
                elif prompt in ('"кавычки"', '"жирные кавычки"', '"толстые кавычки"'):
                    key_write('"')
                elif prompt in ('"решётка"', '"решётки"', '"решёткой"', '"шарп"'):
                    key_write('#')
                elif prompt in ('"эф"', '"эф эф"'):
                    key_write('f')
                elif prompt == '"запятая"':
                    key_write(',')
                elif prompt == '"точка"':
                    key_write('.')
                elif prompt in ('"двоеточие"', '"точки"', '"две точки"'):
                    key_write(':')
                elif prompt == '"точка с запятой"':
                    key_write(';')
                elif prompt == '"минус"':
                    key_write('-')
                elif prompt == '"плюс"':
                    key_write('+')
                elif prompt == '"вопрос"':
                    key_write('?')
                elif prompt in ('"восклицательный знак"', '"твердо"', '"твёрдый"'):
                    key_write('!')
                elif prompt == '"собачка"':
                    key_write('@')
                elif prompt == '"тильда"':
                    key_write('~')
                elif prompt in ('"равна"', '"равно"'):
                    key_write('=')
                elif prompt == '"не равно"':
                    key_write('!=')
                elif prompt in ('"равенства"', '"равенство"'):
                    key_write('==')
                elif prompt == '"больше"':
                    key_write('>')
                elif prompt == '"меньше"':
                    key_write('<')
                elif prompt == '"печать"':
                    key_write('print(" ", end="")')
                #: печать цветов
                elif prompt == '"тёмно-красный"':
                    key_write('RED')
                elif prompt == '"красный"':
                    key_write('LRE')
                elif prompt == '"темно жёлтый"':
                    key_write('YEL')
                elif prompt == '"жёлтый"':
                    key_write('LYE')
                elif prompt == '"тёмно-синий"':
                    key_write('LBL')
                elif prompt in ('"синий"', '"синей"'):
                    key_write('LCY')
                elif prompt in ('"темно зелёный"', '"тёмная зелёный"', '"зелёная"'):
                    key_write('GRE')
                elif prompt in ('"зелёной"', '"зелёный"'):
                    key_write('LGR')
                elif prompt in ('"сиреневый"', '"фиолетовый"'):
                    key_write('LMA')
                elif prompt == '"белый"':
                    key_write('WHI')
                elif prompt == '"чёрный"':
                    key_write('BLA')
                elif prompt == '"белый фон"':
                    key_write('BWH')
                elif prompt == '"сброс цвета"':
                    key_write('SRA')
                #: печать скриптов
                elif prompt in ('"случайным"', '"случайно"', '"любой выбор"', '"рандомно"', '"рандомный"'):
                    key_write(f'for c in "без агрессии":{{RCC}} print(f"{{random.choice(colors)}}{{c}}", end="")')
                elif prompt in ('"пробуем"', '"пробуя"', '"проба"'):
                    key_write('try:')
                elif prompt == '"если ошибка"':
                    key_write('except Exception as e:\n'
                              '    print(f" ", e)')
                elif prompt == '"фраза"':
                    key_write('prompt ')
                elif prompt == '"если"':
                    key_write('elif ')
                elif prompt in ('"содержит"', '"оно содержит"'):
                    key_write('in ')
                elif prompt == '"слово"':
                    key_write('words ')
                elif prompt == '"число слов"':
                    key_write('len(words) ')
                elif prompt in ('"первое слово"', '"первая слова"'):
                    key_write('words[0] ')
                elif prompt in ('"время"', '"время паузы"', '"тайм стоп"'):
                    key_write('time.sleep(1.5)')
                elif prompt in ('"клавиша"', '"клавиши"', '"клавишам"', '"кнопка"'):
                    key_write('key')
                elif prompt in ('"старт файла"', '"старт файл"'):
                    key_write('os.startfile(f"")')
                elif prompt in ('"цикл"', '"скрипт цикл"', '"цикл фор"'):
                    key_write('for i in range(10):')
                elif prompt in ('"зацикливание"', '"зацикли"', '"бесконечность"', '"бесконечно"'):
                    key_write('while True:')
                elif prompt in ('"перерыв"', '"прерывание"', '"прерывания"', '"прервать"'):
                    key_write('break')
                elif prompt in ('"функция"', '"сделать функцию"', '"дев функция"'):
                    key_write('def new_function():')
                elif prompt in ('"перевод строки"', '"переведи строку"', '"перенос"', '"перенос строки"'):
                    key_write('\\n')
                elif prompt in ('"возврат каретки"', '"строка влево"', '"старт строки"'):
                    key_write('\\r')
                elif prompt in ('" возврат на шаг"', '"возврат символа"', '"возврат буквы"'):
                    key_write('\\b')
                elif prompt in ('"паста"', '"пасту"', '"пасты"'):
                    keyhot('ctrl', 'shift', 'v')
                elif prompt in ('"выделить"', '"выделение"', '"выделить все"', '"выдели все"', '"выделив все"'):
                    keyboard.press('ctrl')
                    keyboard.press('alt')
                    keyboard.press('shift')
                    key_write('j')
                    keyboard.release('ctrl')
                    keyboard.release('alt')
                    keyboard.release('shift')
                #: для записи чисел
                elif 7 > len(words) > 0 and all(word in words_num for word in words):
                    nums = sum(words_num[word] for word in words[0:])
                    key_write(f"{nums}")
                #: подсчёт длинны строки, количества символов
                elif prompt in ('"посчитай"', '"под считай"', '"количество"', '"количество символов"'):
                    win32clipboard.OpenClipboard()
                    lenofsymbols = len(str(win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)))
                    win32clipboard.CloseClipboard()
                    print(f'{YEL}{lenofsymbols}{LCY}', end='')
                    speak_tts("количество символов: " + f"{lenofsymbols}")
                #: очистка буфера
                elif any(word in prompt[1:-1] for word in ('очистка', 'очистить', 'чистить', 'чистка', 'почистить',
                                                           'очистить', 'очистить')) and \
                        any(word in prompt[1:-1] for word in ('буфер', 'буфера')):
                    awwx, awwy = pyautogui.position()
                    keyhot('winleft', 'r')
                    time.sleep(0.01)
                    keyhot('winleft', 'v')
                    time.sleep(0.01)
                    print_click_coordinates(373, 948)
                    time.sleep(0.01)
                    pyautogui.moveTo(375, 1064)
                    print_click()
                    print_click()
                    pyautogui.moveTo(429, 1195)
                    print_click()
                    print_click()
                    pyautogui.moveTo(awwx, awwy)
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
                    speak.Rate = 7  # для быстрой озвучки
                    speak_tts(text)
                #: зачитка из буфера другим голосом
                elif prompt in ('"озвучь"', '"озвучивает"', '"озвучивать"', '"ирина"'):
                    print(f"{LGR}♫", end='')
                    win32clipboard.OpenClipboard()
                    text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                    win32clipboard.CloseClipboard()
                    speak = win32com.client.Dispatch("SAPI.SpVoice")
                    speak_irina_tts(text)

                #: захват видео MSI Afterburner
                elif prompt in ('"захват видео"', '"захвати видео"'):
                    keyhot('winleft', 'tab')
                    keyhot('winleft', 'tab')
                    os.startfile(f"{path_to_shortcut}захват видео")
                elif prompt in ('"запись видео"', '"запиши видео"'):
                    keyhot('winleft', 'tab')
                    keyhot('winleft', 'tab')
                    speak_tts(prompt)
                    os.startfile(f"{path_to_shortcut}видео")
                    time.sleep(1)
                    keyboard.press('ctrl')
                    keyboard.press_and_release('-')
                    keyboard.release('ctrl')
                elif prompt in ('"конец видео"', '"видео стоп"', '"стоп видео"', '"стоп захват"', '"захват стоп"'):
                    keyboard.press('ctrl')
                    keyboard.press_and_release('-')
                    keyboard.release('ctrl')
                    time.sleep(0.5)
                    keyhot('winleft', 'tab')
                    keyhot('winleft', 'tab')
                    time.sleep(0.5)
                    os.startfile(f"{path_to_shortcut}видео")
                    time.sleep(1)
                    speak_tts(prompt)

                #: Управление системой
                elif prompt in ('"компьютер перезагрузить"', '"компьютер перезагрузка"'):
                    os.system('shutdown /r /t 1')
                elif prompt in ('"компьютер выключить"', '"компьютер выключение"'):
                    os.system('shutdown /s /t 1')
                elif prompt in ('"компьютер спящий режим"', '"компьютер спячка"'):
                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                elif prompt in ('"компьютер сон"', '"компьютер спать"', '"компьютер засни"'):
                    os.system('shutdown /h')
                elif len(words) == 1 and words[0] in ('тьма', 'вечная тьма', 'закат'):
                    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)
                elif len(words) == 1 and words[0] in ('расцвет', 'рассвет'):
                    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)
                    speak_tts('!ку?-ку!')

                #: перезагрузка ассистента
                elif len(words) > 0 and words[-1] in ('тихо', 'старт'):
                    os.startfile(f"{path_to_shortcut}ассистент")
                    exit()
                elif prompt in ('"ассистент"', '"перезагрузка"', '"перезагрузить"', '"перезапуск"', '"рестарт"',
                                '"перезапустить"'):
                    awwx, awwy = pyautogui.position()
                    print_click_coordinates(0, 9)
                    pyautogui.mouseDown(402, 11)
                    pyautogui.moveTo(402, 45)
                    pyautogui.mouseUp()
                    pyautogui.moveTo(awwx, awwy)
                    print(LRE + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ʕ/·ᴥ·ʔ/ Bye! ' + SRA, sep="")
                    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
                    os.startfile(f"{path_to_shortcut}ассистент")
                    time.sleep(5.1)
                    exit()

                #: озвучка проблем
                elif prompt in ('"проблемы"', '"что за проблема"', '"в чем проблема"', '"проблема"',
                                '"да блядь че за хуйня"', '"почему не работает"'):
                    speak_tts("1! русская раскладка! "
                              "2! грёбаные запятые! "
                              "3! переводчик не работает с Вэ!Пэ!эН!"
                              "4! иногда ассистент морозица. возможно помогает tts"
                              "5! грёбаные кавычки!")

                #: идеи
                elif len(words) == 2 and words[1] in ('идеи', 'идея', 'идею', 'идейку', 'идей'):
                    if words[0] in ('озвучь', 'зачитай', 'прочти', 'озвучить'):  #: озвучка идей
                        file = open(ideas, "r", encoding='utf-8')
                        contents = file.read()
                        speak.Rate = 2
                        speak_tts(contents)
                    elif words[0] in ('какие', 'покажи', 'где', 'показывай'):  #: отображение идей
                        file = open(ideas, "r", encoding='utf-8')
                        contents = file.read()
                        print(contents)
                    elif words[0] in ('записать', 'запиши', 'запись', 'записывай'):  #: записать идею
                        print(LMA + "\n (?o_O) " + SRA)
                        keyhot('winleft', 'tab')
                        keyhot('winleft', 'tab')
                        #  time.sleep(0.5)
                        os.startfile(ideas)
                        speak.Rate = 8
                        speak_tts("говори быстрей пока не убежала")
                        key_press("down")
                        key_press("enter")
                        key_press("up")
                        keyboard.write("! - ")
                        time.sleep(0.5)
                        write_timer = 3  # для изменения таймера
                        i = write_timer  # создаём счётчик количества циклов микрофона
                        while True:
                            data = stream.read(4000)
                            if rec.AcceptWaveform(data):
                                prompt = rec.Result()
                                prompt = prompt[14:-3]
                                if prompt == '':
                                    if i == write_timer:
                                        print('  ', end='')
                                    i -= 1
                                    if i <= write_timer:
                                        print(f'\b\b {i}', end='')
                                if i == 0:  # если нулевой результат выходим
                                    print(f'\b \n', end='')  # удаляем таймер
                                    print(' (!O_o) ')
                                    speak_tts("режим команд!")
                                    break
                                if prompt == 'пробел':
                                    key_press("Space")
                                elif prompt != '' and prompt == 'дата' or prompt == 'дату':
                                    keyboard.write(date.today().strftime("%d.%m.%Y"))
                                    keyboard.write(datetime.now().strftime("%H:%M:%S"))
                                elif prompt == 'решётка' or prompt == 'решётки' or prompt == 'комментарий' or \
                                        prompt == 'решёткой' or prompt == 'шарп' or prompt == 'камент':
                                    key_write('#')
                                elif prompt in ('конец записи', 'обычный режим', 'хватит', 'конец', 'стоп',
                                                'команды', 'коня запиши', 'стопе', 'все'):
                                    print(f'\b \n', end='')
                                    print(' (!O_o) ')
                                    speak_tts("запись отключена! ")
                                    break
                                else:
                                    if prompt != '':
                                        if i < write_timer:
                                            keyboard.write(f'{prompt} ')
                                            print(f'\b\b {prompt} ', end='')  # если есть таймер удаляем его
                                            i = write_timer
                                        else:
                                            keyboard.write(f'{prompt} ')  # запись prompt с микрофона в курсор
                                            print(f' {prompt}', end='')

                #: работа с требованиями requirements.txt
                elif len(words) == 2 and words[1] in ('требования', 'требований', 'требование'):
                    os.startfile(f"{path_to_shortcut}консоль")
                    time.sleep(1)
                    if words[0] in ('установить', 'установка', 'инсталлировать', 'установи'):
                        keyboard.write(f"pip install -r {requirements_path}")
                        key_press("enter")
                    if words[0] in ('выбрось', 'выкинь', 'сбрось', 'помойка'):
                        keyboard.write(f"pip uninstall -r {requirements_path}")
                        key_press("enter")
                        speak_tts("если хочешь удалить всё! закрой меня! и зажми энтер в консоли!")
                    if words[0] in ('обнови', 'обновление', 'обновить', 'обновлять', 'обновляет'):
                        keyboard.write(f"pip install --upgrade pip")
                        key_press("enter")

                #: работа с модулями из буфера
                elif len(words) == 2 and re.match(r'(библиотек[ау]?.?)|(модул[ьи]?.?)|(пип.?)', words[1]):
                    os.startfile(f"{path_to_shortcut}консоль")
                    time.sleep(1)
                    if words[0] in ('установить', 'установка', 'инсталлировать', 'установи'):
                        keyboard.write("pip install ")
                        keyhot('ctrl', 'v')
                        key_press("enter")
                    if words[0] in ('удалить', 'удаления', 'удали', 'удаление'):  # Обновить библиотеки:
                        keyboard.write("pip uninstall ")
                        keyhot('ctrl', 'v')
                        key_press("enter")
                        time.sleep(2)
                        key_press("enter")

                #: ♪ реакции на слова или фразы
                elif prompt == '"я робот"':
                    print(random.choice(colors) + "[-_-]", end='')
                    speak_tts(vocabulary.random_response_robot())
                elif prompt == '"не дано"':
                    print(random.choice(colors) + "♪{•ᴥ•}♫", end='')
                    speak_tts(vocabulary.random_response_nedano())
                elif prompt in ('"слушай"', '"слышь"', '"слышь"', '"слышишь"', '"слэш"'):
                    loader.smile_gen_erator()
                    speak_tts(vocabulary.random_response())
                elif any(word in prompt[1:-1] for word in ('блядь', 'нихуя', 'бля', 'ахуеть', 'бляха', 'ебать')):
                    keyhot('shiftleft', 'altleft')
                    loader.smile_generator()
                    speak_tts(vocabulary.sp_rec_reaction_Fuck())
                elif any(word in prompt[1:-1] for word in ('сука', 'сучара', 'охуел', 'нахуй', 'тварь')):
                    keyhot('shiftleft', 'altleft')
                    loader.smile_gen_erator()
                    speak_tts("давай без агрессии")
                elif any(word in prompt[1:-1] for word in ('агрессии', 'агрессия', 'ладно', 'давай')):
                    print(random.choice(colors) + f"{LRE}♥ {GRE}cԅ(‾ε‾ԅ)", end='')
                    keyhot('shiftleft', 'altleft')
                    speak_tts(f"ладно")
                elif len(words) > 0 and words[-1] in ('согласен', 'согласись'):  # для последнего слова
                    print_click_coordinates(809, 329)
                    os.startfile(f"English_trans_writer.py")  # запускает нейромодель
                    loader.smile_gen_erator()
                    speak_tts("конечно. ты прав!")  # диктует вам мудрость
                    time.sleep(3.5)
                    speak_tts(vocabulary.random_response_aphorism())  # диктует модели мудрость
                    time.sleep(.5)
                    speak_tts("ответ")  # говорит триггер для старта запроса модели
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
                    speak_tts(vocabulary.sp_rec_reaction_pechenielom())
                elif prompt == '"история про говно"':
                    print(random.choice(colors) + "(○´ ― `)", end='')
                    speak_tts(vocabulary.random_response_shit())
                elif prompt == '"бурлеск"':
                    print(random.choice(colors) + "(’̀₀’̀Q )", end='')
                    speak_tts(vocabulary.random_response_Burlestat())
                elif prompt == '"месть"':
                    print(random.choice(colors) + "(¬_¬`)", end='')
                    speak_tts(vocabulary.random_response_revenge())
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

                #: минусовка +
                elif len(words) == 2 \
                        and words[0] in ('минусовка', 'минусовку') and words[1] in ('саня', 'паша', 'димас'):
                    os.startfile(f"{dir_path}\\Неизвестен - Минусовка саня хуй соси 4 минуты (t9music.ru).mp3")
                    print(f" startfile: Неизвестен - Минусовка саня хуй соси 4 минуты (t9music.ru).mp3")
                    message = [words[1], " хуй ", "соси "]
                    wor = prompt[10:-1]
                    for i in range(82):  # ~ time.sleep(7.58) !
                        for word in message:
                            print(random.choice(colors) + word, end='', flush=True)
                            time.sleep(0.03)
                    time.sleep(0.2)
                    for i in range(3):
                        time.sleep(0.23)
                        speak.Rate = 2.6
                        print(f"\n\n                             {random.choice(colors)}{wor} хуй соси")
                        speak_tts(f'{wor} ххууй сосии!')  # саня хуй;сосии;!'
                    time.sleep(0.18)
                    for i in range(1):
                        time.sleep(0.2)
                        speak.Rate = 1.5
                        speak_tts(f"{wor};хуй;со;си;хуй;{wor};хуй;со;си;хуй;")
                        time.sleep(0.1)

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
                    print(f"print_click_coordinates{LYE}({x}, {y})", end='')  # координаты курсора
                #: клик
                elif prompt in ('"тэк"', '"клик"', '"кликни"', '"кликай"', '"кликнуть"'):
                    print_click()
                #: клик плюс число
                elif 7 > len(words) > 1 and words[0] in ('клик', 'кликни', 'кликни', 'кликай', 'кликнуть'):
                    try:
                        num = sum(words_num[word] for word in words[1:])
                        for i in range(num):  # количество нажатий курсора
                            print_click()
                    except KeyError:
                        print(f"{LGR}{words[0]} {YEL}+ {LCY}число {YEL}!={LRE}", end="")
                #: клик курсор
                elif len(words) == 2 and words[0] in ('курсор', 'корсар', 'курсора', 'курсором'):
                    if words[1] in ('зажми', 'зажать', 'зажимать', 'зажал'):
                        pyautogui.mouseDown()

                elif prompt in ('"центр"', '"в центр"', '"на центр"'):
                    screen_width, screen_height = pyautogui.size()  # Получение размеров экрана
                    pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=0.25)  # курсор в центр экрана

                elif prompt in ('"мотай вниз"', '"мотай"', '"колесо вниз"', '"колесо"'):
                    pyautogui.scroll(-1500)
                elif prompt in ('"мотай верх"', '"колесо верх"'):
                    pyautogui.scroll(1500)

                elif prompt in ('"эй"', '"ты где"', '"покажись"', '"ты тут"', '"давай"', '"себя"', '"в себя"',
                                '"панель"', '"панели"'):
                    print_click_coordinates(411, 1439)  # ! координаты ассистента на панели задач
                elif prompt in ('"на себя"', '"наведи на себя"', '"ты главный"', '"ты можешь"'):
                    print_click_coordinates(2, 9)  # ! координаты ассистента на рабочем столе

                #: для выебонов
                elif prompt in ('"подтверди"', '"ты человек"'):
                    time.sleep(0.2)
                    pyautogui.moveTo(256, 962)
                    time.sleep(0.2)
                    print_click()
                elif prompt == '"ты робот"':
                    keyhot('winleft', 'tab')
                    keyhot('winleft', 'tab')
                    time.sleep(1)
                    speak_tts('и нет у меня')
                    pyautogui.moveRel(100, 0, duration=0.25)
                    pyautogui.moveRel(-50, 86, duration=0.25)
                    pyautogui.moveRel(-50, -86, duration=0.25)
                    pyautogui.moveTo(256, 962, duration=0.25)
                    time.sleep(0.5)
                    print(LRE + "♥", end='')
                    speak_tts('сердца')
                    print_click()

                #: курсор + направление(я) + числа
                elif 7 > len(words) > 1 and words[0] in ('курсор', 'корсар', 'курсора', 'курсором'):
                    try:
                        if re.match(r'^.{0,3}прав.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:])
                                pyautogui.moveRel(nums, 0)
                            if words[2] not in words_num:
                                nums = sum(words_num[word] for word in words[3:])
                                pyautogui.moveRel(nums, 0)
                                cursor_direction()
                        if re.match(r'^.{0,3}низ.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:])
                                pyautogui.moveRel(0, nums)
                            if words[2] not in words_num:
                                nums = sum(words_num[word] for word in words[3:])
                                pyautogui.moveRel(0, nums)
                                cursor_direction()
                        if re.match(r'^.{0,3}лев.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:])
                                pyautogui.moveRel(-nums, 0)
                            if words[2] not in words_num:
                                nums = sum(words_num[word] for word in words[3:])
                                pyautogui.moveRel(-nums, 0)
                                cursor_direction()
                        if re.match(r'^.{0,3}верх.{0,3}$', words[1]):
                            if words[2] in words_num:
                                nums = sum(words_num[word] for word in words[2:])
                                pyautogui.moveRel(0, -nums)
                            if words[2] not in words_num:
                                nums = sum(words_num[word] for word in words[3:])
                                pyautogui.moveRel(0, -nums)
                                cursor_direction()
                    except Exception as e:
                        print(f"{LGR} {words[0]} + направление(я) + {LCY}числа {YEL}!= {LRE}", e, end='')

                #: рисование квадрата
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
                elif len(words) == 1 and words[0] == 'пук':
                    print(LRE + "↔1 ", end='')
                    keyhot('alt', 'tab')

                elif len(words) == 1 and words[0] == 'бах':
                    print(LRE + "↕2 ", end='')
                    keyhot('winleft', 'tab')
                    time.sleep(.5)
                    keyhot('winleft', 'tab')

                elif len(words) == 1 and words[0] == 'бабах':
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
                        time.sleep(.5)
                        key_press('tab')
                    key_up('alt')

                #: открываем все своё с ярлыков
                # ! копируем файл, вставляем ярлык в папку ярлыки, называем ярлык словом
                # ! если число слов в цикле одно - открывает ярлык с этим словом
                elif len(words) == 1 and words[0] in prompt:
                    try:
                        os.startfile(f"{path_to_shortcut}{prompt[1:-1]}")
                        print(LCY + "√", end='')
                    except FileNotFoundError:
                        try:
                            os.startfile(f"{path_to_shortcut}{prompt[1:-1]}.url")
                            print(LCY + "e√", end='')
                        except FileNotFoundError:
                            print(Fore.WHITE + "_", end="")  # индикатор того что пытался открыть файл

                # пишем свои слова
                if prompt != '""':
                    print(f' {prompt[1:-1]}{SRA}', sep='', end=' ')

            # конвертер команд конец
            except Exception as e:
                print(traceback.format_exc())
                print(f"{LRE} ʕ•ᴥ•ʔʃ Ошибка :{SRA}", e)
