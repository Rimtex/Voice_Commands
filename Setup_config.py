path_to_shortcut = "ярлыки\\"  # папка ярлыков
ideas = path_to_shortcut + "идеи.txt"  # путь для работы команд с текстовым файлом 1
reminder = path_to_shortcut + "напоминалка.txt"  # 2
models_directory = "voskmodels"
dir_path = r"E:\Muzic"  # ! путь для проигрывания музыки
requirements_path = "F:\\Rimtex\\Projects\\Voice_Commands.py\\requirements.txt"  # ! для команд библиотек
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
