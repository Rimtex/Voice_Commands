import os
import traceback
import keyboard

from Voice_Commands import stream, rec, speak, speak_tts
from colorama import init, Fore, Style
from loader import download_generator
from python_translator import Translator
from model_prompts import req_rand_question, req_rand_comedy, req_rand_Lyrics, req_rand_facts, req_rand_medicine, \
    req_rand_history, req_rand_games

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

try:
    from pygpt4all import GPT4All_J
    from pyllamacpp.model import Model
except ImportError:
    print("Trying to Install required modules: pygpt4all pyllamacpp")
    os.system('pip install --upgrade pygpt4all pyllamacpp')
    from pygpt4all import GPT4All_J
    from pyllamacpp.model import Model

# Код ошибки 0xc0000005 проблемы с памятью.
"""
#: состав словаря из названий моделей
file_list = os.listdir("models\\")
bin_files = [f for f in file_list if f.endswith(".bin")]
labels = []  # словарь названий ярлыков
for bin_file in bin_files:
    full_path = os.path.join("models\\", bin_file)
    label = bin_file
    labels.append(label)
for i, label in enumerate(labels):
    print(f"{i + 1}. {label}")
"""
print("""
1. ggml-gpt4all-j-v1.3-groovy.bin
2. ggml-gpt4all-l13b-snoozy.bin
""")
model_name = None
num = input(" введите номер модели: ")

if num == '1':
    model_path = './models/ggml-gpt4all-j-v1.3-groovy.bin'
    model = GPT4All_J(model_path)
    model_name = os.path.basename(model_path)
elif num == '2':
    model_path = './models/ggml-gpt4all-l13b-snoozy.bin  '
    model = Model(model_path)
    model_name = os.path.basename(model_path)


def generate_response(user_input_gener):
    response_gener = model.generate(user_input_gener)
    responses = ""
    try:
        for res in response_gener:
            responses += res
            print(f"{res}", end='', flush=True)
        return responses
    except KeyboardInterrupt:
        return responses


def print_trans_response():
    try:
        print(GRE + " > " + YEL + f"{request_prompts}" + GRE + " > " + LCY)
        responsegpt = generate_response(request_prompts)
        transgpt = translator.translate(responsegpt, "russian", "english")
        trans_fullgpt = str(transgpt)
        print(LGR + f"\n{trans_fullgpt}")
        speak_tts(f" {trans_fullgpt}")
    except Exception as t:
        print(traceback.format_exc())
        print(f"{LRE} def print_trans_response() {SRA}", t)


print(f"""\
\r ╔════════════╤════════════════════════════════════════╤════════════════════════════════════╗
\r ║ model_name │ {CYA}{model_name} {SRA}        │     {LCY}ctrl + c{SRA}   для прерывания      ║
\r ╠════════════╧═════════════════════╤══════════════════╧════════════════════════════════════╣ 
\r ║ по-умолчанию > запись голоса > #:│{LYE} ответ | давай | понял | дальше {LRE}¦ стоп ¦ сброс {SRA}        ║
\r ║ голосовые команды            > #:│{YEL} запрос | история | медицина | комедия | лирика | факт {SRA}║
\r ║ для ввода с клавиатуры нажмите > │{LCY} shift {GRE}: пишем на английском {SRA}                          ║
\r ╚══════════════════════════════════╧═══════════════════════════════════════════════════════╝ 
""", sep='', end='')

if __name__ == '__main__':
    while True:
        try:
            translator = Translator()
            speak.Rate = 4
            download_generator()
            full_sentence = ""
            while True:
                if keyboard.is_pressed('shift'):  # если shift нажат
                    print(LRE + 'X' + GRE)
                    print(" >", end='')
                    request_prompts = input(" ввод с клавиатуры: ")
                    if request_prompts == '':
                        continue
                    print_trans_response()
                    break
                if rec.AcceptWaveform(stream.read(4000)):
                    prompt = rec.Result()[13:-2]
                    words = prompt[1:-1].split()
                    part_prompt = prompt[1:-1]
                    full_sentence += part_prompt + " "
                    # print(full_sentence)
                    try:
                        if prompt in ('"поговорим"', '"переводчик"', '"закройся"', '"с свали"', '"свали"'):
                            exit()
                        elif len(words) > 0 and words[-1] in ('ответ', 'давай', 'понял', 'дальше'):
                            print(LCY + "#: " + words[-1])
                            full_sentence = full_sentence.rsplit(words[-1], 1)[0]  # Удалите последнее слово
                            trans = translator.translate(full_sentence, "english", "russian")  # print(full_sentence)
                            request_prompts = str(trans)
                            print_trans_response()
                            # speak_tts("согласен!")  # триггер для ассистента
                            break
                        elif prompt in ('"стоп"', '"сброс"', '"заново"', '"снова"', '"сначала"', '"сбросить"'):
                            print(LCY + "#: " + words[-1])
                            print(LRE + 'X')
                            break
                        elif prompt in ('"запрос"', '"запрашиваю"'):
                            print(LCY + "#: " + words[-1])
                            request_prompts = req_rand_question()
                            print_trans_response()
                            break
                        elif prompt in ('"игра"', '"игры"'):
                            print(LCY + "#: " + words[-1])
                            request_prompts = req_rand_games()
                            print_trans_response()
                            break
                        elif prompt in ('"история"', '"истории"'):
                            print(LCY + "#: " + words[-1])
                            request_prompts = req_rand_history()
                            print_trans_response()
                            break
                        elif prompt in ('"медицина"', '"медицины"'):
                            print(LCY + "#: " + words[-1])
                            request_prompts = req_rand_medicine()
                            print_trans_response()
                            break
                        elif prompt in ('"комедия"', '"комедии"'):
                            print(LCY + "#: " + words[-1])
                            request_prompts = req_rand_comedy()
                            print_trans_response()
                            break
                        elif prompt in ('"лирика"', '"лирикой"'):
                            print(LCY + "#: " + words[-1])
                            request_prompts = req_rand_Lyrics()
                            print_trans_response()
                            break
                        elif prompt in ('"факт"', '"факты"'):
                            print(LCY + "#: " + words[-1])
                            request_prompts = req_rand_facts()
                            print_trans_response()
                            break

                        elif prompt != '""':  # !
                            print(f'{LYE}{part_prompt}{SRA} ', end='')

                    except Exception as e:
                        print(traceback.format_exc())
                        print(LRE, e)
                        print(full_sentence)
        except Exception as e:
            print(traceback.format_exc())
            print(LRE, e)
