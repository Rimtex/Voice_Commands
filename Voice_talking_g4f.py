import os
import keyboard
import pyaudio
import g4f
import time
import pygetwindow
import win32com.client as wincl
from colorama import Fore, Style, init
from vosk import Model, KaldiRecognizer
from setup_config import create_shortcut, model1

LYE = Fore.LIGHTYELLOW_EX
LCY = Fore.LIGHTCYAN_EX
LGR = Fore.LIGHTGREEN_EX
SRA = Style.RESET_ALL
init(convert=True)

create_shortcut("болтать", os.path.abspath(__file__))
app_title = pygetwindow.getWindowsWithTitle("болтать")[0]
app_title.moveTo(-8, 319)
app_title.resizeTo(836, 210)

# Старт модели определеия голоса
voice_model = model1
current_model = Model(voice_model)
rec = KaldiRecognizer(current_model, 48000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    frames_per_buffer=4000
)
stream.start_stream()

# Определение функции, которая будет озвучивать текст
speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()
for voice in voices:
    if voice.GetAttribute("Name") == "Microsoft Pavel Mobile":
        speak.Volume = 100  # громкость
        speak.Rate = 4  # скорость
        speak.Voice = voice

# вызов нейро чата
neyro_model = "gpt_35_turbo_16k_0613"


def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=getattr(g4f.models, neyro_model),
        messages=messages)
    print(LYE + response)
    speak.speak(response)
    return response


messagesgpt = []

try:
    if __name__ == "__main__":
        print(
            f"""\
    ╔{"═" * len(voice_model)}══╤════════════╗
    ║ {LGR}{voice_model}{SRA} │{LCY} загружена!{SRA} ║
    ║{" " * (len(voice_model) - len(neyro_model))} {LYE}{neyro_model}{SRA} │{LCY} загружена!{SRA} ║
    ╚{"═" * len(voice_model)}══╧════════════╝
    ╔═════════════════════════════════════╤════════════════════╗
    ║ для сброса чата                     │{LCY} Ctrl - Shift{SRA}       ║
    ║ зажмите одну из клавиш для пропуска │{LCY}▾Ctrl▾ ▾Shift▾ ▾alt▾{SRA}║
    ╚═════════════════════════════════════╧════════════════════╝\
    """
        )
        while True:
            start_time = time.time()
            print(LCY + " начало чата: ")
            while True:
                if rec.AcceptWaveform(stream.read(4000)):
                    prompt = rec.Result()[13:-2]
                    if (
                            keyboard.is_pressed("ctrl")
                            or keyboard.is_pressed("shift")
                            or keyboard.is_pressed("alt")
                    ):
                        prompt = '""'
                    if prompt != '""':
                        promptgpt = prompt[1:-1]
                        print(LGR + promptgpt)
                        messagesgpt.append({"role": "User", "content": promptgpt})
                        messagesgpt.append({"role": "assistant", "content": ask_gpt(messages=messagesgpt)})
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("shift"):
                    messagesgpt = None
                    prompt = '""'
                    break

                elapsed_time = time.time() - start_time
                if elapsed_time >= 30:
                    input("Пауза! Нажмите Enter, чтобы продолжить...")
                    break
except Exception as e:                
            print(e)
            input()