
try:
    import re
    import os
    import time
    import json
    import g4f
    import keyboard
    import pyautogui
    import pyperclip
    import ctypes
except ImportError as e:
    missing_module = str(e).split(' ')[-1].replace("'", "")
    import subprocess
    subprocess.call(['pip', 'install', '--upgrade', missing_module])
    import re
    import os
    import time
    import json
    import g4f
    import keyboard
    import pyautogui
    import pyperclip
    import ctypes

""""""
from setup_config_apps import create_shortcut
app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]
app_title.resizeTo(836, 144)
app_title.moveTo(-8, 119)
for i in range(20):
    app_title.moveRel(0, 10)
    time.sleep(0.005)

"""
gpt_35_turbo_16k_0613
gpt_4
gpt_4_32k_0613
gpt_4_turbo
"""
neyro_model = "gpt_35_turbo_16k_0613"

# model=g4f.models.gpt_4_turbo

# вызов нейро чата
def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=getattr(g4f.models, neyro_model),
        # model=g4f.models.gpt_35_long,
        # provider=g4f.Provider.GPTalk,  # FakeGpt GPTalk
        messages=messages)
    return response

# Проверка наличия файлов и создание при необходимости
def txt_create(text):
    if not os.path.exists(text):
        with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file_prompt_gpt_action:
            file_prompt_gpt_action.write("")

# Функция проверки того, пуст ли файл
def is_file_empty(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_e:
            return not bool(file_e.read().strip())
    except FileNotFoundError:
        return True

txt_create('prompt_gpt_action.txt')
txt_create('gpt_role.txt')

with open('gpt_role.txt', 'r', encoding='utf-8') as file:
    default_role = file.read()
role_message = [{"role": "system", "content": default_role}]

if is_file_empty('prompt_gpt_action.txt'):
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file:
        json.dump(role_message, file, ensure_ascii=False, indent=4)

with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
first_object = data[0]["content"]

role_message = [{"role": "system", "content": first_object}]


with open("prompt_gpt_action.txt", "w", encoding='utf-8') as file:
    file.truncate()

if not os.path.exists("gpt_code.py"):
    with open("gpt_code.py", "w", encoding='utf-8'):
        pass


def print_text_by_character(text):
    for char in text:
        print(char)

x = 7
print(f"""\
роль: {first_object}
╔{"═" * (x + len(neyro_model))}╗
║ G4F: {neyro_model}{" " * (x - len(neyro_model))} ║
╚{"═" * (x + len(neyro_model))}╝\
""")

# Сохранение сообщений в файл
def save_messages(messages):
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file_s:
        json.dump(messages, file_s, ensure_ascii=False, indent=4)


# Загрузка сообщений из файла
def load_messages():
    try:
        with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file_l:
            messages = json.load(file_l)  # messages для нейро чата
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []
    return messages


save_messages(role_message)


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)


if __name__ == "__main__":
    try:
        if is_file_empty('G4f_action.txt'):
            exit()
        with open('G4f_action.txt', 'r', encoding='utf-8') as file:
            data = file.read()
        printt(data + "\n")
        print("˅" * len(data))
        prompt_gpt_action = load_messages()
        prompt_gpt_action.append({"role": "user", "content": data})
        responses = ask_gpt(prompt_gpt_action)
        prompt_gpt_action.append({"role": "assistant", "content": responses})
        save_messages(prompt_gpt_action)
        response_code = responses
        # first_line = response_code.split('\n')[0]
        printt("(√¬_¬)ԅ⌐╦╦═─‒=═≡Ξ gpt_code.py                     !")
        print(response_code)
        pattern = r'```python\n(.*?)```'
        matches = re.findall(pattern, response_code, re.IGNORECASE | re.DOTALL)
        match = '\n'.join(matches)
        # Find start and end indices of the match
        start_index = response_code.index(matches[0])
        end_index = response_code.index(matches[-1]) + len(matches[-1])
        # Extracting content before and after the pattern
        before_pattern = response_code[:start_index]
        after_pattern = response_code[end_index:]
        app_title.minimize()
        app_title.restore()
        content_code = f'"""\n{before_pattern.strip()}\n"""\n\n{match}\n\n"""\n{after_pattern.strip()}\n"""' + "\n" + 'input()'
        with open('gpt_code.py', 'w', encoding='utf-8') as file:
            file.write(content_code)
            time.sleep(0.1)
        os.startfile("gpt_code.py")

    except Exception as e:
        print(e)
        input()
        os.startfile(f"{app_title_window}")
        exit()
