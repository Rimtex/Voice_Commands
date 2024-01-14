import discord
import g4f
from craiyon import Craiyon
from concurrent.futures import ThreadPoolExecutor
import vocabulary
import asyncio

# from discord.ext import commands

with open('token.txt', 'r') as token_file:  # токен Discord скопировать в token.txt
    token = token_file.readline()

# Устанавливаем Intents для доступа к различным возможностям Discord, включая прослушивание сообщений.
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# ID канала, в котором бот должен работать: пкм на канал - копировать ID канала
target_channel_ids = [1068528493605961821, 1134946605372559360]  # Замените на реальный ID вашего канала

"""
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.type == discord.ChannelType.text and channel.id in target_channel_ids:
                print(f'Connected to text channel: {channel}')
"""


# для всех каналов

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channels = client.get_all_channels()
    for channel in channels:
        if channel.type == discord.ChannelType.text:
            print(f'Connected to text channel: {channel}')


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
(√¬_¬)
"""

executor = ThreadPoolExecutor()

toggle_switch = True


def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=messages)
    # print(response)
    return response


messagesgpt = []


@client.event
async def on_message(message):  # Обработчик сообщений в дискорде
    global toggle_switch
    prompt = message.content
    words = prompt.split()
    if message.author == client.user:
        return

    elif not toggle_switch and message.content in ["!", "ё"]:
        toggle_switch = True
        messagesgpt.clear()
        await message.channel.send("(√¬_¬) готов базарить! че надо?")

    elif toggle_switch and len(words) == 1 and message.content in ["сброс", "сначала", "снова", "#", "№", "$"]:
        messagesgpt.clear()
        await message.channel.send("(↺▪˽▪) чат сброшен")

    elif toggle_switch and message.content in ["!", "ё"]:
        toggle_switch = False
        messagesgpt.clear()
        await message.channel.send("(ꞁꞁ×_×)")

    elif toggle_switch and not message.content.startswith('3!') and not message.content.startswith('`'):
        gptgprompt = message.content
        if gptgprompt is not None:
            print(gptgprompt)
            messagesgpt.append({"role": "user", "content": gptgprompt})
            messagesgpt.append({"role": "assistant", "content": ask_gpt(messages=messagesgpt)})
            response = await client.loop.run_in_executor(executor, ask_gpt, messagesgpt)
            # response = ask_gpt(messages=messagesgpt)
            await message.channel.send(response)

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


"""
    prompt = message.content
    words = prompt.split()

    elif len(words) == 1 and (words[0] == "анекдот"):
        await message.channel.send(vocabulary.random_anecdote())
    elif len(words) == 1 and (words[0] == "волк"):
        await message.channel.send(vocabulary.sp_rec_reaction_auf())
    elif len(words) == 1 and (words[0] == "афоризм"):
        await message.channel.send(vocabulary.random_response_aphorism())
    elif len(words) == 1 and (words[0] == "стих"):
        await message.channel.send(vocabulary.random_rhymes())
"""

client.run(token)  # Запускаем бота
