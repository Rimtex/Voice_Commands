import pyaudio
from vosk import KaldiRecognizer, Model

from colorama import init, Fore, Style

from Voice_Commands import stream

colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX,
          Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]
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


vosk_model = "vosk-model-small-en-us-0.15"  # 
try:
    rec = KaldiRecognizer(Model(rf"{vosk_model}"), 48000)
except Exception as e:
    print(f"{RED} !vosk-model! отсутствует:{SRA}\n", e)
    print(f"{LGR} https://alphacephei.com/vosk/models{SRA}")
    print(f"{LCY} установите модель и введите её название:{SRA}")
    vosk_model = input(" ")
    rec = KaldiRecognizer(Model(rf"{vosk_model}"), 48000)

if __name__ == '__main__':
    while True:
        if rec.AcceptWaveform(stream.read(4000)):
            try:
                prompt = rec.Result()
                words = prompt[14:-3].split()
                prompt = prompt[13:-2]
                if prompt in ('"english"', '"english of"', '"english off"', '"инглиш"'):
                    exit()
                elif prompt != '""':
                    try:
                        print(f' {GRE}{prompt[1:-1]}{SRA} ', end='')
                    except TypeError:
                        print(f"{WHI}_{SRA}", sep='', end='')
            except Exception as e:
                print(f"{RED} !1! :{SRA}", e)
