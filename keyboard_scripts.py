import os
import random
import time
import re
import keyboard
import pyautogui
import py_win_keyboard_layout
from colorama import init, Fore, Style
from pyttsx3 import speak

import loader
import vocabulary

from address_config import path_to_shortcut, requirements_path

colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX,
          Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]
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
SRA = Style.RESET_ALL
init(convert=True)

#: для перевода слов в цифры
words_num = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
             'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
             'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
             'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
             'восемьдесят': 80, 'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400,
             'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900,
             'тысяча': 1000
             }
"""
         'плюс': '+', 'минус': '-', 'разделить': '/', 'умножить': '*', 'остаток': '%', 'возведение': '**',
         'корень': 'sqrt'}
"""


#: курсор клик
def click_print():
    pyautogui.click()
    print(f'{LCY}∆', end='')


#: курсор клик в координаты и назад
def click_print_cor(asdx, asdy, button='left'):
    cor_x, cor_y = pyautogui.position()
    pyautogui.click(x=asdx, y=asdy, button=button)
    pyautogui.moveTo(cor_x, cor_y)
    print(f'{LGR} ¤{LCY}∆', end='')


def keyrus_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04190419)  # для переключения на русскую раскладку
    print(LYE + f"{string} " + SRA, end='')
    keyboard.write(string)


def key_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    print(YEL + f"{string} ", end='')
    keyboard.write(string)  # запись в курсор


def keytrans_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    print(GRE + f"{string} " + SRA, end='')
    keyboard.write(string)  # запись в курсор


def key_down(string):
    pyautogui.keyDown(string)  # зажатие клавиши
    print(f"{LGR}▾{LBL}{string}{LGR}▾{LCY} ", end='')


def key_up(string):
    pyautogui.keyUp(string)  # отпускание клавиши
    print(f"{LGR}▴{LBL}{string}{LGR}▴{LCY} ", end='')


def key_press(key):
    pyautogui.press(key)  # нажатие на клавишу
    print(Fore.LIGHTCYAN_EX + f"{key} ", end='')

    """
      # Получить текущую раскладку клавиатуры
      current_layout = py_win_keyboard_layout.get_keyboard_layout_list()
      # Если текущая раскладка клавиатуры отличается от английской, то изменить ее на английскую
      if current_layout != "00000409":
          py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)    
      # Вернуть текущую раскладку клавиатуры, если она была изменена
      if current_layout != "00000409":
          py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04190409)    
    """


#: клавиши с принтом
def keyhot(*keys):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    # Нажать комбинацию клавиш
    pyautogui.hotkey(*keys)
    # Вывести информацию о нажатой комбинации клавиш
    print(F" {WHI}{LCY}{keys[0]}{WHI}{LCY}", end='')
    if len(keys) > 1:
        print(F"{WHI}‒{CYA}{keys[1]}{WHI}{LCY}", end='')
        if len(keys) > 2:
            print(F"{WHI}‒{LBL}{keys[2]}{WHI}{LCY}", end='')


# для проигрывания случайной музыки
def play_music():
    from address_config import dir_path
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


# конвертер команд старт

def key_symbols(prompt):
    if prompt in ('"скоба"', '"скобка"', '"скоб бачка"'):
        key_write('(')
    elif prompt in ('"скобы"', '"скобки"', '"скоб очки"'):
        key_write('()')
    elif prompt in ('"фигурная"', '"фигура"', '"формат"'):
        key_write('{')
    elif prompt in ('"фигурные"', '"фигуры"', '"фигурные скобки"'):
        key_write('{}')
    elif prompt in ('"квадратная"', '"квадратное"', '"квадрат"'):
        key_write('[')
    elif prompt in ('"квадратные"', '"квадратной"', '"квадраты"'):
        key_write('[]')
    elif prompt in ('"кавычках"', '"кавычка"', '"одинарные кавычки"', '"тонкие кавычки"'):
        key_write("'")
    elif prompt in ('"кавычки"', '"жирные кавычки"', '"толстые кавычки"'):
        key_write('"')
    elif prompt in ('"решётка"', '"решётки"', '"решёткой"', '"шарп"'):
        key_write('#')
    elif prompt == '"слэш"':
        key_write('\\')
    elif prompt == '"пайп"':
        key_write('|')
    elif prompt == '"обратный слэш"':
        key_write('/')
    elif prompt == '"запятая"':
        key_write(',')
    elif prompt == '"точка"':
        key_write('.')
    elif prompt in ('"двоеточие"', '"точки"', '"две точки"'):
        key_write(':')
    elif prompt == '"точка с запятой"':
        key_write(';')
    elif prompt == '"апостроф"':
        key_write('`')
    elif prompt == '"минус"':
        key_write('-')
    elif prompt == '"плюс"':
        key_write('+')
    elif prompt in ('"подчёркивание"', '"почерк"'):
        key_write('_')
    elif prompt in ('"цирком флекс"', '"флекс"', '"крышечка"'):
        key_write('^')
    elif prompt in ('"проценты"', '"процентов"', '"процент"'):
        key_write('%')
    elif prompt == '"доллар"':
        key_write('$')
    elif prompt == '"вопрос"':
        key_write('?')
    elif prompt == '"номер"':
        key_write('№')
    elif prompt in ('"звёздочка"', '"умножить"', '"умножь"'):
        key_write('*')
    elif prompt in ('"восклицательный знак"', '"твердо"', '"твёрдый"'):
        key_write('!')
    elif prompt in ('"собачка"', '"собака"', '"собакой"'):
        key_write('@')
    elif prompt == '"тильда"':
        key_write('~')
    elif prompt in ('"равна"', '"равно"'):
        key_write('=')
    elif prompt == '"не равно"':
        key_write('!=')
    elif prompt in ('"равенства"', '"равенство"'):
        key_write('==')
    elif prompt == '"знак больше"':
        key_write('>')
    elif prompt == '"знак меньше"':
        key_write('<')


def open_music(prompt):
    from address_config import dir_path
    #: ♫ включение случайной музыки
    if prompt in ('"радио"', '"включи радио"'):
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


def scripts_others(words):
    #: очистка буфера
    if 3 > len(words) > 0 and (re.match(r'\w{0,2}чист\w{0,3}\b', words[0])) \
            and (re.match(r'буфер\w?\b', words[1])):
        awwx, awwy = pyautogui.position()
        keyhot('winleft', 'r')
        time.sleep(0.01)
        keyhot('winleft', 'v')
        time.sleep(.5)
        click_print_cor(373, 948)
        pyautogui.moveTo(375, 1064)
        click_print()
        click_print()
        pyautogui.moveTo(429, 1195)
        click_print()
        click_print()
        pyautogui.moveTo(awwx, awwy)

    #: работа с требованиями requirements.txt
    elif len(words) == 2 and re.match(r'(требован\w{0,2}\b)', words[1]):
        if re.match(r'установ\w{0,5}\b', words[0]):  # + установить
            os.startfile(f"{path_to_shortcut}консоль")
            time.sleep(1)
            keyboard.write(f"pip install -r {requirements_path}")
            key_press("enter")
        if re.match(r'\w{0,2}брос\w?\b|выки\w{0,5}\b|помойк\w?\b', words[0]):  # + удалить
            os.startfile(f"{path_to_shortcut}консоль")
            time.sleep(1)
            keyboard.write(f"pip uninstall -r {requirements_path}")
            key_press("enter")
        if re.match(r'обнов\w{0,5}\b', words[0]):  # + обновить
            os.startfile(f"{path_to_shortcut}консоль")
            time.sleep(1)
            keyboard.write(f"pip install --upgrade -r {requirements_path}")
            key_press("enter")

    #: работа с модулями из буфера
    elif len(words) == 2 and re.match(r'библиотек[ау]?.?|модул[ьи]?.?|пип.?', words[1]):
        if re.match(r'установ\w{0,5}\b', words[0]):
            os.startfile(f"{path_to_shortcut}консоль")
            time.sleep(1)
            keyboard.write("pip install ")
            time.sleep(1)
            keyhot('ctrl', 'v')
            key_press("enter")
        if re.match(r'\w{0,2}брос\w?\b|выки\w{0,5}\b|помойк\w?\b', words[0]):
            os.startfile(f"{path_to_shortcut}консоль")
            time.sleep(1)
            keyboard.write("pip uninstall ")
            time.sleep(1)
            keyhot('ctrl', 'v')
            key_press("enter")
            time.sleep(2)
            key_press("enter")
        if re.match(r'обнов\w{0,5}\b', words[0]):
            os.startfile(f"{path_to_shortcut}консоль")
            time.sleep(1)
            keyboard.write(f"pip install --upgrade ")
            time.sleep(1)
            keyhot('ctrl', 'v')
            key_press("enter")


def rimtex_colors(prompt):
    #: печать цветов
    if prompt == '"тёмно-красный"':
        key_write('RED')
    elif prompt == '"красный"':
        key_write('LRE')
    elif prompt == '"оранжевый"':
        key_write('YEL')
    elif prompt == '"жёлтый"':
        key_write('LYE')
    elif prompt == '"тёмно-синий"':
        key_write('LBL')
    elif prompt in ('"синий"', '"синей"', '"голубой"'):
        key_write('LCY')
    elif prompt in ('"темно зелёный"', '"тёмная зелёный"'):
        key_write('GRE')
    elif prompt in ('"зелёный"', '"зелёной"', '"зелёная"'):
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


def rimtex_pycharm(prompt):
    #: печать функций и скриптов
    if prompt in ('"эф"', '"эф эф"'):
        key_write('f')
    elif prompt in ('"комментарий"', '"комментарии"'):
        key_write('"""')
    elif prompt == '"печать"':
        key_write('print(" ", end="")')
    elif prompt in ('"печатать"', '"напечатать"'):
        key_write('print("" " """)')
    elif prompt in ('"случайно"', '"случайный"', '"рандомно"', '"рандомный"'):
        key_write(f'random.choice()')
    elif prompt in ('"проверка"', '"проверить"', '"проверим"', '"проба"', '"пробовать"', '"пробуем"', '"попробуем"'):
        key_write('try:\n')
        key_write('except Exception as e: print(e, f"")')
    elif prompt == '"если"':
        key_write('elif ')
    elif prompt in ('"число"', '"в число"', '"числа"'):
        key_write('int("")')
    elif prompt in ('"длина"', '"длину"', '"длина объекта"', '"длину объекта"'):
        key_write('len("")')
    elif prompt in ('"строку"', '"в строку"', '"строка"', '"строчка"'):
        key_write('str("")')
    elif prompt in ('"вход"', '"вести"', '"ввести"', '"водить"', '"вводить"'):
        key_write('input("")')
    elif prompt in ('"время"', '"время паузы"', '"тайм стоп"'):
        key_write('time.sleep(1.5)')
    elif prompt in ('"старт файла"', '"старт файл"'):
        key_write('os.startfile(f"")')
    elif prompt in ('"цикл"', '"скрипт цикл"', '"цикл фор"'):
        key_write('for i in range(10):')
    elif prompt in ('"зацикли"', '"зацикливание"', '"бесконечно"', '"бесконечность"'):
        key_write('while True:')
    elif prompt in ('"перерыв"', '"прерывание"', '"прерывания"', '"прервать"'):
        key_write('break')
    elif prompt in ('"функция"', '"новая функция"', '"сделать функцию"', '"дев функция"'):
        key_write('def new_function():')
    elif prompt in ('"перевод строки"', '"переведи строку"', '"перенос"', '"перенос строки"'):
        key_write('\\n')
    elif prompt in ('"возврат каретки"', '"строка влево"', '"старт строки"'):
        key_write('\\r')
    elif prompt in ('" возврат на шаг"', '"возврат символа"', '"возврат буквы"'):
        key_write('\\b')
    #: печать функций и скриптов ассистента
    if prompt in ('"говорит"', '"скажет"'):
        key_write('speak')
    elif prompt == '"фраза"':
        key_write('prompt ')
    elif prompt in ('"слово"', '"слов"', '"слова"'):
        key_write('words')

    #: пишарм и гитхаб
    elif prompt in ('"паста"', '"пасту"', '"пасты"'):
        keyhot('ctrl', 'shift', 'v')
    elif prompt in ('"выделить"', '"выделение"', '"выделить все"', '"выдели все"', '"выделив все"'):
        keyhot('ctrl', 'alt', 'shift', 'j')
        print("-j", end="")
    elif prompt in ('"новый"', '"новое"', '"новая"', '"новые"'):
        keyhot('shift', 'f4')
    elif prompt in ('"камент"', '"комент"', '"коммент"'):
        keyhot('ctrl', 'k')
    elif prompt in ('"пуш"', '"закинь"', '"закинуть"'):  #: авто пуш
        keyhot('ctrl', 'k')
        time.sleep(.3)
        key_press("down")
        key_press("tab")
        key_press("tab")
        key_press("space")
        time.sleep(2)
        keyhot('ctrl', 'enter')
    elif re.match('"закинь камент|"закинуть коммент|"закинуть камент|"закинь коммент', prompt):
        keyhot('ctrl', 'k')
        time.sleep(.3)
        keyhot('ctrl', 'v')  # - закидывает из буфера
        key_press("tab")
        key_press("tab")
        key_press("space")
        time.sleep(2)
        keyhot('ctrl', 'enter')


def rimtex_personal(prompt):
    #: захват видео MSI Afterburner
    if prompt in ('"захват видео"', '"захвати видео"'):
        os.startfile(f"{path_to_shortcut}захват видео")  # ярлык MSI Afterburner
    elif prompt in ('"запись видео"', '"запиши видео"'):
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

    #: для выебонов
    elif prompt == '"ты робот"':
        keyhot('winleft', 'tab')
        keyhot('winleft', 'tab')
        time.sleep(1)
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(-50, 86, duration=0.25)
        pyautogui.moveRel(-50, -86, duration=0.25)
        pyautogui.moveTo(256, 962, duration=0.25)
        time.sleep(0.5)
        print(LRE + "♥", end='')
        click_print()
    elif prompt in ('"подтверди"', '"ты человек"'):
        time.sleep(0.2)
        pyautogui.moveTo(256, 962)
        time.sleep(0.2)
        click_print()


def rimtex_reactions(prompt, words):
    from Voice_Commands import speak_irina_tts, speak_tts, random_voice

    #: ♪ реакции на слова или фразы
    if prompt == '"я робот"':
        print(random.choice(colors) + "[-_-]", end='')
        speak_irina_tts(vocabulary.random_response_robot())
    elif prompt == '"не дано"':
        print(random.choice(colors) + "♪{•ᴥ•}♫", end='')
        speak_irina_tts(vocabulary.random_response_nedano())
    elif prompt in ('"слушай"', '"слышь"', '"слышишь"', '"слышь ты"'):
        loader.smile_gen_erator()
        speak_tts(vocabulary.random_response())
    elif any(word in prompt[1:-1] for word in ('блядь', 'нихуя', 'бля', 'ахуеть', 'бляха', 'ебать')):
        loader.smile_generator()
        speak_tts(vocabulary.sp_rec_reaction_Fuck())
    elif any(word in prompt[1:-1] for word in ('сука', 'сучара', 'охуел', 'нахуй', 'тварь')):
        loader.smile_generator()
        speak_tts("давай без агрессии")
    elif any(word in prompt[1:-1] for word in ('агрессии', 'агрессия', 'ладно')):
        print(random.choice(colors) + f"{LRE}♥ {GRE}cԅ(‾ε‾ԅ)", end='')
    elif len(words) > 0 and words[-1] in ('согласен', 'согласись'):  # - для последнего слова
        loader.smile_gen_erator()
        speak_tts("конечно. ты прав!")
        speak_tts(vocabulary.random_response_aphorism())
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
        #  print(random.choice(colors) + '( •̪O )', end='')
        #  speak_tts(vocabulary.random_anecdote())
        file_path = "F:\Rimtex\блокнот\анекдоты.txt"
        with open(file_path, 'r', encoding='utf-8') as file:
            jokes = file.read().split('\n\n')
            if jokes:
                speak_tts(random.choice(jokes))
            else:
                print("Файл с анекдотами пуст.")
