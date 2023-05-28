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

print("""   
https://stackoverflow.com/questions/40466626/simulate-alttab-in-python
ⱽ ⱺ ⱹ ⱷ ⱶ Ⱶ ⱴ ⱱ Ɒ ⱦ ȶ ȴ ȣ Ȣ ȡ ȝ Ȝ ț ȋ Ȋ ȉ Ȉ ǯ Ǯ ǃ ǀ ƿ ƾ ƺ ƹ Ƹ Ʒ Ʋ ư ƪ ƣ Ƣ Ɵ ƛ Ɩ ƕ ƍ ſ ỽ
ϗ Ϙ ϙ Ϛ ϛ Ϝ ϝ Ϟ ϟ Ϡ ϡ Ϣ ϣ Ϥ ϥ Ϧ ϧ Ϩ ϩ Ϫ ϫ Ϭ ϭ Ϯ ϯ ϰ ϱ ϲ ϳ ϴ ϵ ϶ Ϸ ϸ Ϲ Ϻ ϻ ϼ Ͻ Ͼ Ͽ ℮ ᶅ
ᴀ ᴁ ᴂ ᴃ ᴄ ᴅ ᴆ ᴇ ᴈ ᴉ ᴊ ᴋ ᴌ ᴍ ᴎ ᴏ ᴐ ᴑ ᴒ ᴓ ᴔ ᴕ ᴖ ᴗ ᴘ ᴙ ᴚ ᴛ ᴜ ᴝ ᴞ ᴟ ᴠ ᴡ ᴢ ᴣ ᴤ ᴥ ᴦ ᴧ ᴨ ᴩ ᴪ ᴫ 
ᵫ ᵬ ᵭ ᵮ ᵱ ᵲ ᵳ ᵵ ᵷ ᵸ ᵺ ᵻ Ǳ ǲ ǳ Ǆ ǅ ǆ ȸ £ ₤ ₣ ƒ ₲ ₭ ₥ ₦ ₱ ＄ $ ₮ ₩ ¥ ₴ ₰ ¤ ₪ ₯ ₠ ₧ ₨ ® © ™
ⱽ ⱺ ⱹ ⱷ ⱶ Ⱶ ⱴ ⱱ Ɒ ⱦ ȶ ȴ ȣ Ȣ ȡ ȝ Ȝ ț ȋ Ȋ ȉ Ȉ ǯ Ǯ ƿ ƾ £ ¥ € $ ¢ ₡ ₢ ₵ ₫ ẟ Ɀ Ȿ ꜠ ꜡ ỻ ¶ § þ ð 
ƺ ƹ Ƹ Ʒ Ʋ ư ƪ ƣ Ƣ Ɵ ƛ Ɩ ƕ ƍ ſ ỽ ‽ ¶ ¿ º § ¶ ¡ ¿ ɂ Ɂ ‽ ◊ π ± √ ‰ Ω ∞ ≈ ÷ ≠ † ‡ ǂ Þ µ ƻ Ƽ ƽ 
$ ¢ $ € £ ¥ ₮ ฿ ₠ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ ₭ ₯ ₰ ₱ ₲ ₳ ₴ ₵ ¤ ƒ ♯ ° ø ≠ ‰ § ¶ ℓ Ⅎ ₰ ₯ Ɗɑɫë ψ
ᵢ ᵣ ᵤ ᵥ ᵦ ᵧ ᵨ ᵩ ᵪ ₐ ₑ ₒ ₓ ₔ ᵢ ᴭ ᴮ ᴯ ᴰ ᴱ ᴲ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴻ ᴼ ᴽ ᴾ ᴿ ᵀ ᵁ ᵂ ᵃ ᵄ ᵆ ᵇ ᵈ ᵉ ᵊ ᵋ ᵌ
ᵍ ʱ ʰ ᵎ ʲ ᵏ ᵐ ᵑ ᵒ ᵓ ᵖ ʳ ʴ ᵗ ʵ ᵘ ᵙ ᵛ ᵚ ᵝ ᵞ ᵟ ᵠ ᵡ ᶛ ᶜ ᶝ ᶞ ᶟ ᶠ ᶡ ᶢ ᶣ ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᵍ ʱ ʰ ᵎ ʲ 
ᵏ ᵐ ᵑ ᵒ ᵓ ᵖ ʳ ʴ ᵗ ʵ ᶰ ᵡ ᶛ ᶜ ᶠ ᶧ ᶨ ᶩ ᶪ ᶫ ᵘ ᵙ ᵛ ᵚ ᵞ ᵟ ᵠ ᶝ ᶞ ᶟ ᶡ ᶢ ᶣ ᶤ ᶥ ᶦ ᴽ ᶛ ᶜ ᶝ ᶞ ᶟ ᶠ ᶡ ᶢ ᶣ 
ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᶬ ᶭ ᶮ ᶯ ᶰ ᶱ ᶲ ᶳ ᶴ ᶵ ᶶ ᶷ ᶹ ᶺ ᶻ ᶼ ᶽ ᶾ ᶿ ᴬ ᴭ ᴽ ᵃ ᵄ ᵅ ᵆ ᵇ ᵈ ᵉ ᵊ ᵋ ᵌ ᵍ ᵎ ᵏ ᵐ ᵑ ᵒ 
ᵓ ᵖ ᵗ ᵘ ᵙ ᵚ ᵛ ᵝ ᵞ ᵟ ᵠ ᵡ ⁱ ™ ᴹᴿ° ᴮᴼˢˢ ᶦᶰᵈ ᴾᴿᴼ ™ ᴴᴰ ª ᵜ ᵔ ᵕ Ɛ ω Ɛ ³ ͡  ˵ ʱ ª ₎ ⁾ ˁ ˀ ԅ  ʰ͙ ᵉ͙ˡ͙ˡ͙ᵒ͙
⓿ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿ ⁰¹²³⁴⁵⁶⁷⁸⁹ ₀₁₂₃₄₅₆₇₈₉ ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ 
½ ⅓ ¼ ⅕ ⅙ ⅛ ⅔ ⅖ ¾ ⅗ ⅜ ⅘ ⅚ ⅝ ⅞ ⅍ ℅ © ® ™ ℗ ◊ π ∞ Σ ∑ ♯ ø ≠ ∏ ₩ ∂ ∟ ∙ √ ∞ ∩ ∫ ☺ ☻ ∆ ≈
◄▲▼► ◂▴▾▸ ˂˄˅˃ ≤≥ ←↑→↓←↑↔↕↨ ♪ ♫ ϟ ♠ ♣ ♥ ♦ · • ● ◦ ° * ○ ☼ ¤ ◌ ҉ ◙ ■ ▪ ▀ ▄ ▬ ▫ □ █ ▌ ▐     
↔ ↕ ♀ ♂ ‼ « » ‹› /  ⁄  ⁄ | ᴕ ∞ ꜠ ꜡ ǁ ∆ 
ᴿᴱᴾᴱᴬᵀ ᴾᴬᵁˢᴱ ᴺᴱˣᵀ ˢᴼᴺᴳ ʳᵉᵖᵉᵃᵗ ᵖᵃᵘˢᵉ ᴺᴼᵂ ᴾᴸᴬᵞᴵᴺᴳ ᴴᵅᵖᵖᵞ ᴯⁱʳᵗʰᵈᵃᵞ ɢᵒᵒᵈ ɴⁱᵍᵗʰ ᴴᵃᵛᵉ ᵃ ⁿⁱˢᵉ ᵈᵃᵞ
⌐═╤══╤╦═  ⌐╦═╤═─   ̷̷̷̷⌐╦╦═─  ⌐╦╦═─  ⌐╦═─ ▬ι═══>
ʕ•̫͡ʕ•̫͡ʕ•̫͡ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʔ•̫͡•ʔ  ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ  ʕ‾•ᴥ•‾ʔ•ᴥ•‾ʔ
ʕ→ᴥ←ʔʕ*ᴥ*ʔʕ→ᴥ←ʔʕ•ᴗ•ʔʕ·ᴥ·ʔʕˁȌᴥȌˀʔʕ·ᴥ·˵ʔʕ˵• ᴥ •˵ʔʅʕ•ᴥ•ʔʃʕ/·ᴥ·ʔ/\ʕ•ᴥ•ʔ/╘[´• ᵕ •`]╕ʕʘ̅ꞈʘ̅ʔ 
(→ᴥ←)(ᵔᴥᵔ)(^ᴥ^)(•ᴗ•)(♥ᴗ♥)(×_×)(¬_¬)(⌐■˽■)(°□°)(˘ᵕ˘ ) (Ɔ ˘ᴗ˘)♥ ( •_•)>⌐ {˶•ᴗ•˶}[-_-]{•ᴥ•}
(¬_¬")-cԅ(‾ε‾ԅ)_/'(•˛•)'\_ ┌п┐(._.)┌∩┐¯\_('-')_/¯└(`▪´)┐┌(◄_►)┐ (*´ з`)(´ε `*)
(´•_•`)(•`_´•)(´-_-` )(○´ ― `)(•ŏᴗŏ•)(⁰ε ⁰ ●)(^.^(^.^*)> (=O*_*)=O \=( •̪● )главный=/ Q-(’̀₀’̀Q ) 
(o.O)(ˇò_ó)(o_O")(Ծ_Ծ)("O_o)(!o_O)!!ˁ(Ò_Ò)ˀ("o_o")("o‗o")(Θ_Θ)(ʘᴗʘ)(ǒ.ǒ)(ó_òʔ)(ʘ͜͡)(←_←)ʅ(ο_ο)ʃ
(*ˊᵕˋ)~ * .·:*¨₊˚Lᵒᵛᵉᵧₒᵤ♥ ├┐╓───╖~(‾▾‾~)┌┤ «-(`¯ᴥ¯´)-«  [■□□□□□□□□□] 10%  Volume: ■■■■■□□□
•·.·''·.· .·:*¨¨*:·. ¸,ø¤º°`°º¤ø,¸ (¯`·.¸¸.·´¯`·.¸¸.-> text <-.¸¸.·´¯`·.¸¸.·´¯)  
..••°°°°••..°°••....••°° ¸¸.•*¨*•♫♪ ¸„.-•~¹°"ˆ˜¨ Hello ¨˜ˆ"°¹~•-.„¸
¨ … ‘ ’ „ ¸ ` ' Ꞌ ´ ^ ꞊ ꞈ ꞁ │| ¦ ¯ ¬ _ ‐ ▬ ⁃ ‒ ― ─ ═ ≡ Ξ  ̿   ̿ ͇   ⌠ ⌡ »»------(¯` ´¯)------»»
║ ╔ ╒ ╕ ╓ ╖ ╔ ╗ ╘ ╛ ╙ ╜ ╚ ╝ ╞ ╡ ╟ ╢ ╠ ╣ ║ ╬ ╥ ╨ ╧ ╤ ╦ ╩ ╪ ╫ ╬ ├ ┤ | │ ┼ ┘┌ ┐└ ─ ┴ ┬ ⱶ Ⱶ ˩ ˥ 
┬┴┬┴┬┴ ╤╧╤╧╤╧ ─┬┴─┬┴ ╔╝╔╝╔╝ ▄▀▄▀▄▀  █ ▌ ▐  ░▒▓█▓▒░ ░▒▓█ █▓▒░ ░ ◙■◙ ░ ▒ ▓  ₪₪₪₪ 
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