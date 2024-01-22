import os
import pyautogui
import win32com

path_to_shortcut = "ярлыки\\"  # папка ярлыков
ideas = path_to_shortcut + "идеи.txt"
reminder = path_to_shortcut + "напоминалка.txt"
models_directory = "voskmodels"
dir_path = r"E:\Muzic"  # ! путь для проигрывания музыки
current_folder = os.path.dirname(os.path.abspath(__file__))
requirements_path = os.path.join(current_folder, "requirements.txt")  # ! для команд библиотек

model1 = r"voskmodels\vosk-model-small-ru-0.22"
model2 = r"voskmodels\vosk-model-small-en-us-0.15"
model3 = r"voskmodels\vosk-model-ru-0.42"
model4 = r"voskmodels\vosk-model-en-us-0.22"

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
    shortcut_if_create = None
    try:
        shortcut_if_create = pyautogui.getWindowsWithTitle(shortcut_name)[0]
        shortcut_if_create.moveTo(88, 220)
        shortcut_if_create.resizeTo(849, 327)
    except Exception as e:
        print(
            f"\r                                                   (!o_O) ярлык --> {shortcut_name}\r")
        script_path = target_script_path
        script_directory = os.path.dirname(script_path)
        shortcut_name_link_path = os.path.join(script_directory, path_to_shortcut + shortcut_name + ".lnk")
        if not os.path.isfile(shortcut_name_link_path):
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_name_link_path)
            shortcut.TargetPath = script_path
            shortcut.Description = shortcut_name
            shortcut.WorkingDirectory = script_directory
            shortcut.Save()
        print(e)
        os.startfile(path_to_shortcut + shortcut_name)
        exit()
