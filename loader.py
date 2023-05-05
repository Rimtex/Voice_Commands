import random
import time

import keyboard
from colorama import Fore, Style, init, Back

colors = [Fore.GREEN, Fore.YELLOW,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX]

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

init(convert=True)


#  boot loader screen saver
def loader_screen_rimtex():
    message = [(CYA, " ᴙimtex "), (YEL, "Voice "), (GRE, "Assistant "), (WHI, "Commands")]
    for color, word in message:
        for char in word:
            print(color + char, end='', flush=True)
            time.sleep(0.01)


#  генератор загрузок
def download_generator():
    load_square = (f"""
{Fore.LIGHTCYAN_EX}
[□□□□□□□□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■□□□□□□□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■□□□□□□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■□□□□□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■■□□□□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■■■□□□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■■■■□□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■■■■■□□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■■■■■■□□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■■■■■■■□]\b\b\b\b\b\b\b\b\b\b\b\b
[■■■■■■■■■■]
""")
    losq = load_square.strip().split('\n')
    for char in losq:
        print(char, end='', flush=True)
        time.sleep(.05)


def down_generator():
    word = (f"""\
(¯`·.¸¸.·´¯`·.¸¸.->\
¸.·´¯¯`·.¸\
..••°°°°••..\
¸„.-•~¹°'ˆ˜¨\
{random.choice(colors)}\
random.choice(colors)\
{random.choice(colors)}\
¨˜ˆ'°¹~•-.„¸\
¸,ø¤º°`°º¤ø,¸\
<-.¸¸.·´¯`·.¸¸.·´¯)
""")
    lines = word.strip().split('\n')
    for char in word:
        print(char, end='', flush=True)
        time.sleep(0.05)
    for char in random.choice(lines):
        print(random.choice(colors) + char, end='', flush=True)
        time.sleep(0.05)


#: генератор стенки
def waal_generator():
    from Voice_Commands import stream, rec
    build = """
╠╬╣╚╝╔╗╦═╩║═╠╬╣╚╝╔╗╦═╩═╠╬╣╚╝╔╗╦═╩═╠╬╣╚╝╔╗╦═╩═╚╝╔╗╚╝╔╗╚╝╔╗╚╝╔╗═
╟╫╢╙╜╓╖╥─╨║─╟╫╢╙╜╓╖╥─╨─╟╫╢╙╜╓╖╥─╨─╟╫╢╙╜╓╖╥─╨─╙╜╓╖╙╜╓╖╙╜╓╖╙╜╓╖─
╞╪╡╘╛╒╕╤═╧│═╞╪╡╘╛╒╕╤═╧═╞╪╡╘╛╒╕╤═╧═╞╪╡╘╛╒╕╤═╧═╘╛╒╕╘╛╒╕╘╛╒╕╘╛╒╕═
├┼┤└┘┌┐┬─┴│─├┼┤└┘┌┐┬─┴─├┼┤└┘┌┐┬─┴─├┼┤└┘┌┐┬─┴─└┘┌┐└┘┌┐└┘┌┐└┘┌┐─
"""
    lines = build.strip().split('\n')
    random_line = random.choice(lines)
    #  iterations = len(prompt[1:-1])  # 5555  # Число повторений ! !! надо сделать если больше ноля то прерываеца
    print(random.choice(colors), end="")
    while True:
        if rec.AcceptWaveform(stream.read(4000)):
            prompt = rec.Result()
            prompt = prompt[13:-2]
            if keyboard.is_pressed('space'):
                break
            elif prompt != '""':
                break
        random_color = random.choice(colors)
        # for _ in range(iterations):
        random_character = random.choice(random_line)
        colored_character = random_character
        print(colored_character, end='', flush=True)
        time.sleep(.05)


#: генератор буквы
def letters_random():
    from Voice_Commands import stream, rec
    build = """
ц        укенгшщзхфывапролджэячсмитбюё
q        wertyuiopasdfghjklzxcvbnm
ц        укенгшщзхфывапролджэячсмитбюёq        wertyuiopasdfghjklzxcvbnm
$        ¥£€¢±‰÷≠=*·+-/¹²³☺▪▫°♠♣♥♦↔↕≤≥♀♂‼^_
"""
    """
    
    ._. - смайл скучать
    -_- - смайл печаль
    ¬_¬ - смайл закрытые глаза 
    O_O - смайл круглые глаза
    
"""
    lines = build.strip().split('\n')
    random_line = random.choice(lines)
    #  iterations = len(prompt[1:-1])  # 5555  # Число повторений ! !! надо сделать если больше ноля то прерываеца
    while True:
        if rec.AcceptWaveform(stream.read(4000)):
            prompt = rec.Result()
            prompt = prompt[13:-2]
            if keyboard.is_pressed('space'):
                break
            elif prompt != '""':
                break

        # for _ in range(iterations):
        random_color = random.choice(colors)
        random_character = random.choice(colors) + random.choice(random_line)
        colored_character = random_character
        print(colored_character, end='')
        time.sleep(.05)


#  генератор смайлов
def smile_generator():
    edges = {'[': ']', '{': '}', '(': ')', 'ʕ': 'ʔ'}
    edgel = random.choice("[{(ʕ")
    edger = edges[edgel]
    edlesl = "¨’‘´'͡‾ˁ˶"
    eyes = "→←·•●◦°*○☼¤◌҉oOǒΘʘ×óòȌ→^˘▪■¬⌐-"
    centr = random.choice("ᴥᴗ_˽ꞈ.")
    print(f"""{random.choice(colors)}\
{edgel}{random.choice(colors)}\
{random.choice(edlesl)}{random.choice(colors)}\
{random.choice(eyes)}{random.choice(colors)}\
{centr}{random.choice(colors)}\
{random.choice(eyes)}{random.choice(colors)}\
{random.choice(edlesl)}{random.choice(colors)}\
{edger}""", end='')


#  генератор смайлов 2
def smile_gen_erator():
    col1 = random.choice(colors)
    col2 = random.choice(colors)
    col3 = random.choice(colors)
    edges = {'[': ']', '{': '}', '(': ')', 'ʕ': 'ʔ'}
    edgel = random.choice("[{(ʕ")
    edger = edges[edgel]
    edless = {'¨': '¨', '’': '’', '‘': '‘', '´': '´', '͡': '͡', '‾': '‾', 'ˁ': 'ˀ', '˶': '˶', "'": "'"}
    edlesl = random.choice("¨’‘´'͡‾ˁ˶")
    edlesr = edless[edlesl]
    eyes = random.choice("→←·•●◦°*○☼¤◌҉oOǒΘʘ×óòȌ→^˘▪■¬⌐-")
    centr = random.choice("ᴥᴗ_˽ꞈ.")
    print(f"""{col1}\
{edgel}{col2}\
{edlesl}{col3}\
{eyes}{random.choice(colors)}\
{centr}{col3}\
{eyes}{col2}\
{edlesr}{col1}\
{edger}\
""", end='')


#  удалитель дублирующихся символов
def duplicate_character_remover():
    s = """
ᵏᵐᵑᵒᵓᵖʳʴᵗʵᶰᵡᶛᶜᶠᶧᶨᶩᶪᶫᵘᵙᵛᵚᵞᵟᵠᶝᶞᶟᶡᶢᶣᶤᶥᶦᴽᶬᶭᶮᶯᶱᶲᶳᶴᶵᶶᶷᶹᶺᶻᶼᶽᶾᶿᴬᴭᵃᵄᵅᵆᵇᵈᵉᵊᵋᵌᵍᵎᵝⁱ™ᴹᴿ°ᴮᴼˢᴾᴴᴰªᵜᵔᵕƐω³͡˵ʱ₎⁾ˁˀԅʰ͙ˡ⓿❶❷❸❹❺❻❼❽❾❿⁰¹²⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉⓪①②
③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳½⅓¼⅕⅙⅛⅔⅖¾⅗⅜⅘⅚⅝⅞⅍℅©®℗◊π∞Σ∑♯ø≠∏₩∂∟∙√∩∫☺☻∆≈◄▲▼►◂▴▾▸˂˄˅˃←↑→↓♪♫ϟ♠♣♥♦·•●◦*○☼¤◌҉◙■▪▀▄▬▫□
█▌▐↔↕♀♂‼«»‹›/\⁄|ᴕ꜠꜡ǁᴱᵀᵁᴺˣᴳᵂᴸᴵᴯɢɴⁿ⌐═╤╦─̷ι>ʕ̫ʔ͓-‾ᴥᴗȌʅʃ╘[´`]╕ʘ̅ꞈ()^×_¬˽˘Ɔ{˶}"cε'˛┌п┐.¯└з―ŏ=O̪главныйQ’̀oˇòóԾ!‗Θǒ͜οˊˋ~:¨₊˚Lᵧₒᵤ├╓╖┤
10%Vlume¸,ºtx<„ˆ˜H…‘Ꞌ꞊ꞁ│¦‐⁃‒≡Ξ͇̿⌠⌡║╔╒╗╛╙╜╚╝╞╡╟╢╠╣╬╥╨╧╩╪╫┼┘┴┬ⱶⱵ˩˥░▒▓₪+abrsF4Ϟỽℓß‽яiтмByſ₰₯₧ƒОшибк2αÁáÀàÅåÄäÆæÇçÉéÈèÊêÍíÌì
ÎîÑñÓÒÔôÖöØÚúÙùÜüŽž₳฿âãðëïõþ‡ĂăǕǖÐΩᶀᶁᶂᶃᶄᶆᶇᶈᶉᶊᶋᶌᶍᶎᶏᶐᶑᶒᶓᶔᶕᶖᶗᶘᶙᶚᶸᵯᵰᵴᵶᵹᵼᵽᵾᵿ¶¥£RAnCdƦīⱮƫⱸẊȏἱͼÂṡṣἳẠạẢảḀḁÃǍǎẤấẦầẨẩȂȃẪẫẬậẮắẰằẲẳẴẵẶ
ặĀāĄąǞȀȁǺǻǟǠǡẚȦȧȺÅⱥǼǢǣⱯḂḃḄḅḆḇƁɃƀƃƂƄƅḈḉĆćĈĉĊċČčƇƈȻȼDḊḋḌḍḎḏḐḑḒḓĎďƊƋƌƉĐđȡEḔḕḖḗḘḙḚḛḜḝẸẹẺẻẾếẼẽỀềỂểỄễỆệĒēĔĕĖėĘęĚěËȄȅȨȩȆȇƎɆ
fḞḟƑℲⅎGgƓḠḡĜĝĞğĠġĢģǤǥǦǧǴǵhḢḣḤḥḦḧḨḩḪḫẖĤĥȞȟĦħⱧⱨǶIḬḭḮḯĲĳÏĨĩĪĬĭĮįıƗƚỺǏǐJjĴĵȷⱼɈɉǰKkḰḱḲḳḴḵĶķƘƙǨǩⱩⱪĸḶḷḸḹḺḻḼḽĹĺĻļĽİľĿŀŁłỈỊịȽⱠⱡⱢǇǈǉȉȈȊ
ȋMḾḿṀṁṂṃƩƜNṄṅṆṇṈṉṊṋŃńŅņŇňǸǹŊƝŉȠƞŋǊǋǌȵ№ṌṍṎṏṐṑṒṓȪȫȬȭȮȯȰȱǪǫǬǭỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợƠơŌōŎŐőÕǑȍȎŒœǾǽǿPpṔṕṖṗƤƥⱣǷqɊɋȹŔŕ
ŖŗŘřṘṙṚṛṜṝṞṟȐȑȒȓɍɌⱤSṠṢṤṥṦṧṨṩŚśŜŝŞşŠšȘșȿƧƨẞẛẜẝTṪṫṬṭṮṯṰṱŢţŤťŦŧƬƮẗȚȾƭțⱦȶUṲṳṴṵṶṷṸṹṺṻỤỦủỨỪụứỬửừữỮỰựŨũŪūŬŭŮůŰűǙǚǗǘǛǜŲųǓǔȔȕÛûȖȗƯɄ
ưƲƱvṼṽṾṿỼɅⱱⱴⱽWwẀẁẂẃẄẅẆẇẈẉŴŵẘⱲⱳXẋẌẍYẎẏỾỿẙỲỳỴỵỶỷỸỹŶŷƳƴŸÿÝýɎɏȲƔȳZzẐẑẒẓẔẕŹźŻżȤȥⱫⱬƵƶɀἀἁἂἃἄἅἆἇἈἉἊἋἌἍἎἏἐἑἒἓἔἕἘἙἚἛἜἝἠἡἢἣἤ
ἥἦἧἨἩἪἫἬἭἮἯἰἲἴἵἶἷἸἹἺἻἼἽἾἿὀὁὂὃὄὅὈὉὊὋὌὍὐὑὒὓὔὕὖὗὙὛὝὟὠὡὢὣὤὥὦὧὨὩὪὫὬὭὮὯὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗ
ᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴᾶᾷᾸᾹᾺΆᾼ᾽ι᾿῀῁ῂῃῄῆῇῈΈῊΉῌ῍῎῏ῐῑῒΐῖῗῘῙῚΊ῝῞῟ῠῡῢΰῤῥῦῧῨῩῪΎῬ῭΅`ῲῳῴῶῷῸΌῺΏῼ´῾ͰͱͲͳʹ͵Ͷͷͺͻͽ;΄΅
Ά·ΈΉΊΌΎΏΐΑΒΓΔΕΖΗΙΚΛΜΝΟΠΡΤΥΦΧΨΩΪΫάέήίΰβγδζηθκλμνξρςστυφχψϊϋόύώϐϑϒϓϔϕϖʌɑəɜɪɒɔʊ
    """
    new_s = '\n'.join(s.splitlines())
    result = ''
    for char in new_s:
        if char not in result or char == '':
            result += char
    print(result)
    input()
