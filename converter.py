#: преобразователь команд в понятный текст для показа!!!
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

#: преобразователь команд в понятный текст для показа!!!
filename = "Voice_Commands.py"  # имя файла
keyboard_scripts = "keyboard_scripts.py"

start_marker = "конвертер команд старт"  # начальный маркер
end_marker = "конвертер команд конец"  # конечный маркер

#: вырезаем лишние строки
code_patterns = ["hhvvhhvv", "hgtfndgudjed7y564y"]  # для символов с пробелом

#: вырезаем копи пастой можно из низа пишарма или ассистента. удобненько
added_code_patterns = """
speak
Fore
if re.match
print
os.start
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
                # заменяем строки, содержащие куски кода из заданных шаблонов на пустые строки
                skip_line = any(pattern in line for pattern in code_patterns)
                if not skip_line:
                    ctline += line
            elif start_marker in line:
                print_started = True

# print(ctline)
cta = ctline

#: замена условий
#: покраски
paint = str(cta
            .replace(f"\n", f"\n{SRA}")
            .replace(f",", f"{LYE},{SRA}")
            .replace(f"(", f"{SRA}(")
            .replace(f"'", f"{SRA}'{LGR}")
            .replace(f'"', f'{SRA}"{LGR}')
            .replace(f")", f"{SRA})")
            .replace(f" or ", f"{SRA} or ")
            .replace(f" and ", f"{SRA} and ")
            .replace(f"#: ", f"{LCY}#: ")
            .replace(f"# ", f"{CYA}# ")
            .replace(f"!", f"{LRE}!")
            .replace(f"random.choice(colors)", f"{MAG}random.choice(colors)")
            .replace(f"Fore", f"{LMA}Fore")
            )

#: перевод значений
trans = str(paint
            .replace(" False ", " ложь ").replace(" None ", " ничего ").replace(" True ", " истина ")
            .replace(" and ", " и ").replace(" as ", " как ").replace(" assert ", " утверждать ")
            .replace(" async ", " асинхронный ").replace(" await ", " ожидать ").replace(" break ", " прервать ")
            .replace(" class ", " класс ").replace(" words ", " слов ").replace(" continue ", " продолжить ")
            .replace(" def ", " определить ").replace(" del ", " удалить ").replace(" elif ", " иначе если ")
            .replace(" else ", " иначе ").replace(" except ", " исключение ").replace(" finally ", " в конечном итоге ")
            .replace(" for ", " для ").replace(" from ", " из ").replace(" global ", " глобальный ")
            .replace(" if ", " если ").replace(" import ", " импорт ").replace(" in ", " в ").replace(" is ", " это ")
            .replace(" lambda ", " лямбда ").replace(" nonlocal ", " нелокальный ").replace(" not ", " не ")
            .replace(" or ", " или ").replace(" pass ", " пропуск ").replace(" raise ", " поднять ")
            .replace(" return ", " вернуть ").replace(" try ", " попытаться ").replace(" while ", " пока ")
            .replace(" with ", " с ").replace(" yield ", " передавать ")
            .replace(" prompt ", " фраза ")
            .replace(" prompt[1:-1] ", " фразe ")
            .replace("word ", "слово ")
            .replace("words", "слов")
            .replace("слов[0]", "первое_слово")
            .replace("слов[1]", "второе_слово")
            .replace("слов[-1]", "последнее_слово")
            .replace("any", "любое")
            .replace(" len", " число")
            .replace(" any ", " любое ").replace(" range", " любое")
            .replace(" words_num ", " словарь_чисел ")
            )

#: удаление лишнего
delete = str(trans
             .replace(" иначе ", "")
             .replace(" если ", "")
             )


def convert_paint():  # результат
    responses = paint
    return responses


def convert_trans():  # результат с переводом
    responses = trans
    return responses


def convert_delete():  # результат с удалением лишнего
    responses = delete
    return responses

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
