import discord
import g4f
from craiyon import Craiyon
from concurrent.futures import ThreadPoolExecutor
import vocabulary
import asyncio

with open('token.txt', 'r') as token_file:  # токен Discord скопировать в token.txt
    token = token_file.readline()

# Устанавливаем Intents для доступа к различным возможностям Discord, включая прослушивание сообщений.
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# ID канала, в котором бот должен работать: пкм на канал - копировать ID канала
target_channel_ids = [1068528493605961821, 1134946605372559360]  # Замените на реальный ID вашего канала


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.type == discord.ChannelType.text and channel.id in target_channel_ids:
                print(f'Connected to text channel: {channel}')


# для всех каналов
"""
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channels = client.get_all_channels()
    for channel in channels:
        if channel.type == discord.ChannelType.text:
            print(f'Connected to text channel: {channel}')
"""

executor = ThreadPoolExecutor()


def process_message_gpt(gptprompt):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": gptprompt}],
        stream=True,
    )
    bot_responses = []
    for gptmessage in response:
        bot_responses.append(gptmessage)
    return bot_responses


def process_message_bing(gptprompt):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,  # по сути - Bing
        messages=[{"role": "user", "content": gptprompt}],
    )
    return response


def genimage(imgprompt):
    generator = Craiyon()  # Instantiate the api wrapper
    try:
        result = generator.generate(imgprompt)
        image_urls = result.images  # Get the list of image URLs
        return image_urls
    except Exception as e:
        print(f"Error generating image: {e}")
        return None


@client.event
async def on_message(message):  # Обработчик сообщений в дискорде
    prompt = message.content
    words = prompt.split()
    if message.author == client.user:
        return

    elif message.content.startswith('!'):
        gptprompt = message.content[1:]
        if gptprompt is not None:
            response = await client.loop.run_in_executor(executor, process_message_gpt, gptprompt)
            response_text = ''.join(response)
            response_text = response_text.strip()
            await message.channel.send(response_text)

    elif message.content.startswith('2!'):
        gptprompt = message.content[2:]
        if gptprompt is not None:
            response = await client.loop.run_in_executor(executor, process_message_bing, gptprompt)
            await message.channel.send(response)

    elif message.content.startswith('3!'):
        imgprompt = message.content[2:]
        if imgprompt is not None:
            await message.channel.send(f"Малюю каляку \"{imgprompt}\"...")

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
                first_part_message = " ".join(first_part)
                second_part_message = " ".join(second_part)

                # Send two separate messages with each set of URLs
                await message.channel.send(first_part_message)
                await message.channel.send(second_part_message)
            else:
                await message.channel.send("Не удалось выполнить запрос после нескольких попыток.")

    elif len(words) == 1 and (words[0] == "анекдот"):
        await message.channel.send(vocabulary.random_anecdote())
    elif len(words) == 1 and (words[0] == "волк"):
        await message.channel.send(vocabulary.sp_rec_reaction_auf())
    elif len(words) == 1 and (words[0] == "афоризм"):
        await message.channel.send(vocabulary.random_response_aphorism())
    elif len(words) == 1 and (words[0] == "стих"):
        await message.channel.send(vocabulary.random_rhymes())


client.run(token)  # Запускаем бота
