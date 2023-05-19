import random
import time

import keyboard
from colorama import Fore, init, Style, Back

colors = [Fore.GREEN, Fore.YELLOW, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX]

init(convert=True)


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)


#  boot loader screen saver
def loader_screen_rimtex():
    message = [(Fore.CYAN, " ᴙimtex "), (Fore.YELLOW, "Voice "), (Fore.GREEN, "Assistant "), (Fore.WHITE, "Commands")]
    for color, word in message:
        for char in word:
            print(color + char, end='', flush=True)
            time.sleep(0.01)


#  прощание
def download_bye():
    load_square = (f"""
\b\b\b\b\b\b\bBye!
 ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
  ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
   ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
    ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
     ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
      ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
       ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
        ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
         ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
          ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
           ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
            ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
           ʕ/·ᴥ·ʔ/\b\b\b\b\b\b\b
""")
    losq = load_square.strip().split('\n')
    for char in losq:
        print(char, end='', flush=True)
        time.sleep(.02)


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
[■■■■■■■■■■]\b\b\b\b\b\b\b\b\b\b\b\b
 >          \b\b\b\b\b\b\b\b\b
""")
    losq = load_square.strip().split('\n')
    for char in losq:
        print(char, end='', flush=True)
        time.sleep(.05)


def down_generator():
    word = (f"""\
¸,ø*¤º°¨`¨°º¤*ø,¸
¸,.·•°´ˆ¯ˆ`°•·.,¸
¸„.-•~¹°"ˆ˜¨¨˜ˆ"°¹~•-.„¸
""")
    lines = word.strip().split('\n')
    random_line = random.choice(lines)
    while True:
        for char in random_line:
            print(char, end='', flush=True)
            time.sleep(.05)
            if keyboard.is_pressed('space'):
                break


#: генератор стенки
def waal_generator():
    build = """
╠╬╣╚╩╝╔╦╗║══
╟╫╢╙╨╜╓╥╖║──
╞╪╡╘╧╛╒╤╕│══
├┼┤└┴┘┌┬┐│──
╠╬╣╚╩╝╔╦╗║══╟╫╢╙╨╜╓╥╖║──╞╪╡╘╧╛╒╤╕│══├┼┤└┴┘┌┬┐│──
"""
    lines = build.strip().split('\n')
    random_line = random.choice(lines)
    print(random.choice(colors), end='')
    while True:
        if keyboard.is_pressed('space'):
            break
        print(random.choice(random_line), end='', flush=True)
        time.sleep(.1)


#: генератор бреда
def letters_random():
    build = """
ц        укенгшщзхфывапролджэячсмитбюё
q        wertyuiopasdfghjklzxcvbnm
ц        укенгшщзхфывапролджэячсмитбюёq        wertyuiopasdfghjklzxcvbnm
$        ¥£€¢±‰÷≠=*·+-/¹²³☺▪▫°♠♣♥♦↔↕≤≥♀♂‼^_
$        ¥£€¢±‰÷≠=*·+-/¹²³☺▪▫°♠♣♥♦↔↕≤≥♀♂‼^_ц        укенгшщзхфывапролджэячсмитбюёq        wertyuiopasdfghjklzxcvbnm
"""

    """
    ._. - смайл скучать
    -_- - смайл печаль
    ¬_¬ - смайл закрытые глаза 
    O_O - смайл круглые глаза
"""

    lines = build.strip().split('\n')
    random_line = random.choice(lines)
    while True:
        if keyboard.is_pressed('space'):
            break
        colored_character = random.choice(colors) + random.choice(random_line)
        print(colored_character, end='')
        time.sleep(.1)


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


#  ген_ератор смайлов 2
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


#  генератор загрузок 2
def download_gen_erator():
    load_square = (f"""\
[□□□□□□□□□□]
[■□□□□□□□□□]
[■■□□□□□□□□]
[■■■□□□□□□□]
[■■■■□□□□□□]
[■■■■■□□□□□]
[■■■■■■□□□□]
[■■■■■■■□□□]
[■■■■■■■■□□]
[■■■■■■■■■□]
[■■■■■■■■■■]
""")
    losq = load_square.strip().split('\n')
    for char in losq:
        for i in char:
            print(i, end='', sep="")
            time.sleep(.12)
        print("\r", end='')
        time.sleep(.12)


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
