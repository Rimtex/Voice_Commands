import os
import discord
import g4f
from craiyon import Craiyon
from concurrent.futures import ThreadPoolExecutor
import vocabulary
import asyncio
import json

# Проверка наличия файла '2000.txt' и его создание при необходимости
if not os.path.exists('2000.txt'):
    with open('2000.txt', 'w', encoding='utf-8') as file2000:
        file2000.write("")
with open('token.txt', 'r') as token_file:  # токен Discord скопировать в token.txt
    token = token_file.readline()

# Устанавливаем Intents для доступа к различным возможностям Discord, включая прослушивание сообщений.
intents = discord.Intents.all()
client = discord.Client(intents=intents)

"""
# ID канала, в котором бот должен работать: пкм на канал - копировать ID канала
target_channel_ids = [1068528493605961821, 1134946605372559360]  # Замените на реальный ID вашего канала
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.type == discord.ChannelType.text and channel.id in target_channel_ids:
                print(f'Connected to text channel: {channel}')
"""


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


"""
FakeGpt
GPTalk
"""
# вызов нейро чата
def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k_0613,
        # model=g4f.models.gpt_35_turbo_16k_0613,
        # provider=g4f.Provider.FakeGpt,
        messages=messages)
    # print(response)
    return response


# Проверка наличия файлов и создание при необходимости
if not os.path.exists('messagesgpt.txt'):
    with open('messagesgpt.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write("")
if not os.path.exists('gptrole.txt'):        
    with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write("")    

# Загрузка сообщений из файла
def load_messages():
    try:
        with open('messagesgpt.txt', 'r', encoding='utf-8') as file:
            messages = json.load(file)
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

# Функция проверки того, пуст ли файл
def is_file_empty(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return not bool(file.read().strip())
    except FileNotFoundError:
        return True

messagesgpt_file_path = 'messagesgpt.txt'
gptrole_file_path = 'gptrole.txt'

import random

def change_role_gpt():
    with open("random_role.txt", "r", encoding="utf-8") as file:
        roles_text = file.read()
    roles_list = roles_text.split('\n\n')  # Пустая строка разделяет роли
    random_role = random.choice(roles_list)
    # Создайте список, содержащий только сообщение роли по умолчанию.
    role_message = [{"role": "user", "content": f"{random_role}"}]
    # Сохраните сообщение роли в файл
    with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write(random_role)
    save_messages(role_message)    

if is_file_empty(gptrole_file_path):
    change_role_gpt()

executor = ThreadPoolExecutor()  # без него ошибка - client.py:441>> is being executed.

toggle_switch = True  # выключатель нейро чата

if is_file_empty(messagesgpt_file_path):  
    role_message = [{"role": "user", "content": f"!Твоя роль: {read_default_role('gptrole.txt')}!"}]
    save_messages(role_message)

default_role = read_default_role('gptrole.txt')

@client.event
async def on_ready():
    # Устанавливаем статус "играет в:"
    await client.change_presence(activity=discord.Game(default_role[:128]))
    print(f'{client.user} has connected to Discord!')
    channels = client.get_all_channels()  # для всех каналов
    for channel in channels:
        if channel.type == discord.ChannelType.text:
            print(f'Connected to text channel: {channel}')
    if not is_file_empty(messagesgpt_file_path):           
        with open('messagesgpt.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            for key, value in item.items():
                print(f'"{key}": "{value}"')
            print()       


@client.event
async def on_message(message):  # Обработчик сообщений в дискорде

    global toggle_switch

    default_role = read_default_role('gptrole.txt')
    messagesgpt = load_messages()

    prompt = message.content
    words = prompt.split()

    if message.author == client.user:
        return
    
    elif len(words) == 1 and (words[0] == "анекдот"):
        await message.channel.send(vocabulary.random_anecdote())
    elif len(words) == 1 and (words[0] == "волк"):
        await message.channel.send(vocabulary.sp_rec_reaction_auf())
    elif len(words) == 1 and (words[0] == "афоризм"):
        await message.channel.send(vocabulary.random_response_aphorism())
    elif len(words) == 1 and (words[0] == "стих"):
        await message.channel.send(vocabulary.random_rhymes())
    elif len(words) == 1 and words[0] == "история":
        response = vocabulary.random_response_stories()
        if len(response) > 2000:
            chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
            for chunk in chunks:
                await message.reply(chunk)
        else:
            await message.reply(response)

    elif not toggle_switch and message.content in '#':
        toggle_switch = True
        await message.channel.send("(√¬_¬) готов базарить! че надо?")
    elif toggle_switch and message.content in '#':
        toggle_switch = False
        await message.channel.send("(ꞁꞁ×_×) свалил в помойку.")
    elif toggle_switch and message.content in '?':    
        with open("messagesgpt.txt", "w") as file:
            file.truncate(0)
        change_role_gpt()
        default_role = read_default_role('gptrole.txt')
        await client.change_presence(activity=discord.Game(default_role[:128]))
    elif toggle_switch and message.content in '$':
        with open("messagesgpt.txt", "w") as file:
            file.truncate(0)
        save_messages([{"role": "user", "content": default_role}])
        await message.channel.send("(↺▪˽▪) чат сброшен")
    elif toggle_switch and message.content.startswith('!'):
        with open("messagesgpt.txt", "w") as file:
            file.truncate(0)
        role_message = [{"role": "user", "content": f"!Твоя роль: {message.content[1:]}!"}]
        with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
            filemessagesgpt.write(f"{message.content[1:]}")   
        save_messages(role_message)
        default_role = read_default_role('gptrole.txt')
        await client.change_presence(activity=discord.Game(default_role[:128]))
            
    elif toggle_switch and not message.content.startswith('3!') and not message.content.startswith('`'):
        gptgprompt = message.content
        if gptgprompt is not None:
            print(message.author.display_name + ": " + gptgprompt)
            messagesgpt.append({"role": "user", "content": message.author.display_name + ": " + gptgprompt})
            response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
            messagesgpt.append({"role": "assistant", "content": response})
            save_messages(messagesgpt)
            if len(response) > 2000:
                chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
                for chunk in chunks:
                    await message.reply(chunk)
            else:
                await message.reply(response)

    elif message.content.startswith('3!'):
        imgprompt = message.content[2:]
        if imgprompt is not None:
            await message.channel.send(f"(~o▾o) Малюю каляку \"{imgprompt}\"...")
            retry_count = 9  # Set the maximum number of retries
            response = None
            while retry_count > 0:
                response = await client.loop.run_in_executor(executor, genimage, imgprompt)
                if response is not None:
                    break  # Break out of the loop if the response is successful
                else:
                    await asyncio.sleep(5)  # Wait for 5 seconds before retrying
                    retry_count -= 1

            if response is not None:
                async for msg in message.channel.history(limit=2):
                    if msg.author == client.user:
                        await msg.delete()

                # Split the list of image URLs into two parts
                first_part = response[:5]
                second_part = response[5:]

                # Join the image URLs into strings
                first_part_message = "\n".join(first_part)
                second_part_message = "\n".join(second_part)

                # Send two separate messages with each set of URLs
                await message.channel.send(first_part_message)
                await message.channel.send(second_part_message)
            else:
                await message.channel.send("Не удалось выполнить запрос после нескольких попыток.")

    elif message.content.startswith('`clear'):
        if message.author.display_name == "Rimtex":
            # Check if the command has the correct number of arguments
            args = message.content.split()
            if len(args) != 2 or not args[1].isdigit():
                await message.channel.send('Usage: `clear X (X should be a number)')
                return
            num_messages_to_delete = int(args[1])
            await message.channel.purge(limit=num_messages_to_delete + 1)


client.run(token)  # Запускаем бота
