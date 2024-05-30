import discord
from concurrent.futures import ThreadPoolExecutor
import vocabulary
import asyncio
import pyautogui
from bot_config import *


""" парсинг роли при запуске """
try:
    import requests
    from bs4 import BeautifulSoup
    # Отправляем GET-запрос к сайту
    response = requests.get("https://joyreactor.cc/")
    # Получаем HTML-код страницы
    html_code = response.text
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(html_code, 'html.parser')
    # Находим тег div с классом "description" и получаем текст
    description = soup.find('div', class_='description').text.strip()
    with open("messagesgpt.txt", "w") as file:
        file.truncate(0)
    role_message = [{"role": "user", "content": f"{description}"}]
    with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write(f"{description}")   
    save_messages(role_message)
except Exception as e:                
    print(e)


with open('token.txt', 'r') as token_file:  # токен Discord скопировать в token.txt
    token = token_file.readline()

""""""
from setup_config_apps import create_shortcut
app_title_window = os.path.basename(__file__).replace('.py', '')
create_shortcut(app_title_window, os.path.abspath(__file__))
app_title = pyautogui.getWindowsWithTitle(app_title_window)[0]

# Устанавливаем Intents для доступа к различным возможностям Discord, включая прослушивание сообщений.
intents = discord.Intents.all()
client = discord.Client(intents=intents)


default_role = read_default_role('gptrole.txt')

executor = ThreadPoolExecutor()  # без него ошибка - client.py:441>> is being executed.
toggle_switch = True  # выключатель нейро чата


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


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channels = client.get_all_channels()  # для всех каналов
    for channel in channels:
        if channel.type == discord.ChannelType.text:
            print(f'Connected to text channel: {channel}')

    # Устанавливаем статус "играет в:"
    await client.change_presence(activity=discord.Game(default_role[:128]))

    # вывод сохраненного чата в консоль
    if not is_file_empty('messagesgpt.txt'):
        with open('messagesgpt.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            for key, value in item.items():
                print(f'"{key}": "{value}"')
            print()    
        await asyncio.sleep(1)
        app_title.minimize()

@client.event
async def on_message(message):  # Обработчик сообщений в дискорде
    try:
        app_title.restore()

        global toggle_switch

        default_role = read_default_role('gptrole.txt')
        messagesgpt = load_messages()

        prompt = message.content
        words = prompt.split()

        if message.author == client.user:
            return

        elif len(words) == 1 and (words[0] == "ауф"):
            await message.message.delete() if message.guild else None
            auf_answer =  random.choice([vocabulary.sp_rec_reaction_auf(), vocabulary.random_response_aphorism()])
            await message.channel.send(auf_answer)
            gptgprompt = auf_answer
            if gptgprompt is not None:

                # роли случайно
                response = gptgprompt
                t = 5
                for i in range(t):                
                    change_new_role_gpt()
                    default_role = read_default_role('gptrole.txt')      
                    messagesgpt = load_messages()  
                    response = response
                    await client.change_presence(activity=discord.Game(f"{t} {default_role[:126]}"))
                    await asyncio.sleep(1)
                    messagesgpt.append({"role": "system", "content": response})                
                    response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
                    messagesgpt.append({"role": "assistant", "content": response})
                    save_messages(messagesgpt)
                    await asyncio.sleep(1)
                    response = response
                    if len(response) > 1980:
                        chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                        for chunk in chunks:
                            await message.reply(f"{t} {chunk}")
                    else:
                        await message.reply(f"{t} {response}")
                    t = t - 1

                change_new_role_gpt()    
                role_message = [{"role": "system", "content": f"{last_role}"}]
                with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
                    filemessagesgpt.write(last_role)        
                save_messages(role_message)            
                default_role = read_default_role('gptrole.txt')      
                messagesgpt = load_messages()  
                response = response
                await client.change_presence(activity=discord.Game(f"= {default_role[:126]}"))
                await asyncio.sleep(1)
                messagesgpt.append({"role": "user", "content": response})                
                response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
                messagesgpt.append({"role": "assistant", "content": response})
                save_messages(messagesgpt)
                await asyncio.sleep(1)
                response = response
                if len(response) > 1980:
                    chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                    for chunk in chunks:
                        await message.reply(f"= {chunk}")
                else:
                    await message.reply(f"= {response}")

                """
                # роли по порядку
                t = len(open("sequences_role.txt", "r", encoding="utf-8").read().split('\n\n'))
                response = gptgprompt
                for i in range(t):             
                    # change_role_gpt()
                    default_role = sequences_role_gpt()      
                    messagesgpt = load_messages()  
                    response = response
                    await client.change_presence(activity=discord.Game(f"{t} {default_role[:126]}"))
                    await asyncio.sleep(2)
                    messagesgpt.append({"role": "user", "content": response})                
                    response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
                    messagesgpt.append({"role": "assistant", "content": response})
                    save_messages(messagesgpt)                
                    if len(response) > 1980:
                        chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                        for chunk in chunks:
                            await message.reply(f"{t} {chunk}")
                    else:
                        await message.reply(f"{t} {response}")
                    t = t - 1
                """

                """
                change_role_gpt()    
                random_role = "сгенерируй код на Python на тему:"   
                role_message = [{"role": "system", "content": f"{random_role}"}]
                # Сохраните сообщение роли в файл
                with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
                    filemessagesgpt.write(random_role)        
                save_messages(role_message)
                default_role = read_default_role('gptrole.txt')      
                messagesgpt = load_messages()  
                response = response
                await client.change_presence(activity=discord.Game(f"+ {default_role[:126]}"))
                await asyncio.sleep(1)
                messagesgpt.append({"role": "user", "content": response})                
                response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
                messagesgpt.append({"role": "assistant", "content": response})
                save_messages(messagesgpt)
                await asyncio.sleep(1)
                response = response
                if len(response) > 1980:
                    chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                    for chunk in chunks:
                        await message.reply(chunk)
                else:
                    await message.reply(response)
                """
        elif len(words) == 1 and (words[0] == "волк"):
            await message.channel.send(vocabulary.sp_rec_reaction_auf())
        elif len(words) == 1 and (words[0] == "анекдот"):
            await message.channel.send(vocabulary.random_anecdote())
        elif len(words) == 1 and (words[0] == "афоризм"):
            await message.channel.send(vocabulary.random_response_aphorism())
        elif len(words) == 1 and (words[0] == "стих"):
            await message.channel.send(vocabulary.random_rhymes())
        elif len(words) == 1 and words[0] == "история":
            response = vocabulary.random_response_stories()
            if len(response) > 1980:
                chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                for chunk in chunks:
                    await message.reply(chunk)
            else:
                await message.reply(response)

        elif not toggle_switch and message.content in '#':
            toggle_switch = True
            await message.message.delete() if message.guild else None
            await message.channel.send("(√¬_¬) готов базарить! че надо?")
        elif toggle_switch and message.content in '#':
            toggle_switch = False
            await message.message.delete() if message.guild else None
            await message.channel.send("(ꞁꞁ×_×) свалил в помойку.")
        elif toggle_switch and message.content in '?':    
            with open("messagesgpt.txt", "w") as file:
                file.truncate(0)
            change_role_gpt()
            default_role = read_default_role('gptrole.txt')
            await message.message.delete() if message.guild else None
            await client.change_presence(activity=discord.Game(default_role[:128]))
        elif toggle_switch and message.content in '$':
            with open("messagesgpt.txt", "w") as file:
                file.truncate(0)
            save_messages([{"role": "system", "content": default_role}])
            await message.message.delete() if message.guild else None
            await message.channel.send("(↺▪˽▪) чат сброшен")
        elif toggle_switch and message.content.startswith('!'):
            with open("messagesgpt.txt", "w") as file:
                file.truncate(0)
            role_message = [{"role": "system", "content": f"{message.content[1:]}"}]
            with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
                filemessagesgpt.write(f"{message.content[1:]}")   
            save_messages(role_message)
            default_role = read_default_role('gptrole.txt')
            await message.message.delete() if message.guild else None
            await client.change_presence(activity=discord.Game(default_role[:128]))

        # чат с разными ролями  
        elif message.content.startswith('.'):  
            gptgprompt = message.content[1:]
            if gptgprompt is not None:

                # роли случайно
                response = gptgprompt
                t = 5
                for i in range(t):                
                    change_new_role_gpt()
                    default_role = read_default_role('gptrole.txt')      
                    messagesgpt = load_messages()  
                    response = response
                    await client.change_presence(activity=discord.Game(f"{t} {default_role[:126]}"))
                    await asyncio.sleep(1)
                    messagesgpt.append({"role": "user", "content": response})                
                    response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
                    messagesgpt.append({"role": "assistant", "content": response})
                    save_messages(messagesgpt)
                    await asyncio.sleep(1)
                    response = response
                    if len(response) > 1980:
                        chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                        for chunk in chunks:
                            await message.reply(f"{t} {chunk}")
                    else:
                        await message.reply(f"{t} {response}")
                    t = t - 1

                change_new_role_gpt()    
                role_message = [{"role": "system", "content": f"{last_role}"}]
                # Сохраните сообщение роли в файл
                with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
                    filemessagesgpt.write(last_role)        
                save_messages(role_message)            
                default_role = read_default_role('gptrole.txt')      
                messagesgpt = load_messages()  
                response = response
                await client.change_presence(activity=discord.Game(f"= {default_role[:126]}"))
                await asyncio.sleep(1)
                messagesgpt.append({"role": "user", "content": response})                
                response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
                messagesgpt.append({"role": "assistant", "content": response})
                save_messages(messagesgpt)
                await asyncio.sleep(1)
                response = response
                if len(response) > 1980:
                    chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                    for chunk in chunks:
                        await message.reply(f"= {chunk}")
                else:
                    await message.reply(f"= {response}")

        # стандартный чат         
        elif toggle_switch and not message.content.startswith(('3!', '`', '.')):
            gptgprompt = message.content
            if gptgprompt is not None:
                print(message.author.display_name + ": " + gptgprompt)
                messagesgpt.append({"role": "user", "content": message.author.display_name + ": " + gptgprompt})
                response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
                messagesgpt.append({"role": "assistant", "content": response})
                save_messages(messagesgpt)
                if len(response) > 1980:
                    chunks = [response[i:i+1980] for i in range(0, len(response), 1980)]
                    for chunk in chunks:
                        await message.reply(chunk)
                else:
                    await message.reply(response)

        # рисовалка
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

        app_title.minimize()        
        
    except Exception as e:                
                app_title.restore()
                print(e)

client.run(token)  # Запускаем бота
