import time
import re
import keyboard
import pyautogui
import py_win_keyboard_layout
from colorama import init, Fore, Style

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


#  конвертер команд старт

def windows_show():
    # Получаем список всех окон на рабочем столе
    windows = pyautogui.getAllWindows()
    unique_windows = []
    # Выводим список приложений
    for window in windows:
        if window.title and window.title not in unique_windows:
            unique_windows.append(window.title)
            print(window.title)
            time.sleep(.02)


#: курсор
def click_print():
    pyautogui.click()
    print(f'{LCY} ∆', end='')


#: курсор в координаты
def click_print_cor(asdx, asdy, button='left'):
    cor_x, cor_y = pyautogui.position()
    pyautogui.click(x=asdx, y=asdy, button=button)
    pyautogui.moveTo(cor_x, cor_y)
    print(f'{LGR} ¤{LCY}∆', end='')


def keytrans_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    print(GRE + f"{string}" + SRA, end='')
    keyboard.write(string)  # запись в курсор


def key_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    print(YEL + f"{string}", end='')
    keyboard.write(string)  # запись в курсор


def keyrus_write(string):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04190419)  # для переключения на русскую раскладку
    print(LYE + f"{string}" + SRA, end='')
    keyboard.write(string)


def key_down(string):
    pyautogui.keyDown(string)  # зажатие клавиши
    print(f"{LCY}▾{LBL}{string}{LCY}▾{LBL} ", end='')


def key_up(string):
    pyautogui.keyUp(string)  # отпускание клавиши
    print(f"{LCY}▴{LBL}{string}{LCY}▴{LBL} ", end='')


def key_press(key):
    pyautogui.press(key)  # нажатие на клавишу
    print(Fore.LIGHTCYAN_EX + f" {key}", end='')

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
    # Нажать комбинацию клавиш
    pyautogui.hotkey(*keys)
    # Вывести информацию о нажатой комбинации клавиш
    print(F" {WHI}{LCY}{keys[0]}{WHI}{LCY}", end='')
    if len(keys) > 1:
        print(F"{WHI}‒{CYA}{keys[1]}{WHI}{LCY}", end='')
        if len(keys) > 2:
            print(F"{WHI}‒{LBL}{keys[2]}{WHI}{LCY}", end='')


def script_writing_function(prompt, words):
    #: для пишарм
    if prompt in ('"скобки"', '"скобы"', '"скобки"', '"скобка"', '"скоб очки"'):
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
    #: печать функций и скриптов ассистента
    elif prompt in ('"говорит"', '"скажет"'):
        key_write('speak')
    elif prompt == '"фраза"':
        key_write('prompt ')
    elif prompt in ('"слово"', '"слов"', '"слова"'):
        key_write('words')
    elif prompt in ('"первое слово"', '"первая слова"'):
        key_write('words[0] ')
    elif prompt in ('"клавиша"', '"клавиши"', '"клавишам"', '"кнопка"'):
        key_write('key')
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
    #: печать функций и скриптов
    elif prompt == '"печать"':
        key_write('print(" ", end="")')
    elif prompt in ('"случайно"', '"случайный"', '"рандомно"', '"рандомный"'):
        key_write(f'random.choice()')
    elif prompt in ('"проверка"', '"проверить"', '"проверим"', '"проба"', '"пробовать"', '"пробуем"'):
        key_write('try:\n')
        key_write('except Exception as e: print(e, f"")')
    elif prompt == '"если"':
        key_write('elif ')
    elif prompt in ('"число"', '"в число"', '"числа"'):
        key_write('int()')
    elif prompt in ('"длина"', '"длину"', '"длина объекта"', '"длину объекта"'):
        key_write('len()')
    elif prompt in ('"строку"', '"в строку"', '"строка"', '"строчка"'):
        key_write('str()')
    elif prompt in ('"вход"', '"вести"', '"вводить"'):
        key_write('input()')
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
    #: пишарм и гитхаб
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
    elif prompt in ('"новый"', '"новое"', '"новая"', '"новые"'):
        keyhot('shift', 'f4')
    elif prompt in ('"камент"', '"комент"', '"коммент"'):
        keyhot('alt', '0')
    elif prompt in ('"пуш"', '"закинь"', '"закинуть"'):  #: авто пуш
        keyhot('alt', '0')  # вызов окна комментирования
        time.sleep(.3)
        window_position = pyautogui.getWindowsWithTitle('Commit')[0].topleft  # Получаем позицию
        pyautogui.moveTo(window_position)  # Делаем окно активным
        pyautogui.moveRel(33, 92)  # ставим галку
        pyautogui.click()
        key_press("tab")
        key_press("tab")
        key_press("tab")
        key_press("space")
        time.sleep(2)
        keyhot('ctrl', 'enter')
    elif re.match('"закинь камент|"закинуть коммент|"закинуть камент|"закинь коммент', prompt):
        keyhot('alt', '0')
        time.sleep(.3)
        window_position = pyautogui.getWindowsWithTitle('Commit')[0].topleft
        pyautogui.moveTo(window_position)
        pyautogui.moveRel(33, 92)
        pyautogui.click()
        key_press("tab")
        key_press("space")
        keyhot('ctrl', 'v')  # закидывает из буфера
        key_press("tab")
        key_press("tab")
        key_press("space")
        time.sleep(2)
        keyhot('ctrl', 'enter')
    #: очистка буфера
    elif 3 > len(words) > 0 and (re.match(r'(\w{0,2}чист\w{0,3}\b)', words[0])) \
            and (re.match(r'(буфер\w?\b)', words[1])):
        awwx, awwy = pyautogui.position()
        keyhot('winleft', 'r')
        time.sleep(0.01)
        keyhot('winleft', 'v')
        time.sleep(.5)
        time.sleep(0.01)
        click_print_cor(373, 948)
        time.sleep(0.01)
        pyautogui.moveTo(375, 1064)
        click_print()
        click_print()
        pyautogui.moveTo(429, 1195)
        click_print()
        click_print()
        pyautogui.moveTo(awwx, awwy)
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
    elif prompt in ('"монитор"', '"приложение"'):
        print(YEL + "☼")
        windows_show()
