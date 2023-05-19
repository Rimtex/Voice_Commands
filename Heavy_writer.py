import keyboard
import pyaudio
from colorama import Fore, init
from vosk import Model, KaldiRecognizer

init(convert=True)
"""
r"vosk-model-small-ru-0.22"
r"vosk-model-small-en-us-0.15"
r"vosk-model-ru-0.42"
r"vosk-model-en-us-0.22"
"""
rec = KaldiRecognizer(Model(r"vosk-model-ru-0.42"), 48000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    frames_per_buffer=4000
)
stream.start_stream()

print(f"""\
 ╔════════════════════╤════════════╗
 ║ {Fore.LIGHTGREEN_EX}vosk-model-ru-0.42{Fore.RESET} │{Fore.LIGHTCYAN_EX} загружена!{Fore.RESET} ║                    
 ╠════════════════════╧════════════╩═══╤════════════════════╗ 
 ║ для записи нажмите здесь ввод       │{Fore.LIGHTCYAN_EX} Enter{Fore.RESET}              ║
 ║ для остановки                       │{Fore.LIGHTCYAN_EX} Ctrl - Shift{Fore.RESET}       ║
 ║ зажмите одну из клавиш для пропуска │{Fore.LIGHTCYAN_EX}▾Ctrl▾ ▾Shift▾ ▾alt▾{Fore.RESET}║
 ╚═════════════════════════════════════╧════════════════════╝ 
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
