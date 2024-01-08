import os
import keyboard
import pyaudio
import pyautogui
import win32com
import win32com.client as wincl
from colorama import Fore, init
from vosk import Model, KaldiRecognizer

from Setup_config import path_to_shortcut, model3

Heavy_writer_window = "писатель"
if __name__ == '__main__':

    # Находим окно с именем 'писатель'
    Heavy_writer = None
    try:
        Heavy_writer = pyautogui.getWindowsWithTitle(Heavy_writer_window)[0]
        Heavy_writer.moveTo(88, 220)
        Heavy_writer.resizeTo(849, 327)
    except Exception as e:
        print(f"\r                                                   (!o_O) ярлык --> {Heavy_writer_window}\r")
        # Получить путь к текущему скрипту
        script_path = os.path.abspath(__file__)

        # Получить путь к папке, в которой находится скрипт
        script_directory = os.path.dirname(script_path)

        # Проверить наличие ярлыка писатель
        Heavy_writer_window_link_path = os.path.join(script_directory, path_to_shortcut + Heavy_writer_window + ".lnk")
        if not os.path.isfile(Heavy_writer_window_link_path):
            # Создать объект ярлыка
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(Heavy_writer_window_link_path)
            # Установить путь к исходному скрипту в ярлыке
            shortcut.TargetPath = script_path
            # Установить имя ярлыка
            shortcut.Description = Heavy_writer_window
            # Установить рабочую папку
            shortcut.WorkingDirectory = script_directory
            # Сохранить ярлык
            shortcut.Save()
        print(e)
        os.startfile(path_to_shortcut + Heavy_writer_window)
        exit()

    app_title = pyautogui.getWindowsWithTitle(Heavy_writer_window)[0]
    app_title.moveTo(-8, 319)
    app_title.resizeTo(836, 185)

    current_model = Model(model3)
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

    init(convert=True)

    print(f"""\
     ╔{"═" * len(model3)}══╤════════════╗
     ║ {Fore.LIGHTGREEN_EX}{model3}{Fore.RESET} │{Fore.LIGHTCYAN_EX} загружена!{Fore.RESET} ║                    
     ╚{"═" * len(model3)}══╧════════════╝   
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
