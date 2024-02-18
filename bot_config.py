import os
import g4f
from craiyon import Craiyon
import json
import random


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


# вызов нейро чата
def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k_0613,
        provider=g4f.Provider.GPTalk,  # FakeGpt GPTalk 
        messages=messages)
    # print(response)
    return response


# Проверка наличия файлов и создание при необходимости
if not os.path.exists('2000.txt'):
    with open('2000.txt', 'w', encoding='utf-8') as file2000:
        file2000.write("")
if not os.path.exists('messagesgpt.txt'):
    with open('messagesgpt.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write("")
if not os.path.exists('gptrole.txt'):
    with open('gptrole.txt', 'w', encoding='utf-8') as filegptrole:
        filegptrole.write("")
if not os.path.exists('gptrole.txt'):
    with open('last_gptrole.txt', 'r', encoding='utf-8') as last_gptrole:
        filegptrole.write("")

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
