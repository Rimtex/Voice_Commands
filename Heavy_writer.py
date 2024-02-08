import os
import keyboard
import pyaudio
import pygetwindow
from colorama import Fore, init
from vosk import Model, KaldiRecognizer
from setup_config import create_shortcut, model1, model2, model3, model4

init(convert=True)

create_shortcut("писатель", os.path.abspath(__file__))
app_title = pygetwindow.getWindowsWithTitle("писатель")[0]
app_title.moveTo(-8, 319)
app_title.resizeTo(836, 185)

model_glob = model3
current_model = Model(model_glob)
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

if __name__ == '__main__':
    print(f"""\
╔{"═" * len(model_glob)}══╤════════════╗
║ {Fore.LIGHTGREEN_EX}{model_glob}{Fore.RESET} │{Fore.LIGHTCYAN_EX} загружена!{Fore.RESET} ║
╚{"═" * len(model_glob)}══╧════════════╝
╔═════════════════════════════════════╤════════════════════╗
║ для записи нажмите здесь ввод       │{Fore.LIGHTCYAN_EX} Enter{Fore.RESET}              ║
║ для остановки                       │{Fore.LIGHTCYAN_EX} Ctrl - Shift{Fore.RESET}       ║
║ зажмите одну из клавиш для пропуска │{Fore.LIGHTCYAN_EX}▾Ctrl▾ ▾Shift▾ ▾alt▾{Fore.RESET}║
╚═════════════════════════════════════╧════════════════════╝\
""")
    while True:
        input(Fore.LIGHTGREEN_EX + " нажмите Enter")
        print(Fore.LIGHTCYAN_EX + " запись голоса:")
        while True:
            if rec.AcceptWaveform(stream.read(4000)):
                prompt = rec.Result()[13:-2]
                if keyboard.is_pressed("ctrl") or keyboard.is_pressed("shift") or keyboard.is_pressed("alt"):
                    prompt = '""'
                if prompt != '""':
                    keyboard.write(prompt[1:-1] + " ")
            if keyboard.is_pressed("ctrl") and keyboard.is_pressed("shift"):
                prompt = '""'
                break
