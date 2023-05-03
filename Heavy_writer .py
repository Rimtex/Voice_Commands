import keyboard
from colorama import Fore, init
import pyaudio
import win32api
from address_config import model2
from vosk import Model, KaldiRecognizer

init(convert=True)

# Инициализация распознавателя с начальной моделью
current_model = Model(model2)
rec = KaldiRecognizer(current_model, 48000)

# Инициализация аудио потока
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    frames_per_buffer=4000
)
stream.start_stream()

print(Fore.LIGHTGREEN_EX + model2 + Fore.LIGHTCYAN_EX + " загружена!")

while True:
    #  if keyboard.is_pressed('CapsLock'):  # Проверка нажатия клавиши
    #  print(Fore.LIGHTCYAN_EX + " CapsLock ", end="")
    #  print("\b\b\b\b\b\b\b\b\b\b", end="")
    if rec.AcceptWaveform(stream.read(4000)):
        prompt = rec.Result()[13:-2]
        words = prompt[1:-1].split()
        #: Запись в курсор # для записи фраз или слов: нажимаем Num Lock и - диктуем
        # Проверить, включена ли клавиша Num Lock
        num_lock_state_check = win32api.GetKeyState(0x90)  # 0x90 - код клавиши Num Lock
        caps_lock_state_check = win32api.GetKeyState(0x14)  # 0x14 - код клавиши Caps Lock
        # Если клавиша Num Lock включена
        if (num_lock_state_check == 1 or num_lock_state_check == -127) and \
                (caps_lock_state_check != 1 and caps_lock_state_check != -127):  # и выключен Caps Lock
            if prompt != '""':  # если не тишина
                print(Fore.LIGHTYELLOW_EX + prompt[1:-1], sep=" ", end=" ")
                keyboard.write(prompt[1:-1])  # пишем
            # elif prompt == '""':  # если тишина
            #     # Нажать клавишу Num Lock, чтобы выключить её
            #     win32api.keybd_event(0x90, 0x45, 0x1, 0)
            #     win32api.keybd_event(0x90, 0x45, 0x3, 0)
