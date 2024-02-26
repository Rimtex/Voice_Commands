import os
import time
import g4f
from craiyon import Craiyon
import json
import random

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

# вызов рисовалки
def genimage(imgprompt):
    generator = Craiyon()  # Instantiate the api wrapper
    try:
        result = generator.generate(imgprompt)
        image_urls = result.images  # Get the list of image URLs
        return image_urls
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def printt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

Providers = """
GPTalk
FreeChatgpt
Llama2
GeminiProChat
Bing
Aura
"""

neyro_models = """
gpt_35_turbo_16k_0613
gpt_35_turbo_16k
gpt_35_turbo_0613
default
gpt_4
gpt_4_turbo
gpt_4_32k_0613
gpt_4_0613
gpt_4_32k
gemini_pro
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

# Преобразование строки в список построчно
neyro_models_list = neyro_models.strip().split('\n')
providers_list = Providers.strip().split('\n')

current_provider_idx = 0
current_model_idx = 0


# вызов нейро чата
def ask_gpt(messages: list) -> str:
    x = 0
    global current_model_idx
    global current_provider_idx
    while current_provider_idx < len(providers_list): 
        current_model_idx = 0
        print(f'{LCY}> {providers_list[current_provider_idx]} > ')
        while current_model_idx < len(neyro_models_list): 
            #x = x + 20       
            printt(f'{LGR}> {neyro_models_list[current_model_idx]} > ')
            try:            
                response = g4f.ChatCompletion.create(
                    model=getattr(g4f.models, neyro_models_list[current_model_idx]),                
                    provider=getattr(g4f.Provider, providers_list[current_provider_idx]),
                    # provider=g4f.Provider.FakeGpt,
                    messages=messages)
                return response                              
            except Exception as e:                
                print(f"{RED}Error")
                print(f"{WHI} + {e}")
                current_model_idx += 1           
        print("All models failed to provide a response.")
        current_provider_idx += 1
    return input("All providers and models failed to provide a response.")


# Проверка наличия файлов и создание при необходимости
# Проверка наличия файлов и создание при необходимости
def file_create(name):
    if not os.path.exists(name):
        with open(name, 'w', encoding='utf-8') as file_p:
            file_p.write("")

file_create('messagesgpt.txt')
file_create('gptrole.txt')
file_create('last_gptrole.txt')
file_create('sequences_role.txt')
file_create('random_role.txt')
file_create('last_gptrole.txt')


# чтение последней роли
with open('last_gptrole.txt', 'r', encoding='utf-8') as last_gptrole:
    last_role = last_gptrole.read()


# Функция проверки того, пуст ли файл
def is_file_empty(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return not bool(file.read().strip())
    except FileNotFoundError:
        return True


# Загрузка сообщений из файла
def load_messages():
    try:
        with open('messagesgpt.txt', 'r', encoding='utf-8') as file:
            messages = json.load(file)  # messages для нейро чата
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []
    return messages


# Сохранение сообщений в файл
def save_messages(messages):
    with open('messagesgpt.txt', 'w', encoding='utf-8') as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)


# Функция для чтения роли по умолчанию из файла
def read_default_role(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            default_role = file.read().strip()
        return default_role
    except FileNotFoundError:
        return None


# Функция смены случайной роли
def change_role_gpt():
    with open("random_role.txt", "r", encoding="utf-8") as file:
        roles_text = file.read()
    roles_list = roles_text.split('\n')  # Пустая строка разделяет роли
    random_role = random.choice(roles_list)
    # Создайте список, содержащий только сообщение роли по умолчанию.
    role_message = [{"role": "system", "content": f"{random_role}"}]
    # Сохраните сообщение роли в файл
    with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write(random_role)
    save_messages(role_message)


# Переменная для хранения выбранных ролей
chosen_roles = []


# Функция смены случайной роли, избегать повторного выбора определенных ролей
def change_new_role_gpt():
    # Чтение ролей из файла
    with open("random_role.txt", "r", encoding="utf-8") as file:
        roles_text = file.read()

    # Получение списка ролей из текста
    roles_list = roles_text.split('\n')

    # Исключение уже выбранных ролей из списка
    available_roles = [role for role in roles_list if role not in chosen_roles]

    if not available_roles:
        print("Все роли уже были выбраны.")
        return

    # Выбор случайной роли
    random_role = random.choice(available_roles)

    # Создание списка сообщений с новой ролью
    role_message = [{"role": "system", "content": f"{random_role}"}]

    # Добавление выбранной роли к уже выбранным
    chosen_roles.append(random_role)

    # Сохранение выбранной роли в файл (необязательно)
    with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write(random_role)

    # Сохранение сообщений
    save_messages(role_message)


# роли по очереди
def sequences_role_gpt():
    global current_role_index

    with open("sequences_role.txt", "r", encoding="utf-8") as file:
        roles_text = file.read()

    roles_list = roles_text.split('\n')  # Пустая строка разделяет роли

    if not hasattr(sequences_role_gpt, 'current_role_index'):
        # Если переменная не существует, создаем ее и устанавливаем в 0
        sequences_role_gpt.current_role_index = 0

    # Получаем текущую роль
    current_role = roles_list[sequences_role_gpt.current_role_index]

    # Увеличиваем индекс для следующего вызова функции
    sequences_role_gpt.current_role_index = (sequences_role_gpt.current_role_index + 1) % len(roles_list)

    # Если все роли использованы, обнуляем счетчик
    if sequences_role_gpt.current_role_index == 0:
        sequences_role_gpt.current_role_index = 0
    role_message = [{"role": "system", "content": f"{current_role}"}]
    save_messages(role_message)
    return current_role


"""
# Пример использования
for _ in range(len(open("sequences_role.txt", "r", encoding="utf-8").read().split('\n'))):
    role = sequences_role_gpt()
    print(role)
"""

if is_file_empty('gptrole.txt'):
    change_role_gpt()

if is_file_empty('messagesgpt.txt'):
    role_message = [{"role": "system", "content": f"{read_default_role('gptrole.txt')}"}]
    save_messages(role_message)

default_role = read_default_role('gptrole.txt')
