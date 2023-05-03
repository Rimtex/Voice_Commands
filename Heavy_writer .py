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

# Инициализация аудиопотока
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    frames_per_buffer=4000
)
stream.start_stream()
print(Fore.LIGHTGREEN_EX + model2)
while True:
    if rec.AcceptWaveform(stream.read(4000)):
        prompt = rec.Result()[13:-2]
        words = prompt[1:-1].split()
        print(Fore.LIGHTYELLOW_EX + prompt[1:-1], sep=" ", end="")
        #: Запись в курсор # для записи фраз или слов: нажимаем Num Lock и - диктуем
        # Проверить, включена ли клавиша Num Lock
        num_lock_state = win32api.GetKeyState(0x90)  # 0x90 - код клавиши Num Lock
        if num_lock_state == 1 or num_lock_state == -127:  # Если клавиша включена
            if prompt != '""':  # не выключается при тишине
                keyboard.write(prompt[1:-1])  # пишем до конца цикла
                # Нажать клавишу Num Lock, чтобы выключить её
                win32api.keybd_event(0x90, 0x45, 0x1, 0)
                win32api.keybd_event(0x90, 0x45, 0x3, 0)
