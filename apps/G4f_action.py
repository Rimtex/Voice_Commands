import re
import os
import time
import json
import g4f
import keyboard
import pyautogui
import pyperclip
import ctypes

from setup_config_apps import create_shortcut

""""""
from setup_config_apps import create_shortcut
app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]

def get_keyboard_layout_name():
    # Преобразуем хэндл в строку
    layout_name = ctypes.create_string_buffer(8)
    ctypes.windll.user32.GetKeyboardLayoutNameA(layout_name)
    return layout_name.value.decode()


def switch_to_english_keyboard_layout():
    # Получаем хэндл текущего окна
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    # Получаем английскую раскладку клавиатуры
    english_layout_id = 0x04090409
    # Устанавливаем раскладку клавиатуры
    ctypes.windll.user32.ActivateKeyboardLayout(english_layout_id, 0)
    # Уведомляем систему о смене раскладки
    ctypes.windll.user32.PostMessageA(hwnd, 0x50, 0, 0)


def check_and_switch_to_english_layout():
    current_layout = get_keyboard_layout_name()
    if current_layout != "00000409":  # 00000409 - идентификатор английской раскладки
        switch_to_english_keyboard_layout()


# Вызываем функцию для проверки и при необходимости переключения на английскую раскладку
check_and_switch_to_english_layout()

neyro_model = "gpt_35_turbo_16k"

# model=g4f.models.gpt_35_turbo_16k,


default_role = f"""\
Python
ты нужен чтобы создавать работающие программы из описания текста
твой ответ должен содержать только работающий код\
"""
role_message = [{"role": "system", "content": default_role}]

# Проверка наличия файлов и создание при необходимости
if not os.path.exists('prompt_gpt_action.txt'):
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file_prompt_gpt_action:
        file_prompt_gpt_action.write("")


# Функция проверки того, пуст ли файл
def is_file_empty(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_e:
            return not bool(file_e.read().strip())
    except FileNotFoundError:
        return True


if is_file_empty('prompt_gpt_action.txt'):
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file:
        json.dump(role_message, file, ensure_ascii=False, indent=4)

with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

first_object = data[0]["content"]

role_message = [{"role": "system", "content": first_object}]


with open("prompt_gpt_action.txt", "w") as file:
    file.truncate()

if not os.path.exists("gpt_code.py"):
    with open("gpt_code.py", "w", encoding='utf-8'):
        pass


def print_text_by_character(text):
    for char in text:
        print(char)

x = 64
print(f"""
╔{"═" * x}╗
║ буферная нейронка для запуска файла с кодом ответа GPT         ║
╠{"═" * x}╣
║ SHIFT + WIN для смены роли                                     ║
║ SHIFT + STRL для сброса                                        ║
║ LT + WIN - для ответа из буфера                                ║
╟{"─" * x}╢
║ модель: {neyro_model}{" " * (x - 10 - len(neyro_model))} ║
╚{"═" * x}╝
роль: {first_object}\
""")

# вызов нейро чата
def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=getattr(g4f.models, neyro_model),
        # model=g4f.models.gpt_35_long,
        provider=g4f.Provider.GPTalk,  # FakeGpt GPTalk
        messages=messages)
    return response


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


if __name__ == "__main__":
    while True:
        time.sleep(0.1)
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed('alt+win'):
                app_title.minimize()
                app_title.restore()
                prompt_gpt_action = load_messages()
                data = pyperclip.paste()
                print("+")
                print(data)             
                prompt_gpt_action.append({"role": "user", "content": data})                
                responses = ask_gpt(prompt_gpt_action)
                prompt_gpt_action.append({"role": "assistant", "content": responses})
                save_messages(prompt_gpt_action)
                response_code = responses
                first_line = response_code.split('\n')[0]
                print("=", sep='', end='', flush=True) 
                print(responses)
                pattern1 = r'```python\n(.*?)```'
                pattern2 = r'```Python\n(.*?)```'
                match = re.search(pattern1 + '|' + pattern2, response_code, re.DOTALL)  
                if match:             
                    content_code = match.group(1)                     
                    with open('gpt_code.py', 'w', encoding='utf-8') as file:
                        file.write(content_code)
                    os.startfile("gpt_code.py")
                elif responses.strip().startswith("import"):    
                    content_code = responses              
                    with open('gpt_code.py', 'w', encoding='utf-8') as file:
                        file.write(content_code)
                    os.startfile("gpt_code.py")

            elif keyboard.is_pressed('shift+win'):
                app_title.minimize()
                app_title.restore()
                prompt_gpt_action = load_messages()
                with open("prompt_gpt_action.txt", "w") as file:
                    file.truncate()
                    rolegpt = input("введите роль: ")
                role_message = [{"role": "system", "content": rolegpt}]
                save_messages(role_message)
                os.startfile(f"{app_title_window}")
                exit()
            elif keyboard.is_pressed('shift+ctrl'):
                print("-", sep='', end='', flush=True)
                prompt_gpt_action = load_messages()
                with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file:
                    data = json.load(file)
                first_object = data[0]["content"]
                with open("prompt_gpt_action.txt", "w") as file:
                    file.truncate()
                role_message = [{"role": "system", "content": first_object}]
                save_messages(role_message)
                os.startfile(f"{app_title_window}")
                exit()