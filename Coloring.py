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
SRA = Style.RESET_ALL

# выводим символ с соответствующим цветом и фоном
# print(color + background + key.name + Style.RESET_ALL, end='', flush=True)
#  r = Style.RESET_ALL
init(convert=True)
# символы показывающиеся консоли
print(f"""   
how do I remove the line break here and leave this code the same?
{Fore.LIGHTCYAN_EX}˃˃\
{Fore.LIGHTYELLOW_EX}♪-♫\
{Style.RESET_ALL}==\
{Fore.LIGHTGREEN_EX}а-я\
{Fore.LIGHTCYAN_EX}˃˃\
{Style.RESET_ALL}
      """, sep='', end='')
print("""   
"""


"""

https://stackoverflow.com/questions/40466626/simulate-alttab-in-python
code_patterns += added_code_patterns.strip().split("\n")""" """
⁞⁞⁞⁞⁞⁞⁞⁞ ⁞⁞⁞⁞⁞⁞⁞ ⁞⁞⁞⁞⁞⁞ ⁞⁞⁞⁞⁞ ⁞⁞⁞⁞ ⁞⁞⁞ ⁞⁞ ⁞ """ """
⁞ ⁞⁞ ⁞⁞⁞ ⁞⁞⁞⁞ ⁞⁞⁞⁞⁞ ⁞⁞⁞⁞⁞⁞ ⁞⁞⁞⁞⁞⁞⁞ ⁞⁞⁞⁞⁞⁞⁞⁞ """ """
ⱽ ⱺ ⱹ ⱷ ⱶ Ⱶ ⱴ ⱱ Ɒ ⱦ ȶ ȴ ȣ Ȣ ȡ ȝ Ȝ ț ȋ Ȋ ȉ Ȉ ǯ Ǯ ǃ ǀ ƿ ƾ ƺ ƹ Ƹ Ʒ Ʋ ư ƪ ƣ Ƣ Ɵ ƛ Ɩ ƕ ƍ ſ ỽ""" """
ϗ Ϙ ϙ Ϛ ϛ Ϝ ϝ Ϟ ϟ Ϡ ϡ Ϣ ϣ Ϥ ϥ Ϧ ϧ Ϩ ϩ Ϫ ϫ Ϭ ϭ Ϯ ϯ ϰ ϱ ϲ ϳ ϴ ϵ ϶ Ϸ ϸ Ϲ Ϻ ϻ ϼ Ͻ Ͼ Ͽ ℮ ᶅ """"""
ᴀ ᴁ ᴂ ᴃ ᴄ ᴅ ᴆ ᴇ ᴈ ᴉ ᴊ ᴋ ᴌ ᴍ ᴎ ᴏ ᴐ ᴑ ᴒ ᴓ ᴔ ᴕ ᴖ ᴗ ᴘ ᴙ ᴚ ᴛ ᴜ ᴝ ᴞ ᴟ ᴠ ᴡ ᴢ ᴣ ᴤ ᴥ ᴦ ᴧ ᴨ ᴩ ᴪ ᴫ """ """
ᵫ ᵬ ᵭ ᵮ ᵱ ᵲ ᵳ ᵵ ᵷ ᵸ ᵺ ᵻ Ǳ ǲ ǳ Ǆ ǅ ǆ ȸ £ ₤ ₣ ƒ ₲ ₭ ₥ ₦ ₱ ＄ $ ₮ ₩ ¥ ₴ ₰ ¤ ₪ ₯ ₠ ₧ ₨ ® © ™""" """
ⱽ ⱺ ⱹ ⱷ ⱶ Ⱶ ⱴ ⱱ Ɒ ⱦ ȶ ȴ ȣ Ȣ ȡ ȝ Ȝ ț ȋ Ȋ ȉ Ȉ ǯ Ǯ ƿ ƾ £ ¥ € $ ¢ ₡ ₢ ₵ ₫ ẟ Ɀ Ȿ ꜠ ꜡ ỻ ¶ § þ ð """ """
ƺ ƹ Ƹ Ʒ Ʋ ư ƪ ƣ Ƣ Ɵ ƛ Ɩ ƕ ƍ ſ ỽ ‽ ¶ ¿ º § ¶ ¡ ¿ ɂ Ɂ ‽ ◊ π ± √ ‰ Ω ∞ ≈ ÷ ≠ † ‡ ǂ Þ µ ƻ Ƽ ƽ """ """
$ ¢ $ € £ ¥ ₮ ฿ ₠ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ ₭ ₯ ₰ ₱ ₲ ₳ ₴ ₵ ¤ ƒ ♯ ° ø ≠ ‰ § ¶ ℓ Ⅎ ₰ ₯ Ɗɑɫë ψ """ """
ᵢ ᵣ ᵤ ᵥ ᵦ ᵧ ᵨ ᵩ ᵪ ₐ ₑ ₒ ₓ ₔ ᵢ ᴭ ᴮ ᴯ ᴰ ᴱ ᴲ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴻ ᴼ ᴽ ᴾ ᴿ ᵀ ᵁ ᵂ ᵃ ᵄ ᵆ ᵇ ᵈ ᵉ ᵊ ᵋ ᵌ """ """
ᵍ ʱ ʰ ᵎ ʲ ᵏ ᵐ ᵑ ᵒ ᵓ ᵖ ʳ ʴ ᵗ ʵ ᵘ ᵙ ᵛ ᵚ ᵝ ᵞ ᵟ ᵠ ᵡ ᶛ ᶜ ᶝ ᶞ ᶟ ᶠ ᶡ ᶢ ᶣ ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᵍ ʱ ʰ ᵎ ʲ """ """
ᵏ ᵐ ᵑ ᵒ ᵓ ᵖ ʳ ʴ ᵗ ʵ ᶰ ᵡ ᶛ ᶜ ᶠ ᶧ ᶨ ᶩ ᶪ ᶫ ᵘ ᵙ ᵛ ᵚ ᵞ ᵟ ᵠ ᶝ ᶞ ᶟ ᶡ ᶢ ᶣ ᶤ ᶥ ᶦ ᴽ ᶛ ᶜ ᶝ ᶞ ᶟ ᶠ ᶡ ᶢ ᶣ """ """
ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᶬ ᶭ ᶮ ᶯ ᶰ ᶱ ᶲ ᶳ ᶴ ᶵ ᶶ ᶷ ᶹ ᶺ ᶻ ᶼ ᶽ ᶾ ᶿ ᴬ ᴭ ᴽ ᵃ ᵄ ᵅ ᵆ ᵇ ᵈ ᵉ ᵊ ᵋ ᵌ ᵍ ᵎ ᵏ ᵐ ᵑ ᵒ """ """
ᵓ ᵖ ᵗ ᵘ ᵙ ᵚ ᵛ ᵝ ᵞ ᵟ ᵠ ᵡ ⁱ ™ ᴹᴿ° ᴮᴼˢˢ ᶦᶰᵈ ᴾᴿᴼ ™ ᴴᴰ ª ᵜ ᵔ ᵕ Ɛ ω Ɛ ³ ͡  ˵ ʱ ª ₎ ⁾ ˁ ˀ ԅ ʰ͙ᵉ͙ˡ͙ˡ͙ᵒ͙  """ """
⓿ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿ ⁰¹²³⁴⁵⁶⁷⁸⁹ ₀₁₂₃₄₅₆₇₈₉ ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ """"""
½ ⅓ ¼ ⅕ ⅙ ⅛ ⅔ ⅖ ¾ ⅗ ⅜ ⅘ ⅚ ⅝ ⅞ ⅍ ℅ © ® ™ ℗ ◊ π ∞ Σ ∑ ♯ ø ≠ ∏ ₩ ∂ ∟ ∙ √ ∞ ∩ ∫ ☺ ☻ ∆ ≈ """"""
◄▲▼► ◂▴▾▸ ˂˄˅˃ ←↑→↓←↑ ♪ ♫ ϟ ♠ ♣ ♥ ♦ · • ● ◦ ° ○ ☼ ◌ ҉ ◙ ■ ▪ ▀ ▄ ▬ ▫ □ █ ▌ ▐  """"""
↔ ↕ ♀ ♂ ‼ « » ‹› / \ ⁄ \ ⁄ | ᴕ ∞ ꜠ ꜡ ǁ ∆ """"""
ᴿᴱᴾᴱᴬᵀ ᴾᴬᵁˢᴱ ᴺᴱˣᵀ ˢᴼᴺᴳ ʳᵉᵖᵉᵃᵗ ᵖᵃᵘˢᵉ ᴺᴼᵂ ᴾᴸᴬᵞᴵᴺᴳ ᴴᵅᵖᵖᵞ ᴯⁱʳᵗʰᵈᵃᵞ ɢᵒᵒᵈ ɴⁱᵍᵗʰ ᴴᵃᵛᵉ ᵃ ⁿⁱˢᵉ ᵈᵃᵞ""" """
⌐═╤══╤╦═  ⌐╦═╤═─   ̷̷̷̷⌐╦╦═─  ⌐╦╦═─  ⌐╦═─ ▬ι═══> """"""
ʕ•̫͡ʕ•̫͡ʕ•̫͡ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʔ•̫͡•ʔ  ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ  ʕ‾•ᴥ•‾ʔ•ᴥ•‾ʔ """"""
ʕ→ᴥ←ʔʕ*ᴥ*ʔʕ→ᴥ←ʔʕ•ᴗ•ʔʕ·ᴥ·ʔʕˁȌᴥȌˀʔʕ·ᴥ·˵ʔʕ˵• ᴥ •˵ʔʅʕ•ᴥ•ʔʃʕ/·ᴥ·ʔ/\ʕ•ᴥ•ʔ/╘[´• ᵕ •`]╕ʕʘ̅ꞈʘ̅ʔ""""""
(→ᴥ←)(ᵔᴥᵔ)(^ᴥ^)(•ᴗ•)(♥ᴗ♥)(×_×)(¬_¬)(⌐■˽■)(°□°)(˘ᵕ˘ ) (Ɔ ˘ᴗ˘)♥ ( •_•)>⌐[-_-] """"""
(¬_¬")-cԅ(‾ε‾ԅ)_/'(•˛•)'\_ ┌п┐(._.)┌∩┐¯\_('-')_/¯└(`▪´)┐┌(◄_►)┐ (*´ з`)(´ε `*) """"""
(´•_•`)(•`_´•)(´-_-` )(○´ ― `)(•ŏᴗŏ•)(⁰ε ⁰ ●)(^.^(^.^*)> (=O*_*)=O \=( •̪● )=/ Q-(’̀₀’̀Q ) """ """
(o.O)(ˇò_ó)(o_O")(Ծ_Ծ)("O_o)(!o_O)!!ˁ(Ò_Ò)ˀ("o_o")("o‗o")(Θ_Θ)(ʘᴗʘ)(ǒ.ǒ)(ó_òʔ)(ʘ͜͡)(←_←)ʅ(ο_ο)ʃ """ """
(*ˊᵕˋ)~ * .·:*¨₊˚Lᵒᵛᵉᵧₒᵤ♥ ├┐╓───╖~(‾▾‾~)┌┤ «-(¯`ᴥ´¯)-«  [■□□□□□□□□□] 10%  Volume: ■■■■■□□□ """ """
•·.·''·.· .·:*¨¨*:·. ¸,ø¤º°`°º¤ø,¸ (¯`·.¸¸.·´¯`·.¸¸.-> text <-.¸¸.·´¯`·.¸¸.·´¯) """"""
..••°°°°••..°°••....••°° ¸¸.•*¨*•♫♪ ¸„.-•~¹°"ˆ˜¨ Hello ¨˜ˆ"°¹~•-.„¸ """"""
¨ … ‘ ’ „ ¸ ` ' Ꞌ ´ ^ ꞊ ꞈ │| ¦ ¯ ¬ _ ‐ ▬ ⁃ ‒ ― ─ ═ ≡ Ξ ̿ ͇  ⌠ ⌡ »»------(¯` ´¯)------»» """ """
║ ╔ ╒ ╕ ╓ ╖ ╔ ╗ ╘ ╛ ╙ ╜ ╚ ╝ ╞ ╡ ╟ ╢ ╠ ╣ ║ ╬ ╥ ╨ ╧ ╤ ╦ ╩ ╪ ╫ ╬ ├ ┤ | │ ┼ ┘┌ ┐└ ─ ┴ ┬ ⱶ Ⱶ ˩ ˥  """ """
┬┴┬┴┬┴ ╤╧╤╧╤╧ ─┬┴─┬┴ ╔╝╔╝╔╝ ▄▀▄▀▄▀  █ ▌ ▐  ░▒▓█▓▒░ ░▒▓█ █▓▒░ ░ ◙■◙ ░ ▒ ▓  ₪₪₪₪  

win-tab
delete
◄
► 




""")

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
print("")

print(f"""
ct1 = str(cta.replace(f"'", f"{Fore.LIGHTGREEN_EX}'"))
ct2 = str(ct1.replace(f")", f"){Style.RESET_ALL}"))
ct3 = str(ct2.replace(f"#", f"{Fore.LIGHTCYAN_EX} #"))
ct4 = str(ct3.replace(f"!", f"{Fore.LIGHTRED_EX}!"))
ct5 = str(ct4.replace(f"\n", f"\n{Style.RESET_ALL}"))
ct6 = str(ct5.replace(f"   e", f"{Fore.YELLOW}   e"))
ct7 = str(ct6.replace(f"os", f"{Fore.LIGHTMAGENTA_EX}os"))
ct8 = str(ct7.replace(f"    i", f"{Fore.YELLOW}    i"))
ct9 = str(ct8.replace(f"#:", f"{Fore.BLUE}#:")){Style.RESET_ALL}
    """, sep='', end='')

print(Fore.RED + ' (√¬_¬)ԅ⌐╦╦═─‒=═≡Ξ ' + Fore.LIGHTCYAN_EX + 'win-tab' + random.choice(
    colors) + ' alt-tab ctrl-s alt-F4 ' + Style.RESET_ALL)

print(f"""  \ (√¬_¬)ԅ⌐╦╦═─‒=═≡Ξ""", sep='', end='')

print(f""" 
    Fore.RED + ' (√¬_¬)ԅ⌐╦╦═─‒=═≡Ξ ' + Style.RESET_ALL
    
    {Fore.LIGHTCYAN_EX}win-tab {Style.RESET_ALL}
    {Fore.LIGHTCYAN_EX}► {Style.RESET_ALL}
    {Fore.LIGHTCYAN_EX}► {Style.RESET_ALL}
    {Fore.LIGHTCYAN_EX}► {Style.RESET_ALL}
    {Fore.LIGHTCYAN_EX}◄ {Style.RESET_ALL}
    {Fore.RED}ᴿᴱᴾᴱᴬᵀ {Style.RESET_ALL}
    {Fore.LIGHTGREEN_EX} + 'ᴿᴱᴾᴱᴬᵀ ' + {Style.RESET_ALL}
    {Fore.LIGHTRED_EX}ϟ {Style.RESET_ALL}
    {Fore.LIGHTBLUE_EX}R {Style.RESET_ALL}
          """, sep='', end='')
print(f"""
                                   + random.choice(colors) + "(⌐▪˽▪)" + Style.RESET_ALL +
{Fore.LIGHTCYAN_EX}˃˃ \                                           
{Fore.LIGHTYELLOW_EX}♪-♫ \
{Style.RESET_ALL}== \
{Fore.LIGHTGREEN_EX}а-я \
{Fore.LIGHTCYAN_EX}˃˃ \
{Style.RESET_ALL}за

""", sep='', end='')


def print_color_text(color, text):
    colors_dict = {
        'черный': Fore.BLACK,
        'синий': Fore.BLUE,
        'голубой': Fore.CYAN,
        'зеленый': Fore.GREEN,
        'светло-черный': Fore.LIGHTBLACK_EX,
        'светло-синий': Fore.LIGHTBLUE_EX,
        'светло-голубой': Fore.LIGHTCYAN_EX,
        'светло-зеленый': Fore.LIGHTGREEN_EX,
        'светло-пурпурный': Fore.LIGHTMAGENTA_EX,
        'светло-красный': Fore.LIGHTRED_EX,
        'светло-белый': Fore.LIGHTWHITE_EX,
        'пурпурный': Fore.MAGENTA,
        'белый': Fore.WHITE,
        'желтый': Fore.YELLOW,
        'красный': Fore.RED,
        'светло-желтый': Fore.LIGHTYELLOW_EX,
    }
    color_code = colors_dict.get(color.lower())
    if color_code:
        print(color_code + text + Style.RESET_ALL)
    else:
        print(text)


print_color_text('зеленый', 'Этот текст будет зеленым')
print_color_text('пурпурный', 'Этот текст будет пурпурным')
print_color_text('оранжевый', 'Этот текст будет в стандартном цвете')


def print_color_text(color, text):
    colors_dict = {
        'black': Fore.BLACK,
        'blue': Fore.BLUE,
        'cyan': Fore.CYAN,
        'green': Fore.GREEN,
        'light black': Fore.LIGHTBLACK_EX,
        'light blue': Fore.LIGHTBLUE_EX,
        'light cyan': Fore.LIGHTCYAN_EX,
        'light green': Fore.LIGHTGREEN_EX,
        'light magenta': Fore.LIGHTMAGENTA_EX,
        'light red': Fore.LIGHTRED_EX,
        'light white': Fore.LIGHTWHITE_EX,
        'magenta': Fore.MAGENTA,
        'white': Fore.WHITE,
        'yellow': Fore.YELLOW,
        'red': Fore.RED,
        'light yellow': Fore.LIGHTYELLOW_EX,
    }

    color_code = colors_dict.get(color.lower())
    if color_code:
        print(color_code + text + Style.RESET_ALL)
    else:
        print(text)


print_color_text('green', 'This text will be green')
print_color_text('purple', 'This text will be in the default color')
print(f"")

# Инициализация colorama
# init()

# Исходная строка
RCCC = " + for char in RCCC: +     "
# Печать каждого символа в случайном цвете
for char in RCCC:
    print(f"{random.choice(colors)}{char}{Style.RESET_ALL}", end='')

print(f"""{RCC}{{random.choice(colors)}}""", end='')

# Исходная строка
RCCC = "  = + RCCC "
# Печать каждого символа в случайном цвете
for char in RCCC:
    print(f"{random.choice(colors)}{char}{Style.RESET_ALL}", end='')

print(f"""{random.choice(colors)} {{RCC}}""", end='')

print(f"")



RCCC = "без агрессии"
for char in "без агрессии": print(f"\n{random.choice(colors)}{char}", end='')
print(f"""{LYE}

    # if words[-1] in ('раз', 'раза', 'пикселей', 'пиксели', 'пиксель', 'пикселя'):

    prompt = "включить запись записывать звук"
    words = prompt.split()

    # Получить последнее слово
    words = prompt.split()
    last_word = words[-1]
    print(last_word)  # Выводит: "звук"
    
    # Получить все слова, кроме последнего
    all_but_last = words[:-1]
    print(all_but_last)  # Выводит: ['включить', 'запись', 'записывать']
    
    # Получить первые два слова
    first_two = words[:2]
    print(first_two)  # Выводит: ['включить', 'запись']
    
    # Получить слова, начиная с третьего и до конца
    from_third_onwards = words[2:]
    print(from_third_onwards)  # Выводит: ['записывать', 'звук']
    
""")

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
print("")

print(
    f""" число длинны строки = {Fore.LIGHTCYAN_EX}{len(str('число длинны строки'))}{Fore.LIGHTRED_EX} 'Style.RESET_ALL!!!'{Fore.WHITE}""",
    sep='', end='')

print(f"""\
{Fore.WHITE} hotkey{Fore.WHITE}('{Fore.LIGHTGREEN_EX}winleft{Fore.WHITE}', '{Fore.LIGHTGREEN_EX}tab{Fore.WHITE}')""")

print(f"""\
\r  ╔══════════════════════════════════════════════════════════════════════╦════════╗ 
\r  ║ {CYA}"C:\\Users\\raide\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" {SRA} ║ {LBL}Питон  {SRA}║
\r  ║ {LGR}"F:\\Program Files\\PyCharm\\bin\\pycharm64.exe"                        {SRA} ║ {GRE}Пишарм {SRA}║
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

        current_line += key.name + ' '
        if len(current_line) >= 95:
            print(current_line)
            current_line = ""
        # генерируем случайный цвет и фон
        color = random.choice(colors)
        # background = random.choice(list(backgrounds.values()))
        #  lines = responses.strip().split('\n')
        # выводим символ с соответствующим цветом и фоном
        # print(color + background + key.name + Style.RESET_ALL, end='', flush=True)
        print(color + key.name + Style.RESET_ALL, end=' ', flush=True)

    # если нажата клавиша Backspace
    # elif key.event_type == 'down' and key.name == 'backspace':
    # стираем последний символ из вывода
    # print('\b \b', end='', flush=True)

    """
""""""
""""""""""""""""""


current_line = ""  # Текущая строка
while True:
    # Считываем клавишу с клавиатуры
    key = keyboard.read_event()
    if keyboard.is_pressed('caps lock'):  # Если клавиша Caps Lock нажата, то выходим из программы
        print('\a')
        time.sleep(1.1)
        exit()
    # Если нажата клавиша символа
    if key.event_type == 'down' and key.name.isprintable():
        # Генерируем случайный цвет
        color = random.choice(list(colors.values()))
        # Добавляем символ к текущей строке
        current_line += color + key.name + ' ' + Style.RESET_ALL
        # Если текущая строка содержит более 50 символов, то выводим ее и очищаем строку
        if len(current_line) >= 150:
            print(current_line)
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
        # генерируем случайный цвет и фон
        color = random.choice(colors)
        # background = random.choice(list(backgrounds.values()))
        #  lines = responses.strip().split('\n')
        # выводим символ с соответствующим цветом и фоном
        # print(color + background + key.name + Style.RESET_ALL, end='', flush=True)
        print(color + key.name + Style.RESET_ALL,max(int(str(lines))), end=' ', flush=True)
    # если нажата клавиша Backspace
    # elif key.event_type == 'down' and key.name == 'backspace':
    # стираем последний символ из вывода
    # print('\b \b', end='', flush=True)






#!!! !! !   как сделать так, чтобы надпись мигала????
while True:
    print(f""  {random.choice(colors)}      random.choice(colors)     {Style.RESET_ALL}"", sep='', end='')
    time.sleep(0.5)  # Delay for half a second before resetting the color and printing again

#!!! !! !   как сделать надпись мигающей
while True:
    color = random.choice(colors)
    print(f"{color}{Back.BLACK}  random.choice(colors)  {Style.RESET_ALL}", sep='', end='')
    time.sleep(0.5)  # Delay for half a second before switching off the background color
    print(f"{Style.RESET_ALL}  random.choice(colors)  ", sep='', end='')
    time.sleep(0.5)  # Delay for half a second before printing the colored text again



Чтобы заставить текст в консоли мигать разными цветами без печати, можно использовать библиотеку termcolor для 
установки цвета фона консоли, а затем многократно очищать консоль для создания эффекта мигания. Вот пример фрагмента 
кода, который заставит консоль мигать разными цветами:

python
Скопируйте код
импортировать время
import random
from termcolor import colored
импортировать os

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

while True:
    color = random.choice(colors)
    os.system('cls' if os.name == 'nt' else 'clear') # Очистить консоль
    print(colored('random.choice(colors)', color, 'on_grey', attrs=['bold']))  # Выведите цветной текст с серым фоном
    time.sleep(0.5) # Задержка на полсекунды перед переключением на другой цвет
Этот код использует функцию os.system() для очистки консоли (с помощью команды cls в Windows и команды clear в системах 
на базе Unix), а затем использует функцию colored() из библиотеки termcolor для установки цвета текста и цвета фона 
консоли. Аргумент attrs=['bold'] делает текст жирным для большей наглядности. Функция time.sleep() используется для
введения задержки перед переключением на другой цвет. Этот код приведет к появлению мигающей консоли, где цвет фона 
меняется каждые полсекунды.














print("-------------------------- colorama ------------------------")
print(Fore.RED + " + Fore.RED" + Fore.LIGHTRED_EX + " + Fore.LIGHTRED_EX"
      + Fore.YELLOW + " + Fore.YELLOW" + Fore.LIGHTYELLOW_EX + " + Fore.LIGHTYELLOW_EX +\n"
      + Fore.BLUE + " + Fore.BLUE" + Fore.LIGHTBLUE_EX + " + Fore.LIGHTBLUE_EX"
      + Fore.CYAN + " + Fore.CYAN" + Fore.LIGHTCYAN_EX + " + Fore.LIGHTCYAN_EX +\n"
      + Fore.GREEN + " + Fore.GREEN" + Fore.LIGHTGREEN_EX + " + Fore.LIGHTGREEN_EX"
      + Fore.MAGENTA + " + Fore.MAGENTA" + Fore.LIGHTMAGENTA_EX + " + Fore.LIGHTMAGENTA_EX +\n"
      + Fore.WHITE + " + Fore.WHITE + " + Back.WHITE + Fore.BLACK + "Fore.BLACK + Back.WHITE"
      + Style.RESET_ALL + " + Style.RESET_ALL + ")


              ╓───╖
         ╓───╢ ╔═╗ ╟───╖
   ╓───╢ ╔═╩═╣ ║ ╠═╩═╗ ╟─────╖
   ║    ║ ║   ║ ║ ║   ║ ║    ║
   ║    ║ ╚═╗ ║ ║ ║ ╔═╝ ║    ║
╔══╩══╗ ║   ║ ║ ║ ║ ║   ║ ╔══╩══╗
║     ║ ╚═══╩═╩═╩═╩═╩═══╝ ║     ║
╚═════╝                   ╚═════╝
    ║    ╔═════════════╗    ║
    ║    ║             ║    ║
    ╚════╝             ╚════╝


#

#   
#   
#   


# Ограниченный список ключевых слов Python
kw_string = " ".join(keyword.kwlist)
kw_list = []
current_line = ""
for kw in kw_string.split():
    if len(current_line + kw) < 50:
        current_line += f"{kw} "
    else:
        kw_list.append(current_line.strip())
        current_line = f"{kw} "
kw_list.append(current_line.strip())
print("\n".join(kw_list))
print("\n")

print("\n")
# Ограниченный список клавиш на клавиатуре
key_string = " ".join(pyautogui.KEYBOARD_KEYS)
key_list = []
current_line = ""
for key in key_string.split():
    if len(current_line + key) < 50 and not (len(current_line) == 0 and len(key) > 50):
        current_line += f"{key} "
    else:
        key_list.append(current_line.strip())
        current_line = f"{key} "
key_list.append(current_line.strip())
print("\n".join(key_list))










        # Ограниченный список клавиш на клавиатуре
        key_string = " ".join(keyboard.read_event())
        key_list = []
        current_line = ""
        for key in key_string.split():
            if len(current_line + key) < 50 and not (len(current_line) == 0 and len(key) > 50):
                current_line += f"{key} "
            else:
                key_list.append(current_line.strip())
                current_line = f"{key} "
        key_list.append(current_line.strip())
        print("\n".join(key_list))
        
        
        
        
current_line = ""  # Текущая строка
while True:
    # Считываем клавишу с клавиатуры
    key = keyboard.read_event()
    if keyboard.is_pressed('caps lock'):  # Если клавиша Caps Lock нажата, то выходим из программы
        print('\a')
        time.sleep(1.1)
        exit()
    # Если нажата клавиша символа
    if key.event_type == 'down' and key.name.isprintable():
        # Генерируем случайный цвет
        color = random.choice(list(colors.values()))
        # Добавляем символ к текущей строке
        current_line += color + key.name + ' ' + Style.RESET_ALL
        # Если текущая строка содержит более 50 символов, то выводим ее и очищаем строку
        if len(current_line) >= 150:
            print(current_line)
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
        # генерируем случайный цвет и фон
        # background = random.choice(list(backgrounds.values()))
        color = random.choice(list(colors.values()))
        # выводим символ с соответствующим цветом и фоном
        # print(color + background + key.name + Style.RESET_ALL, end='', flush=True)
        print(color + key.name + ' ' + Style.RESET_ALL, end='', flush=True)


    
    
# print(pyautogui.KEYBOARD_KEYS)
# print("----------------------------- pyautogui.KEYBOARD_KEYS ---------------------")
# Получить список всех клавиш на клавиатуре
keyboard_keys = pyautogui.KEYBOARD_KEYS

# Создать список строк, каждая не более 50 символов
output_list = []
current_line = ""
for key in keyboard_keys:
    if len(current_line + key + " ") <= 50:
        current_line += key + " "
    else:
        output_list.append(current_line)
        current_line = key + " "
if current_line:
    output_list.append(current_line)

# Объединить список строк с помощью символа переноса строки
output_string = "\n".join(output_list)

# Вывести ограниченную строку
print(output_string)

#  print(Fore.YELLOW + f'{keyword.kist}' + Style.RESET_ALL)
print("------------------------------------ keyword.kist --")

# Получить список всех ключевых слов Python
kw_list = keyword.kist

# Создать список строк, каждая не более 50 символов
output_list = []
current_line = ""
for kw in kw_list:
    if len(current_line + kw + " ") <= 50:
        current_line += kw + " "
    else:
        output_list.append(current_line)
        current_line = kw + " "
if current_line:
    output_list.append(current_line)

# Объединить список строк с помощью символа переноса строки
output_string = "\n".join(output_list)

# Вывести ограниченную строку
print(output_string)

    
    
    
    
    
                        #: клавиши стрелки
                    elif prompt in ('"лево"', '"влево"', '"лева"', '"в лево"', '"налево"'):
                        keyboard.press_and_release('left')
                        print(Fore.CYAN + '◄' + Style.RESET_ALL, sep='', end='')
                    elif prompt in ('"право"', '"вправо"', '"права"', '"в право"', '"направо"'):
                        keyboard.press_and_release("right")
                        print(Fore.CYAN + '►' + Style.RESET_ALL, sep='', end='')
                    elif prompt in ('"верх"', '"вверх"', '"в верх"', '"в вверх"', '"наверх"'):
                        keyboard.press_and_release("up")
                        print(Fore.CYAN + '▲' + Style.RESET_ALL, sep='', end='')
                    elif prompt in ('"низ"', '"вниз"', '"в вниз"', '"в ввниз"', '"на вниз"'):
                        keyboard.press_and_release("down")
                        print(Fore.CYAN + '▼' + Style.RESET_ALL, sep='', end='')
    
                    #: индикаторы вывода стрима
                    # elif prompt == '""':  # это удалить потом
                    #     print(print_cq9())  # и это тоже удалить потом
                    elif prompt == '""':
                        print(random.choice(colors) + '-' + Style.RESET_ALL, sep='', end='')
                    elif prompt != '""' and len(words) == 2:  # два слова
                        print(random.choice(colors) + '=' + Style.RESET_ALL, sep='', end='')
                    elif prompt != '""' and len(words) == 3:  # три слова
                        print(random.choice(colors) + '≡' + Style.RESET_ALL, sep='', end='')
                    elif prompt != '""' and len(words) == 4:  # четыре и больше
                        print(random.choice(colors) + 'Ξ' + Style.RESET_ALL, sep='', end='')
                    elif prompt != '""' and len(words) >= 10:  # десять и больше
                        print(random.choice(colors) + '¸,ø¤º°`°º¤ø,¸' + Style.RESET_ALL, sep='', end='')


    
Если вы хотите, чтобы регулярное выражение реагировало только на слова, начинающиеся с "бля" 
и имеющие не более 2 символов после, вы можете использовать следующий код:
    elif len(words) == 1 and re.match(r'бля\w{0,2}\b', words[0]):
    print(prompt, sep='', end='')
Здесь \b обозначает границу слова, то есть регулярное выражение будет реагировать только на слова, которые начинаются 
с "бля" и имеют не более 2 символов после этого, и которые заканчиваются границей слова (то есть не имеют 
дополнительных символов после).
Таким образом, это выражение будет реагировать только на слова "блядь", "бля", "бляь" и "бляха", и не будет
реагировать на слова "блядина" или "блядство".
    
    r'бля[тьд]?'
Здесь [тьд]? означает, что следующий символ может быть либо "т", "д", либо отсутствовать вовсе. 
Таким образом, данное выражение будет находить только строки "бля", "блядь" и "блять".

    r'бля.{0,2}'
Здесь .{0,2} означает, что любой символ может повторяться от 0 до 2 раз.

    r'бля\w{0,2}'
if len(words) == 1 and re.match(r'бля\w{0,2}', words[0]):
\w обозначает любой символ слова (буквы, цифры, знак подчеркивания), а 
{0,2} указывает, что такой символ может повторяться от 0 до 2 раз.

if len(words) == 2 and re.match(r'(библиотек[ау]{0,1})|(модул[ьи]?.{0,1})|(пип.{0,1})', words[1]):
объясни подробнее про эти вещи Конечно, я объясню каждый из этих элементов:

[ау] - это символьный класс, который соответствует одной из двух букв "а" или "у". 
Символьный класс - это набор символов, которые могут 
соответствовать любому символу в заданном месте регулярного выражения. Таким образом, 
[ау] означает, что регулярное выражение будет соответствовать любому символу, который является либо "а", либо "у".

{0,1} - это квантификатор, который указывает, что предыдущий
символ или символьный класс может появляться ноль или один раз. 
Таким образом, [ау]{0,1} означает, что символы "а" или "у" могут появляться ноль или один раз. 
Это альтернативная запись для 
?,которая также означает, что символ или символьный класс может появиться ноль или один раз.

. - это метасимвол, который соответствует любому символу, кроме символа новой строки. Таким образом, .
{0,1} означает, что регулярное выражение будет соответствовать любому символу, который появляется ноль или один раз.

В итоге, выражение (библиотек[ау]?.{0,1}) соответствует строке, содержащей слово "библиотека" или "библиотеку",
после которого может следовать символ "а" или "у" (но это не обязательно), а затем может следовать ноль или один символ.








если нажата клавиша Backspace
elif key.event_type == 'down' and key.name == 'backspace':
стираем последний символ из вывода
print('\b \b', end='', flush=True)

 print("--------------------------------------pyautogui----------------------------------------")
screenWidth, screenHeight = pyautogui.size() # Возвращает два целых числа, ширину и высоту экрана.
(Основной монитор, в многомониторных установках).
currentMouseX, currentMouseY = pyautogui.position() # Возвращает два целых числа,
x и y текущей позиции курсора мыши.
pyautogui.moveTo(100, 150) # Переместите мышь в координаты x, y 100, 150.
pyautogui.click() # Щелкните мышью в ее текущем положении.
pyautogui.click(200, 220) # Щелкните мышью в координатах x, y 200, 220.
pyautogui.move(None, 10) # Переместите мышь на 10 пикселей вниз, то есть переместите мышь относительно ее текущего
положения.
pyautogui.doubleClick() # Двойной щелчок мышью в точке
pyautogui.moveTo(500, 500, duration=2,
tween=pyautogui.easeInOutQuad) # Используйте функцию tweening/easing для перемещения мыши в течение 2 секунд.
pyautogui.write('Hello world!', interval=0.25) # Набираем текст с четвертьсекундной паузой между нажатиями.
pyautogui.press('esc') # Имитация нажатия клавиши Escape.
pyautogui.keyDown('shift')
pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')

print("---------  Escape Codes: \b, \t, \n, \a, \r : String Escape « String « Python  ---------
       -----------  http://www.java2s.com/Code/Python/String/EscapeCodesbtnar.htm  ------------
       ---------------  https://ru.wikipedia.org/wiki/Управляющие_символы  --------------------")
s = "e:\\Beginner"
s1 = "e:" "\\" "Beginner"
s2 = s1 + \
     "\\tst.py"

print("This is a DOS path:", s)
print("This is a DOS path:", s1)
print("This is a DOS path:", s2)

s3 = "I contain 'single' quotes"

print(s3)

s6 = "I contain\t\t\tthree\t\t\ttabs"
s7 = "I contain a\t\v\tvertical tab"
s8 = "I contain a\t\a\tBELL, which you can hear"

print(s6)
print(s7)
print(s8)

s9 = "I contain a BACK\bSPACE"
s10 = "I contain a BACKK\bSPACE AND a \nNEINE and a \rLINEFEED"
s11 = "I ve got a FORM\fFEED!"

print(s9)
print(s10)
print()
print(s11)

s12 = "If Python doesn't know what the escape code\n" \
      "means, it performs the identity operation!  \identity!"
s13 = "But if you don't know what a code means, don't use it!"

print(s12)
print(s13)

print("---------------------Запуск новой копии интерпретатора команд Windows.--------------------"
     "   \n"
     "   CMD [/A | /U] [/Q] [/D] [/E:ON | /E:OFF] [/F:ON | /F:OFF] [/V:ON | /V:OFF]\n"
     "       [[/S] [/C | /K] строка]\n"
     "   \n"
     "   /C      Выполнение указанной команды (строки) с последующим завершением.\n"
     "   /K      Выполнение указанной команды (строки) без последующего завершения.\n"
     "   /S      Изменение поведения после /C или /K (см. ниже)\n"
     "   /Q      Отключение режима вывода команд на экран (ECHO).\n"
     "   /D      Отключение выполнения команд AutoRun из реестра (см. ниже)\n"
     "   /A      Вывод результатов выполнения команд в формате ANSI.\n"
     "   /U      Вывод результатов выполнения команд в формате UNICODE.\n"
     "   /T:fg   Выбор цвета переднего плана/фона (более подробно см. COLOR /?)\n"
     "   /E:ON   Разрешение расширенной обработки команд (см. ниже)\n"
     "   /E:OFF  Запрет расширенной обработки команд (см. ниже)\n"
     "   /F:ON   Разрешение символов завершения имен файлов и папок (см. ниже)\n"
     "   /F:OFF  Запрет символов завершения имен файлов и папок (см. ниже)\n"
     "   /V:ON   Разрешение отложенного расширения переменных среды с применением\n"
     "\n"
     "    https://learn.microsoft.com/ru-ru/windows/terminal/command-line-arguments?tabs=windows\n"
     "\n"
     )

70 горячих клавиш Google Chrome, которые должен знать каждый
https://lifehacker.ru/best-google-chrome-shortcuts/



















def create_command(prompt):
# Создаем регулярное выражение, которое ищет соответствия, начинающиеся с "созд", за которым может 
следовать 0-2 буквы (например, "а" или "ание"), за которым следует ноль или более пробелов, за которым 
следует "команд", за которым может следовать 0-1 буквы (например, "а" или "ы").
pattern1 = r'созд[а-я]{0,2}\s*команд[а-я]?'
# Создаем регулярное выражение, которое ищет соответствия, начинающиеся с "создал", за которым может 
следовать 0-3 буквы (например, "а", "ание" или "ить"), за которым следует ноль или более пробелов, за которым 
следует "коман", за которым может следовать 0-1 буквы (например, "д", "о" или "й").
pattern2 = r'создал[а-я]{0,3}\s*коман[дой]?'
# Ищем соответствия в строке prompt с помощью первого и второго регулярного выражения.
if re.search(pattern1, prompt) or re.search(pattern2, prompt):
# Возвращаем True, если нашли соответствие.
return True
else:
# Возвращаем False, если не нашли соответствие.
return False    



https://stackoverflow.com/questions/854393/change-keyboard-locks-in-python  для раскладки
https://stackoverflow.com/questions/71918479/how-to-change-the-keyboard-layout-language-in-windows-10-with-python

keyboard.add_abbreviation('@', 'raider@ukr.net')  # для записываяния почты
keyboard.add_abbreviation('@@', 'rimtexx@gmail.com')
keyboard.add_abbreviation('@@@', 'dmrimtex@gmail.com')
keyboard.add_abbreviation('@@@@', 'dmrimtex@mail.ru')
keyboard.add_abbreviation('1@', 'о пэн апи @ @')  # ключи о пэн апи @ @
keyboard.add_abbreviation('2@', 'my.long.email@example.com')  # пароль ++ сделать скрипт

pip uninstall
Использование

Windows
py -m pip uninstall [options] <пакет> ...
py -m pip uninstall [options] -r <файл требований> ...
Описание
Деинсталляция пакетов.

pip может деинсталлировать большинство установленных пакетов. Известными исключениями являются:

Чистые пакеты distutils, установленные с помощью python setup.py install, 
которые не оставляют метаданных для определения того, какие файлы были установлены.

Обертки сценариев, устанавливаемые python setup.py develop.

Опции

-r, --requirement <файл>.
Деинсталлировать все пакеты, перечисленные в данном файле требований. Эта опция может быть использована несколько раз.

-y, --yes
Не запрашивать подтверждение удаления.

--root-user-action <root_user_action>
Действие, если pip запущен от имени пользователя root. По умолчанию выдается предупреждение.

--break-system-packages
Разрешить pip изменять установку Python, управляемую извне.

Примеры
Деинсталлировать пакет.

Windows
C:\> py -m pip uninstall simplejson   
Деинсталляция simplejson:
/home/me/env/lib/python3.9/site-packages/simplejson
/home/me/env/lib/python3.9/site-packages/simplejson-2.2.1-py3.9.egg-info
Продолжить (Y/n)? y
Успешно деинсталлирован simplejson


              # # Рисование квадрата с помощью мыши
           elif 1 < len(words) <= 5 and words[0] in ('нарисуй', 'рисуй', 'рисования', 'рисованием', 'рисунок'):
               if words[1] == 'квадрат':
                   pyautogui.mouseDown()
                   pyautogui.moveRel(100, 0)  # вправо сто пикселей
                   pyautogui.moveRel(0, 100)  # вниз сто пикселей
                   pyautogui.moveRel(-100, 0)  # влево сто пикселей
                   pyautogui.moveRel(0, -100)  # вверх сто пикселей
                   pyautogui.mouseUp()
               if words[1] == 'треугольник':
                   pyautogui.mouseDown()
                   pyautogui.moveRel(100, 0)
                   pyautogui.moveRel(-50, 86)
                   pyautogui.moveRel(-50, -86)
                   pyautogui.mouseUp()

ttps://github.com/asweigart/pyautogui
# Координаты, где нужно кликнуть правой кнопкой мыши
x = 100
y = 200
pyautogui.click(x, y)
pyautogui.click(x, y, button='right')

screen_width, screen_height = pyautogui.size() # Получение размеров экрана
pyautogui.moveTo(screen_width / 2, screen_height / 2) # Перемещение мыши в центр экрана

pyautogui.click() # Клик левой кнопкой мыши на текущем месте курсора
pyautogui.doubleClick() # Двойной щелчок мышью
pyautogui.mouseDown() # Нажатие левой кнопки мыши
pyautogui.mouseUp() # Отпускание левой кнопки мыши
pyautogui.mouseDown(button='right') # Нажатие правой кнопки мыши

pyautogui.scroll(10) # Прокрутка колеса мыши вверх на 10 пикселей
pyautogui.scroll(-10) # Прокрутка колеса мыши вниз на 10 пикселей

# Перемещение мыши на координаты (x, y)
x = 100
y = 200
pyautogui.moveTo(x, y)

Перемещение мыши на 100 пикселей вправо и 50 пикселей вниз от текущего положения
pyautogui.moveRel(100, 50)

# Получение текущих координат курсора мыши
x, y = pyautogui.position()
print(f"Текущие координаты: x={x}, y={y}")   

 # # перемещениe и Рисование с помощью мыши
pyautogui.mouseDown()
pyautogui.moveTo(100, 200, duration=0.25)
pyautogui.moveTo(200, 200, duration=0.25)
pyautogui.moveTo(200, 100, duration=0.25)
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(100, 200, duration=0.25)
pyautogui.mouseUp()


jjhgjhgj hgjhg jghjkg

# for voice in voices:
    # print(voice.GetAttribute("Name"))
Microsoft Irina Desktop
Microsoft David Desktop
Microsoft Zira Desktop
Microsoft Paulina Desktop
Microsoft Pavel Mobile
    """
    #  C:\Users\raide\AppData\Local\Programs\Python\Python311\python.exe в питон
    """
"F:\Program Files\PyCharm\bin\pycharm64.exe" для указания запуска в пишарме вставить перед  расположением в объекте

-----------------------------------------------------------------------------------------------
Установить библиотеки:                                   pip install -r requirements.txt
Обновить библиотеки:                                     pip install --upgrade -r  requirements.txt
Удалить библиотеки:                                      pip uninstall -r  requirements.txt
-----------------------------------------------------------------------------------------------
Просмотреть список установленных библиотек:              pip list
Проверка установленных пакетов на наличие обновлений:    pip check
Вывод списка установленных пакетов с версиями:           pip freeze
Поиск пакета в репозитории PyPI:                         pip search <package>
Просмотреть информацию о библиотеке:                     pip show <package>
Просмотреть информацию о библиотеке в формате JSON:      pip show --json <package>
Просмотреть исходный код библиотеки:                     pip download <package>
Установка версии пакета с указанной версией:             pip install <package>==<version>
Установка пакета с указанной или более поздней версией:  pip install <package>~=<version>
-----------------------------------------------------------------------------------------------

print(
    f"{Fore.LIGHTCYAN_EX}˃˃ {Fore.LIGHTYELLOW_EX}♪-♫ {Style.RESET_ALL}== "
    f"{Fore.LIGHTGREEN_EX}а-я {Style.RESET_ALL} ", sep='', end='') 
"F:\Program Files\PyCharm\bin\pycharm64.exe"
speak = wincl.Dispatch("SAPI.SpVoice")
speak.GetVoices()


# ╭ ─ ╮ ─ ╰ ─ ╯


    """""""""""""""""""""
    """"""

#
# print(f"""\
# \n{Fore.LIGHTCYAN_EX}˃˃ \
# \n{Fore.LIGHTYELLOW_EX}♪-♫ \
# \n{Style.RESET_ALL}== \
# \n{Fore.LIGHTGREEN_EX}а-я \
# \n{Style.RESET_ALL}\
# """, sep='', end='')
# ak_tts("запись отключена! ")
#
#    ….…...../"\........./"\
#    ….….....\..:-"""-:…./
#    ……......`;'….//`\.../
#    ……...../…__.....|.."('.
#    .....…..|.O./O)\....\..`)
#    ......._/-.....`......`"`..|`-.
#    .....-=;.`................../...`-.
#    .../o.o.\...,_,....................'.
#    ...L._._;_.-'........................`'-.
#    .....`'-.`.............'.................`'-.
#    .........`..........'........................`-._
#    ...........'-._..-'..............................'.
#    ..............\....................................`\
#    ...............|.....................................\
#    ...............|....|.................................;..._.
#    ...............\....|...........|.....................|-.((
#    ................;...\.........../..../................|-.` )
#    ................|.'..;........./....|.................|(_). )
#    ................|...\.\......./`....|.................;'- -'
#    .................\...'.\..../`......|................/
#    ..................|.../`|.;........\.............../
#    ..................|..|..|..|-._......'.............'
#    ................../..|..|..|__.`'---"_;'-.......-
