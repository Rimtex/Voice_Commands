import time
import traceback

from Voice_Commands import stream, rec, speak, speak_tts
from colorama import init, Fore, Style
from loader import download_generator
from model_prompts import req_rand_question, req_rand_comedy, req_rand_Lyrics, req_rand_facts, req_rand_medicine, \
    req_rand_history
from python_translator import Translator

"""
from pygpt4all import GPT4All_J

model = GPT4All_J('./models/ggml-gpt4all-j-v1.3-groovy.bin')
"""
model_name = "ggml-gpt4all-l13b-snoozy.bin"

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


def generate_response(user_input_gener):
    response_gener = model.generate(user_input_gener)
    responses = ""
    for r in response_gener:
        print(f"{r}", end='', flush=True)
        responses += r
    return responses


def print_trans_response():
    print(YEL + f" > {request_prompts} > " + SRA)
    print(CYA + model_name + LCY)
    responsegpt = generate_response(request_prompts)
    transgpt = translator.translate(responsegpt, "russian", "english")
    trans_fullgpt = str(transgpt)
    print(LGR + f"\n {trans_fullgpt}")
    speak_tts(f" {trans_fullgpt}")


"""
    for token in response_gener:
        print(f"{token}", end='', flush=True)
    """

if __name__ == '__main__':
    from pygpt4all import GPT4All

    model = GPT4All('./models/ggml-gpt4all-l13b-snoozy.bin')
    translator = Translator()
    speak.Rate = 4
    while True:
        download_generator()
        full_sentence = ""
        while True:
            if rec.AcceptWaveform(stream.read(4000)):
                try:
                    prompt = rec.Result()[13:-2]
                    words = prompt[1:-1].split()
                    part_prompt = prompt[1:-1]
                    full_sentence += part_prompt + " "
                    # print(full_sentence)
                    if prompt in ('"поговорим"', '"переводчик"', '"закройся"', '"с свали"', '"свали"'):
                        exit()
                    elif len(words) > 0 and \
                            words[-1] in (
                            'ответ', 'ответь', 'отвечай', 'хватит', 'переведи', 'переводи',
                            'перевод', 'давай', 'ладно', 'слышала', 'слышал', 'понял',
                            'поняла', 'дальше', 'стоп', 'продолжай', 'продолжи',
                    ):
                        full_sentence = full_sentence.rsplit(words[-1], 1)[0]  # Удалите последнее слово
                        print(f'{LGR} >>>{WHI}')
                        trans = translator.translate(full_sentence, "english", "russian")  # print(full_sentence)
                        request_prompts = str(trans)
                        print_trans_response()
                        time.sleep(2.5)
                        speak_tts("согласен!")  # триггер для ассистента
                        time.sleep(.5)
                        break
                    elif prompt in ('"заново"', '"снова"', '"сначала"', '"сброс"', '"сбросить"'):
                        print(f' {LRE}X{SRA}\n', end='')
                        break

                    elif prompt in ('"запрос"', '"вопрос"'):
                        request_prompts = req_rand_question()
                        print_trans_response()
                        break

                    elif prompt in ('"история"', '"истории"'):
                        request_prompts = req_rand_history()
                        print_trans_response()
                        break
                    elif prompt in ('"медицина"', '"медицины"'):
                        request_prompts = req_rand_medicine()
                        print_trans_response()
                        break
                    elif prompt in ('"комедия"', '"комедии"'):
                        request_prompts = req_rand_comedy()
                        print_trans_response()
                        break
                    elif prompt in ('"лирика"', '"лирикой"'):
                        request_prompts = req_rand_Lyrics()
                        print_trans_response()
                        break
                    elif prompt in ('"факты"', '"факт"'):
                        request_prompts = req_rand_facts()
                        print_trans_response()
                        break

                    elif prompt != '""':  # !
                        print(f' {LYE}{part_prompt}{SRA} ', end='')

                except Exception as e:
                    print(LRE)
                    print(traceback.format_exc())
                    print(full_sentence)
                    print(f"{LRE} переводчик :{SRA}", e)
