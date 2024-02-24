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
    subprocess.call(['pip', 'install', '-U', missing_module])    
    import re
    import os
    import time
    import json
    import g4f
    import keyboard
    import pyautogui
    import pyperclip
    import ctypes

from colorama import Fore, init
RED = Fore.RED
LRE = Fore.LIGHTRED_EX
YEL = Fore.YELLOW
LYE = Fore.LIGHTYELLOW_EX
#  BLU = Fore.BLUE  # слишком тёмные цвета
LBL = Fore.LIGHTBLUE_EX
CYA = Fore.CYAN
LCY = Fore.LIGHTCYAN_EX
GRE = Fore.GREEN
LGR = Fore.LIGHTGREEN_EX
#  MAG = Fore.MAGENTA
LMA = Fore.LIGHTMAGENTA_EX
WHI = Fore.WHITE
BLA = Fore.BLACK
init(convert=True) 
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

# model=g4f.models.gpt_,
# provider=g4f.Provider.FakeGpt,  # FakeGpt GPTalk




neyro_models = """
gemini_pro
gpt_35_turbo_16k
gpt_35_turbo_16k_0613
gpt_35_turbo_0613
default
gpt_4
gpt_4_turbo
gpt_4_32k_0613
gpt_4_0613
gpt_4_32k
gpt_35_turbo
gpt_35_long
llama2_7b
llama2_13b
llama2_70b
codellama_34b_instruct
codellama_70b_instruct
mixtral_8x7b
mistral_7b
dolphin_mixtral_8x7b
lzlv_70b
airoboros_70b
airoboros_l2_70b
openchat_35
gemini
claude_v2
pi
"""


"""
default
FreeChatgpt: Yes, 
Llama2: Hello!
Bing: Hello, 
Aura: Hello! 
"""

"""
gpt_35_turbo_16k_0613
GeminiProChat: Hello Test,
FreeChatgpt: Hello, 
Aura: Hello! How can I assist you today?
Bing: Hello, this is Copilot.
"""

"""
gpt_35_turbo_16k
Aura: Hello! I'm here to help you with any questions or assistance you may need. How can I assist you today?
GeminiProChat: Hello, I am here to help you with your test.
GPTalk: Hello! How can I assist you today?
Bing: Hello, this is Copilot. I am an AI companion that can help you with information, questions, and conversation. 😊
"""


"""
gpt_35_turbo
Bing: Hello, this is Copilot.
Aura: Hello! 
"""

"""
airoboros_70b
GeminiProChat: Hello, this is a test. I am an AI chatbot, or virtual assistant, and I am here to help you with your inquiries. I can provide information, answer questions, and engage in conversations. I am trained on a massive amount of text and code data, which allows me to understand and respond to your requests in a natural and informative way.
Aura: Hello! How can I assist you today?
"""


# Преобразование строки в список построчно
neyro_models_list = neyro_models.strip().split('\n')

current_model_idx = 0


# вызов нейро чата
def ask_gpt(messages: list) -> str:
    x = 0
    global current_model_idx
    while current_model_idx < len(neyro_models_list): 
        x = x + 20       
        printt(f'{LGR}> {neyro_models_list[current_model_idx]} > ')
        try:            
            response = g4f.ChatCompletion.create(
                model=getattr(g4f.models, neyro_models_list[current_model_idx]),                
                # provider=g4f.Provider.FreeChatgpt,
                messages=messages)
            return response              
        except Exception as e:
            app_title.resizeTo(836, 144+x)
            print(f"{RED}Error")
            # print(f"{WHI} + {e}")
            current_model_idx += 1           
    return "All models failed to provide a response." 

"""

All models failed to provide a response.
"""


default_role = f"""\
Python
ты нужен чтобы создавать работающие программы из описания текста
твой ответ должен содержать полностью работающий код
в начале кода должен быть скрипт для установки нужных библиотек через - try: imports, except subprocess.call(['pip', 'install'])
"""
role_message = [{"role": "system", "content": default_role}]

# Проверка наличия файлов и создание при необходимости
def file_create(name):
    if not os.path.exists(name):
        with open(name, 'w', encoding='utf-8') as file_p:
            file_p.write("")

file_create('G4f_action.txt')
file_create('prompt_gpt_action.txt')
file_create('gpt_role.txt')
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


if is_file_empty('G4f_action.txt'):
    os.startfile('G4f_action.txt')
    input("укажите действие в G4f_action.txt")

if is_file_empty('gpt_role.txt'):
    os.startfile('gpt_role.txt')
    input("укажите роль в gpt_role.txt")
    
if is_file_empty('prompt_gpt_action.txt'):
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file:
        json.dump(role_message, file, ensure_ascii=False, indent=4)

with open('prompt_gpt_action.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
first_object = data[0]["content"]

role_message = [{"role": "system", "content": first_object}]


if not os.path.exists("gpt_code.py"):
    with open("gpt_code.py", "w", encoding='utf-8'):
        pass


def print_text_by_character(text):
    for char in text:
        print(char)

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


if not is_file_empty('gpt_role.txt'):
    with open('gpt_role.txt', 'r', encoding='utf-8') as file:
        default_role = file.read().split('\n\n')[0]
    role_message = [{"role": "system", "content": default_role}]
    with open('prompt_gpt_action.txt', 'w', encoding='utf-8') as file:
        file.truncate()
        json.dump(role_message, file, ensure_ascii=False, indent=4)

save_messages(role_message)


def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

def gun_fire():
    gun1 = "(√•_•)ԅ⌐╦╦═─"
    gun2 = "(√¬_¬)ԅ⌐╦╦═─"
    fire = "‒=═≡Ξ"
    for i in range(1, len(gun1)):
        print("\b"*len(gun1) + gun1[-i:], end='', flush=True)
        time.sleep(0.03)
    for i in range(1, len(fire)+1):
        print("\r" + gun2 + fire[:i], end='')
        time.sleep(0.005)
    for i in range(1, 15):
        print("\r" + gun2 + " "*i + "_", end='')
        time.sleep(0.01)
    for i in range(1, len(fire)+1):
        print("\r" + gun2 + fire[:i], end='')
        time.sleep(0.005)
    for i in range(1, 15):
        print("\r" + gun2 + " "*i + "─", end='')
        time.sleep(0.01)
    for i in range(1, len(fire)+1):
        print("\r" + gun2 + fire[:i], end='')
        time.sleep(0.005)
    print(" "*30 + "\r", end='')        
    for i in range(1, 15):
        print(gun2 + " "*i + "‾" + "\r", end='')
        time.sleep(0.01)    
    print(" "*30 + "\r", end='')      
    for i in range(len(gun1)+1):
        print("\r" + gun1[i:] + " " + "\r", end='')
        time.sleep(0.03)


try:    
    while current_model_idx < len(neyro_models_list):      
        if is_file_empty('G4f_action.txt'):
            exit()
        with open('G4f_action.txt', 'r', encoding='utf-8') as file:
            action = file.read()                     
        prompt_gpt_action = load_messages()        
        if action == "ошибка" or not is_file_empty('gpt_code_error.txt') :
            printt(f"{LYE} (√¬_¬)ԅ⌐╦╦═─‒=═≡Ξ gpt_code_tester.py ")
            with open('gpt_code.py', 'r', encoding='utf-8') as file:
                code = file.read()        
            with open('gpt_code_error.txt', 'r', encoding='utf-8') as file:
                error = file.read()
            print(action)
            print(code)
            print(error)
            # prompt_gpt_action.append({"role": "user", "content": action})   
            prompt_gpt_action.append({"role": "user", "content": code})            
            prompt_gpt_action.append({"role": "user", "content": error})
            responses = ask_gpt(prompt_gpt_action)
            prompt_gpt_action.append({"role": "assistant", "content": responses})
        else:
            print("\n" + action)
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
            gun_fire()
            print() 
            try:
                with open('gpt_code_format.py', 'w', encoding='utf-8') as file_f:
                    file_f.write(content_code_format)                         
                with open('gpt_code.py', 'w', encoding='utf-8') as file_c:         
                    file_c.write(content_code)
            except:
                with open('gpt_code_format.py', 'w', encoding='utf-8') as file_f:
                    file.write(response_code)     
            time.sleep(0.1)        
            try:  
                os.startfile(f"gpt_code_tester.lnk")
            except FileNotFoundError:   
                os.startfile("gpt_code_tester.py")
        if "IP" in first_line: 
            input("Доступ слишком частый. Пожалуйста, повторите попытку позже. продолжить?")
            current_model_idx += 1       
        elif "IP" not in first_line:               
            break                

except Exception as e:
    print(e)
    # input()
    # os.startfile(f"{app_title_window}")
    # exit()
