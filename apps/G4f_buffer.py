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


default_role = "помогай с кодом в Python"

role_message = [{"role": "system", "content": default_role}]

# Проверка наличия файлов и создание при необходимости
if not os.path.exists('prompt_gpt.txt'):
    with open('prompt_gpt.txt', 'w', encoding='utf-8') as file_prompt_gpt:
        file_prompt_gpt.write("")

    # Функция проверки того, пуст ли файл


def is_file_empty(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_e:
            return not bool(file_e.read().strip())
    except FileNotFoundError:
        return True


if is_file_empty('prompt_gpt.txt'):
    with open('prompt_gpt.txt', 'w', encoding='utf-8') as file:
        json.dump(role_message, file, ensure_ascii=False, indent=4)

with open('prompt_gpt.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

first_object = data[0]["content"]

role_message = [{"role": "system", "content": first_object}]

with open("prompt_gpt.txt", "w") as file:
    file.truncate()


def print_text_by_character(text):
    for char in text:
        print(char)

print(f"""\
╔{"═" * 41}╗
║ буферная нейронка                       ║
╠{"═" * 41}╣
║ SHIFT + WIN для смены роли              ║
║ SHIFT + STRL для сброса чата            ║
║ LT + WIN - выделить текст для генерации ║
╚{"═" * 41}╝
роль: {first_object}
""")

neyro_models = """
gpt_35_turbo_16k_0613
gpt_35_long
gpt_35_turbo
gpt_35_turbo_0613
gpt_35_turbo_16k
gpt_4
gpt_4 0613
gpt_4_32k
gpt_4_32k_0613
gpt_4_turbo
Gpt6
GptForLove           
"""

# Преобразование строки в список построчно
neyro_models_list = neyro_models.strip().split('\n')

current_model_idx = 0

# вызов нейро чата
def ask_gpt(messages: list) -> str:
    global current_model_idx
    while current_model_idx < len(neyro_models_list):
        print(f'{neyro_models_list[current_model_idx]} ', end="")
        try:
            response = g4f.ChatCompletion.create(
                model=getattr(g4f.models, neyro_models_list[current_model_idx]),
                messages=messages)
            return response
        except Exception as e:
            print(f"Error")
            current_model_idx += 1
    return "All models failed to provide a response."


# Сохранение сообщений в файл
def save_messages(messages):
    with open('prompt_gpt.txt', 'w', encoding='utf-8') as file_s:
        json.dump(messages, file_s, ensure_ascii=False, indent=4)


# Загрузка сообщений из файла
def load_messages():
    try:
        with open('prompt_gpt.txt', 'r', encoding='utf-8') as file_l:
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
                print("+", sep='', end='', flush=True)
                prompt_gpt = load_messages()
                data = pyperclip.paste()
                prompt_gpt.append({"role": "user", "content": data})
                responses = ask_gpt(prompt_gpt)
                print("=", sep='', end='', flush=True)
                pyperclip.copy(responses)
                time.sleep(0.2)
                keyboard.press_and_release('ctrl + v')
                # pyautogui.hotkey('ctrl', 'v')                
                prompt_gpt.append({"role": "assistant", "content": responses})
                save_messages(prompt_gpt)
            elif keyboard.is_pressed('shift+win'):
                prompt_gpt = load_messages()
                with open("prompt_gpt.txt", "w") as file:
                    file.truncate()
                    rolegpt = input("введите роль: ")
                role_message = [{"role": "system", "content": rolegpt}]
                save_messages(role_message)
                os.startfile(f"{app_title_window}")
                exit()
            elif keyboard.is_pressed('shift+ctrl'):
                print("-", sep='', end='', flush=True)
                prompt_gpt = load_messages()
                with open('prompt_gpt.txt', 'r', encoding='utf-8') as file:
                    data = json.load(file)
                first_object = data[0]["content"]
                with open("prompt_gpt.txt", "w") as file:
                    file.truncate()
                role_message = [{"role": "system", "content": first_object}]
                save_messages(role_message)
                os.startfile(f"{app_title_window}")
                exit()