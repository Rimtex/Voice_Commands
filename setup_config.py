import os
import pygetwindow
import win32com
import win32com.client as wincl

path_to_shortcut = "ярлыки\\"  # папка ярлыков
ideas = path_to_shortcut + "идеи.txt"
reminder = path_to_shortcut + "напоминалка.txt"
models_directory = "vosk_models"
dir_path = r"E:\Muzic"  # ! путь для проигрывания музыки
current_folder = os.path.dirname(os.path.abspath(__file__))
requirements_path = os.path.join(current_folder, "requirements.txt")  # ! для команд библиотек

model1 = r"vosk_models\vosk-model-small-ru-0.22"
model2 = r"vosk_models\vosk-model-small-en-us-0.15"
model3 = r"vosk_models\vosk-model-ru-0.42"
model4 = r"vosk_models\vosk-model-en-us-0.22"


# группы команд
def command_groups(prompt, words):
    from keyboard_scripts import \
        key_symbols, open_music, scripts_others, \
        rimtex_colors, rimtex_pycharm, rimtex_personal, rimtex_reactions
    # - за комментировать которые не нужны
    key_symbols(prompt)
    open_music(prompt)
    scripts_others(words)
    rimtex_colors(prompt)
    rimtex_pycharm(prompt)
    rimtex_personal(prompt)
    rimtex_reactions(prompt, words)


# создание ярлыка + запуск с него
def create_shortcut(shortcut_name, target_script_path):
    try:
        shortcut_if_create = pygetwindow.getWindowsWithTitle(shortcut_name)[0]
        shortcut_if_create.moveTo(88, 220)
        shortcut_if_create.resizeTo(849, 327)
    except Exception as e:
        print(f"\r                                               (!o_O) ярлык --> {shortcut_name}\r")
        script_path = target_script_path
        script_directory = os.path.dirname(script_path)
        shortcut_name_link_path = os.path.join(script_directory, path_to_shortcut + shortcut_name + ".lnk")
        if not os.path.isfile(shortcut_name_link_path):
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_name_link_path)
            shortcut.TargetPath = "python.exe"
            shortcut.Arguments = script_path
            shortcut.Description = shortcut_name
            shortcut.WorkingDirectory = script_directory
            shortcut.Save()
        print(e)
        os.startfile(path_to_shortcut + shortcut_name)
        exit()

# пример использования
# create_shortcut("ассистент", os.path.abspath(__file__))   
"""
import pyautogui
from setup_config_apps import create_shortcut
app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]
"""

# Функция проверки присутствия файла
def is_file_empty(file_fullname):
    if not os.path.exists(file_fullname):
        with open(file_fullname, 'w', encoding='utf-8') as file:
            file.write("")
    try:
        with open(file_fullname, 'r', encoding='utf-8') as file:
            return not bool(file.read().strip())
    except FileNotFoundError:
        return True
    

