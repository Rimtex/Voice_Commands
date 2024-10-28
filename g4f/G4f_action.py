try:
    import re
    import os
    import time
    import json
    from g4f.client import Client
    import keyboard
    import pyautogui
    import pyperclip
    import ctypes
except ImportError as e:
    missing_module = str(e).split(' ')[-1].replace("'", "")
    import subprocess
    subprocess.call(['pip', 'install', '-U', missing_module])
    import re
    import os
    import time
    import json
    from g4f.client import Client
    import keyboard
    import pyautogui
    import pyperclip
    import ctypes

""""""
from setup_config_g4f import *

app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]
app_title.resizeTo(836, 144)
app_title.moveTo(-8, 119)
for i in range(20):
    app_title.moveRel(0, 10)
    time.sleep(0.005)

# вызов нейро чата
client = Client()


def ask_gpt(messages: list) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages)
        return response.choices[0].message.content
    except Exception as g4fe:
        print(f"{RED}Error")
        input(g4fe)


# from g4f.models import

# Проверка наличия файлов и создание при необходимости
def file_create(name):
    if not os.path.exists(name):
        with open(name, 'w', encoding='utf-8') as file_p:
            file_p.write("")


file_create('G4f_action.txt')
file_create('prompt_gpt_action.txt')
file_create('prompt_gpt_history.txt')
file_create('gpt_code_error.txt')
file_create('gpt_code_format.py')
file_create('gpt_code.py')


# Функция проверки того, пуст ли файл
def is_file_empty(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_e:
            return not bool(file_e.read().strip())
    except FileNotFoundError:
        return True


if not is_file_empty('gpt_role.txt'):
    with open('gpt_role.txt', 'r', encoding='utf-8') as file:
        default_role = file.read().split('\n\n')[0]

if is_file_empty('G4f_action.txt'):
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file_s:
        # Оставить файл пустым
        pass
    printt("Запрос пуст, история очищена!")
    exit()
    # os.startfile('G4f_action.txt')
    # input("укажите действие в G4f_action.txt")

if not os.path.exists("gpt_code.py"):
    with open("gpt_code.py", "w", encoding='utf-8'):
        pass


# Сохранение сообщений в файл
def save_messages(messages):
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file_p:
        json.dump(messages, file_p, ensure_ascii=False, indent=4)


# Загрузка сообщений из файла
def load_messages():
    try:
        with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file_l:
            messages = json.load(file_l)  # messages для нейро чата
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []
    return messages


# Проверка содержимого файла
if not is_file_empty('prompt_gpt_action.txt'):
    with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Если содержимое - пустой список, очистить файл
    if not data:
        with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file:
            file.write('')

print(default_role)

try:

    if is_file_empty('G4f_action.txt'):
        exit()
    with open('G4f_action.txt', 'r', encoding='utf-8') as file:
        action = file.read()
    prompt_gpt_action = load_messages()
    if action == "ошибка" or not is_file_empty('gpt_code_error.txt'):
        print()
        gun_fire(3)
        with open('gpt_code.py', 'r', encoding='utf-8') as file:
            code = file.read()
        with open('gpt_code_error.txt', 'r', encoding='utf-8') as file:
            error = file.read()
        print(action)
        # print(code)
        print(error)
        # prompt_gpt_action.append({"role": "user", "content": action})
        # prompt_gpt_action.append({"role": "user", "content": code})
        prompt_gpt_action.append({"role": "user", "content": error})
        responses = ask_gpt(prompt_gpt_action)
        prompt_gpt_action.append({"role": "assistant", "content": responses})
    else:
        print(action)
        if is_file_empty('prompt_gpt_action.txt'):
            prompt_gpt_action.append({"role": "user", "content": default_role + " " + action})
        else:
            prompt_gpt_action.append({"role": "user", "content": action})
        timer = 0
        responses = ask_gpt(prompt_gpt_action)
        prompt_gpt_action.append({"role": "assistant", "content": responses})
    save_messages(prompt_gpt_action)
    response_code = responses
    first_line = response_code.split('\n')[0]
    # first_line50 = 50 символов
    printt(f"\n{LYE} {first_line[:30]} ")
    with open('gpt_code_format.py', 'w', encoding='utf-8') as file_f:
        file_f.write(response_code)
    pattern = r'```python\n(.*?)```'
    matches = re.findall(pattern, response_code, re.IGNORECASE | re.DOTALL)
    # pattern = r'```\n(.*?)```'
    # matches = re.findall(pattern, response_code, re.IGNORECASE | re.DOTALL)
    if matches:
        match = '\n'.join(matches)
        # Find start and end indices of the match
        start_index = response_code.index(matches[0])
        end_index = response_code.index(matches[-1]) + len(matches[-1])
        # Extracting content before and after the pattern
        before_pattern = response_code[:start_index]
        after_pattern = response_code[end_index:]
        # app_title.minimize()
        # app_title.restore()
        content_code_format = f'"""\n{before_pattern.strip()}\n"""\n\n{match}\n\n"""\n{after_pattern.strip()}\n"""'
        content_code = f'{match}'
        print()
        gun_fire(3)
        print()

        try:
            with open('gpt_code_format.py', 'w', encoding='utf-8') as file_f:
                file_f.write(content_code_format)
            with open('gpt_code.py', 'w', encoding='utf-8') as file_c:
                file_c.write(content_code)
        except Exception as e:
            with open('gpt_code_format.py', 'w', encoding='utf-8') as file_f:
                file.write(response_code)
            print(e)
        time.sleep(0.1)

        try:
            os.startfile("gpt_code_tester.lnk")
        except FileNotFoundError:
            os.startfile("gpt_code_tester.py")
    else:
        # Открываем файл и загружаем данные
        with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)
        # Удаляем последние две позиции
        data = data[:-2]
        # Сохраняем обновлённые данные обратно в файл
        with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Не найден код. Последние две позиции удалены.")

        os.startfile("G4f_action.lnk")
        exit()

except Exception as e:
    print(e)
    input()
    # os.startfile(f"{app_title_window}")
    # exit()
