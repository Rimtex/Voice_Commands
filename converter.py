# преобразователь команд в понятный текст для показа!!!
import random
import re
from colorama import init, Fore, Style, Back

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


"""   
"""






init()

# преобразователь команд в понятный текст для показа!!!
filename = "Voice_Commands.py"  # имя файла
start_marker = "конвертер команд старт"  # начальный маркер
end_marker = "конвертер команд конец"  # конечный маркер

# вырезаем лишние строки
code_patterns = ["hhvvhhvv", "ъ", "ъ", "ъ", "ъ", "ъ", "ъ", "ъ", "ъ", "ъ", "ъ", "ъ"]

# вырезаем копи пастой можно из низа пишарма или ассистента. удобненько
added_code_patterns = """
speak
Fore
if re.match
print
"""
code_patterns += added_code_patterns.strip().split("\n")

with open(filename, encoding="utf-8") as f:
    print_started = False
    ctline = ""
    for line in f:  # только строки содержащие русские буквы, добавлять так - [а-яА-Я]|нужные строки|еще нужные строки|
        if re.search('[а-яА-Я]', line):  # ! если надо добавлять так - [а-яА-Я]|нужные строки|еще нужные строки|
            if end_marker in line:
                break
            if print_started:
                # заменяем строки, содержащие куски кода из заданных шаблонов, на пустые строки
                skip_line = any(pattern in line for pattern in code_patterns)
                if not skip_line:
                    ctline += line
            elif start_marker in line:
                print_started = True

# print(ctline)
cta = ctline

#  замена условий и тонкая настройка и покраски
ct1 = str(cta.replace(f"\n", f"\n{Style.RESET_ALL}"))
ct2 = str(ct1.replace(f"", f""))
ct3 = str(ct2.replace(f'', f''))
ct4 = str(ct3.replace(f"", f""))
ct5 = str(ct4.replace(f"", f""))
ct6 = str(ct5.replace(":", ": "))
ct7 = str(ct6.replace(f"                 ", f"                 {Fore.YELLOW}"))
ct8 = str(ct7.replace(f"(", f"{Style.RESET_ALL}("))
ct9 = str(ct8.replace(f"'", f"{Style.RESET_ALL}'{Fore.LIGHTGREEN_EX}"))
cr1 = str(ct9.replace(f'"', f'{Style.RESET_ALL}"{Fore.LIGHTGREEN_EX}'))
cr2 = str(cr1.replace(f",", f"{Fore.LIGHTRED_EX},{Style.RESET_ALL}"))
cr3 = str(cr2.replace(f"", f""))
cr4 = str(cr3.replace(f"", f""))
cr5 = str(cr4.replace(f")", f"{Style.RESET_ALL})"))
cr6 = str(cr5.replace(f"", f""))
cr7 = str(cr6.replace(f" or ", f"{Style.RESET_ALL} or "))
cr8 = str(cr7.replace(f"", f""))
cr9 = str(cr8.replace(f"#: ", f"{Fore.LIGHTCYAN_EX}#: "))

cq1 = str(cr9.replace(f"# ", f"{Fore.LIGHTBLUE_EX}# "))
cq2 = str(cq1.replace(f"!", f"{Fore.LIGHTRED_EX}!"))
cq3 = str(cq2.replace(f"", f""))
cq4 = str(cq3.replace(f"random.choice(colors)", f"{Fore.MAGENTA}random.choice(colors)"))
cq5 = str(cq4.replace(f"Fore", f"{Fore.LIGHTMAGENTA_EX}Fore"))
cq6 = str(cq5.replace(f"", f""))
cq7 = str(cq6.replace(f"", f""))
cq8 = str(cq7.replace(f'', f''))
cq9 = str(cq8.replace(f'', f''))
def print_cq9():
    responses = cq9  # результат
    return responses

#: ! нормальная покраска
cs1 = str(cq9.replace(f"", f""))
cs2 = str(cs1.replace(f"", f""))
cs3 = str(cs2.replace(f"", f""))
cs4 = str(cs3.replace(f"", f""))
cs5 = str(cs4.replace(f"", f""))
cs6 = str(cs5.replace(f"", f""))
cs7 = str(cs6.replace(f"", f""))
cs8 = str(cs7.replace(f"", f""))
cs9 = str(cs8.replace(f"", f""))




#  if re.search('[а-яА-Я]|Fore|random.choice(colors)|RED|LRE|YEL|LYE|BLU|LBL|CYA|LCY|GRE|LGR|MAG|LMA|WHI|SRA|',line):


# cq5 = str(cq4.replace("", ""))
# cq6 = str(cq5.replace("", ""))
# cq7 = str(cq6.replace("", ""))

# cq5 = str(cq4.replace("                    ", " "))  # убираем отступы иначе консоль не все будет показывать
# cq6 = str(cq5.replace("\n\n\n", "\n\n"))  # убираем пустые строки
# cq7 = str(cq6.replace("\n\n", "\n"))      # убираем пустые строки


#  https://tproger.ru/translations/regular-expression-python/
#  ct1 = re.match(r'i', ct)
#  print(ct1.group(0))
