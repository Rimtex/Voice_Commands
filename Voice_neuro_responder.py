import time

from googletrans import Translator
from Voice_Commands import stream, rec, speak, speak_tts
from colorama import init, Fore, Style
from pygpt4all.models.gpt4all import GPT4All

translator = Translator()

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

model = GPT4All('./gpt4all/pygpt4all/models/ggml-gpt4all-l13b-snoozy.bin')


def generate_response(user_input_gener):

    response_gener = model.generate(user_input_gener, n_predict=192)
    #   response = model.generate(user_input, n_predict=55, n_threads=8)
    return response_gener


if __name__ == '__main__':
    speak.Rate = 4
    while True:
        full_sentence = ""
        while True:
            if rec.AcceptWaveform(stream.read(4000)):
                try:
                    prompt = rec.Result()[13:-2]
                    words = prompt[1:-1].split()
                    transprompt = prompt[1:-1]
                    full_sentence += transprompt + " "
                    # print(full_sentence)
                    if prompt in ('"поговорим"', '"переводчик"', '"закройся"', '"с свали"', '"свали"'):
                        exit()
                    elif prompt != '""':  # !
                        print(f' {LYE}{transprompt}{SRA} ', end='')

                        if len(words) > 0 and \
                                any(word in prompt[1:-1]
                                    for word in ('ответ', 'ответь', 'отвечай', 'хватит', 'переведи', 'переводи',
                                                 'перевод', 'давай', 'вопрос', 'ладно', 'слышала', 'слышал', 'понял',
                                                 'поняла', 'дальше', 'стоп', 'запрос', 'продолжай', 'продолжи',
                                                 'согласен', 'согласись', 'запрос')):
                            # full_sentence = full_sentence.rsplit(words[-1], 1)[0]  # Удалите последнее слово
                            print(f'{LGR} >>>{WHI}')
                            # trans = translator.translate(vocabulary.random_response_aphorism(), dest="en")
                            trans = translator.translate(full_sentence, dest="en")  # print(full_sentence)
                            user_input = ' ! come up with funny aphorisms ! '  # дополнительная фраза
                            response = generate_response(trans.text + user_input)
                            gpt = translator.translate(response, dest="ru")
                            responegpt = gpt.text
                            print(LCY + f" ggml-gpt4all-l13b-snoozy: \n " + YEL + trans.text + GRE + user_input + SRA)
                            print(LCY + " ggml-gpt4all-l13b-snoozy: \n" + LGR + responegpt)
                            speak_tts(gpt.text)
                            time.sleep(2.5)
                            speak_tts("согласен!")
                            time.sleep(.5)
                            break
                    if prompt in ('"заново"', '"снова"', '"сначала"', '"сброс"', '"сбросить"'):
                        print(f' {LRE}X{SRA}\n', end='')
                        break
                except Exception as e:
                    print(full_sentence)
                    print(f"{LRE} переводчик :{SRA}", e)
