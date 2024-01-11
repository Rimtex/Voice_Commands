import discord
import g4f
from concurrent.futures import ThreadPoolExecutor
import vocabulary

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


def process_message_bing(gptprompt):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,  # по сути - Bing
        messages=[{"role": "user", "content": gptprompt}],
    )
    return response


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


executor = ThreadPoolExecutor()


@client.event
async def on_message(message):  # Обработчик сообщений в дискорде
    prompt = message.content
    words = prompt.split()
    if message.author == client.user:
        return

    elif message.content.startswith('2!'):
        gptprompt = message.content[2:]
        if gptprompt is not None:
            response = await client.loop.run_in_executor(executor, process_message_bing, gptprompt)
            await message.channel.send(response)

    elif message.content.startswith('!'):
        gptprompt = message.content[1:]
        if gptprompt is not None:
            response = await client.loop.run_in_executor(executor, process_message_gpt, gptprompt)
            response_text = ''.join(response)
            response_text = response_text.strip()
            await message.channel.send(response_text)

    elif len(words) == 1 and (words[0] == "анекдот"):
        await message.channel.send(vocabulary.random_anecdote())
    elif len(words) == 1 and (words[0] == "волк"):
        await message.channel.send(vocabulary.sp_rec_reaction_auf())
    elif len(words) == 1 and (words[0] == "афоризм"):
        await message.channel.send(vocabulary.random_response_aphorism())
    elif len(words) == 1 and (words[0] == "стих"):
        await message.channel.send(vocabulary.random_rhymes())


client.run(token)  # Запускаем бота
