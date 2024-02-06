import os
import time
import json
import g4f
import keyboard
import py_win_keyboard_layout
import pyautogui
import pyperclip

import ctypes

def get_keyboard_layout_name():
    # Получаем хэндл текущего окна
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    # Получаем хэндл раскладки клавиатуры
    layout_id = ctypes.windll.user32.GetKeyboardLayout(hwnd)
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
        print("Текущая раскладка не английская. Переключаем на английскую.")
        switch_to_english_keyboard_layout()
    else:
        print("Текущая раскладка уже английская.")

# Вызываем функцию для проверки и при необходимости переключения на английскую раскладку
check_and_switch_to_english_layout()

neyro_model = "gpt_35_turbo_16k_0613"

default_role = "!Пиши только Python код!"

role_message = [{"role": "user", "content": default_role}]

# Проверка наличия файлов и создание при необходимости
if not os.path.exists('prompt_gpt.txt'):
    with open('prompt_gpt.txt', 'w', encoding='utf-8') as file_prompt_gpt:
        file_prompt_gpt.write("")   

# Функция проверки того, пуст ли файл
def is_file_empty(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return not bool(file.read().strip())
    except FileNotFoundError:
        return True    
if is_file_empty('prompt_gpt.txt'):
    with open('prompt_gpt.txt', 'w', encoding='utf-8') as file:
        json.dump(role_message, file, ensure_ascii=False, indent=4)

with open('prompt_gpt.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)  

first_object = data[0]["content"]   

role_message = [{"role": "user", "content": first_object}]

with open("prompt_gpt.txt", "w") as file:
    file.truncate()

def print_text_by_character(text):
    for char in text:
        print(char)

print(f"буферная нейронка")
print(f"модель: {neyro_model}")
print(f"роль: {first_object}")
print("SHIFT + WIN для смены роли")
print("STRL + WIN для сброса чата")
print("выделите текст и нажмите: ALT + WIN для генерации")

prov = "GPTalk"
## ! нужно подставить правильно prov в provider=g4f.Provider.GPTalk
# вызов нейро чата
def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=getattr(g4f.models, neyro_model),
        # model=g4f.models.gpt_35_turbo_16k_0613,
        provider=g4f.Provider.GPTalk, # FakeGpt GPTalk 
        messages=messages)
    return response

# Сохранение сообщений в файл
def save_messages(messages):
    with open('prompt_gpt.txt', 'w', encoding='utf-8') as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)
# Загрузка сообщений из файла
def load_messages():
    try:
        with open('prompt_gpt.txt', 'r', encoding='utf-8') as file:
            messages = json.load(file)  # messages для нейро чата
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
                time.sleep(1)
                keyboard.press_and_release('ctrl + c') 
                time.sleep(0.1)         
                data = pyperclip.paste()
                time.sleep(0.1)
                prompt_gpt.append({"role": "user", "content": data})
                response = ask_gpt(prompt_gpt)
                print("=", sep='', end='', flush=True)
                pyperclip.copy(response)    
                time.sleep(0.2)
                keyboard.press_and_release('ctrl + v')
                # pyautogui.hotkey('ctrl', 'v')                
                prompt_gpt.append({"role": "assistant", "content": response})
                save_messages(prompt_gpt)            
            elif keyboard.is_pressed('shift+win'):
                prompt_gpt = load_messages()
                with open("prompt_gpt.txt", "w") as file:
                    file.truncate()
                role_message = [{"role": "user", "content": input("введите роль: ")}]    
                save_messages(role_message)
            elif keyboard.is_pressed('ctrl+win'):
                print("-", sep='', end='', flush=True)
                prompt_gpt = load_messages()
                with open('prompt_gpt.txt', 'r', encoding='utf-8') as file:
                    data = json.load(file)  
                first_object = data[0]["content"]   
                with open("prompt_gpt.txt", "w") as file:
                    file.truncate()
                role_message = [{"role": "user", "content": first_object}]    
                save_messages(role_message)
                  













