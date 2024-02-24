import time
import pyautogui
import keyboard

from colorama import init, Fore, Style, Back
import random
import keyword

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
BGR = Back.GREEN
BLG = Back.LIGHTGREEN_EX
SRA = Style.RESET_ALL

# выводим символ с соответствующим цветом и фоном
# print(color + background + key.name + Style.RESET_ALL, end='', flush=True)
#  r = Style.RESET_ALL
init(convert=True)
# символы показывающиеся консоли

file_path = r'F:\Rimtex\блокнот\смайлы.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print("Произошла ошибка при чтении файла:", e)


print("\n")
# Ограниченный список клавиш на клавиатуре
key_string = " ".join(pyautogui.KEYBOARD_KEYS)
key_list = []
current_line = ""
for key in key_string.split():
    if len(current_line + key) < 100 and not (len(current_line) == 0 and len(key) > 50):
        current_line += f"{key} "
    else:
        key_list.append(current_line.strip())
        current_line = f"{key} "
key_list.append(current_line.strip())
print(LYE + "\n".join(key_list))
print(SRA)
# Ограниченный список ключевых слов Python
kw_string = " ".join(keyword.kwlist)
kw_list = []
current_line = ""
for kw in kw_string.split():
    if len(current_line + kw) < 98:
        current_line += f"{kw} "
    else:
        kw_list.append(current_line.strip())
        current_line = f"{kw} "
kw_list.append(current_line.strip())
print(Fore.CYAN + " " + "\n ".join(kw_list))


print(f"""\
\r  ╓─────────────────────────────────────────────┬─────────────────────────────────╖
\r  ║ {LGR}'слова' должны быть без '"двойных"' кавычек{SRA} │ {LRE}!!!{SRA}                             ║
\r  ╠═════════════════════════════════════════════╧════════════════════════╦════════╣ 
\r  ║ {CYA}"C:\\Users\\raide\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" {SRA} ║ {LBL}Питон  {SRA}║
\r  ║ {LGR}"F:\\My_Portable_soft\\PyCharm\\bin\\pycharm64.exe"                     {SRA} ║ {GRE}Пишарм {SRA}║
\r  ╚══════════════════════════════════════════════════════════════════════╩════════╝ 
    """, sep='', end='')
#  print("-------------------------- Escape Codes: -------------------")
print(f"""\
\r{YEL} \\a{WHI} - звуковой сигнал{YEL} \\f{WHI} - прогон страницы{YEL} \\b{WHI} - возврат на шаг{YEL} \\r{WHI} - Возврат каретки
\r{YEL} \\n{WHI} - перевод строки{YEL} \\v{WHI} - вертикальная табуляция{YEL} \\t{WHI} - горизонтальная табуляция{YEL} \\{WHI} - символ эвакуации
""", sep='', end='')

print(f"""\
{RED} + Fore.RED +                                              {{Fore.RED}}               = + RED + {{RED}}
{LRE} + Fore.LIGHTRED_EX +                                      {{Fore.LIGHTRED_EX}}       = + LRE + {{LRE}}
{YEL} + Fore.YELLOW +                                           {{Fore.YELLOW}}            = + YEL + {{YEL}}
{LYE} + Fore.LIGHTYELLOW_EX +                                   {{Fore.LIGHTYELLOW_EX}}    = + LYE + {{LYE}}
{BLU} + Fore.BLUE +                                             {{Fore.BLUE}}              = + BLU + {{BLU}}
{LBL} + Fore.LIGHTBLUE_EX +                                     {{Fore.LIGHTBLUE_EX}}      = + LBL + {{LBL}}
{CYA} + Fore.CYAN +                                             {{Fore.CYAN}}              = + CYA + {{CYA}}
{LCY} + Fore.LIGHTCYAN_EX +                                     {{Fore.LIGHTCYAN_EX}}      = + LCY + {{LCY}}
{GRE} + Fore.GREEN +                                            {{Fore.GREEN}}             = + GRE + {{GRE}}
{LGR} + Fore.LIGHTGREEN_EX +                                    {{Fore.LIGHTGREEN_EX}}     = + LGR + {{LGR}}
{MAG} + Fore.MAGENTA +                                          {{Fore.MAGENTA}}           = + MAG + {{MAG}}
{LMA} + Fore.LIGHTMAGENTA_EX +                                  {{Fore.LIGHTMAGENTA_EX}}   = + LMA + {{LMA}}
{WHI} + Fore.WHITE +                                            {{Fore.WHITE}}             = + WHI + {{WHI}}
{SRA} + Style.RESET_ALL +                                       {{Style.RESET_ALL}}        = + SRA + {{SRA}}
 + {BLA}{BWH}Fore.BLACK{SRA} +                                            {{Fore.BLACK}}             = + BLA + {{BLA}}
 + {BLA}{BWH}Back.WHITE{SRA} +                                            {{Back.WHITE}}             = + BWH + {{BWH}}
 
""", sep='', end='')

current_line = ""
while True:
    # считываем клавишу с клавиатуры
    key = keyboard.read_event()
    if keyboard.is_pressed('caps lock'):  # если клавиша нажата тогда выход
        print('\a')
        time.sleep(1.1)
        exit()
    # если нажата клавиша символа
    if key.event_type == 'down' and key.name.isprintable():

        current_line += key.name + " "
        if len(current_line) >= 95:
            print(current_line)
            current_line = ""
        # генерируем случайный цвет и фон
        color = random.choice(colors)
        # background = random.choice(list(backgrounds.values()))
        #  lines = responses.strip().split('\n')
        # выводим символ с соответствующим цветом и фоном
        # print(color + background + key.name + Style.RESET_ALL, end='', flush=True)
        # print(color + key.name + Style.RESET_ALL, end=' ', flush=True)
        print(f"'{key.name}', ", end="")