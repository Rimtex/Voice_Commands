
import discord
import g4f

import vocabulary

# Устанавливаем Intents для доступа к различным возможностям Discord, включая прослушивание сообщений.
intents = discord.Intents.all()
client = discord.Client(intents=intents)

TOKEN = "MTA3MzI5OTgyMDY4MjQyNDM1MA.GPC8da.-Y2OIyxXggb39AYYF1b_0n562kPyCR7G9SFmgo"  # Устанавливаем токен Discord

# Функция, которая будет вызываться, когда бот будет готов работать.
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channels = client.get_all_channels()
    for channel in channels:
        if channel.type == discord.ChannelType.text:
            print(f'Connected to text channel: {channel}')
            # Print all available providers


role1 = "!!Твоя роль - пьяный боевой генерал алкоголик! отвечай по-русски и с придурковатостью!!"
role2 = "!!отвечай на русском!!"


# Обработчик сообщений в дискорде
@client.event
async def on_message(message):
    prompt = message.content
    words = prompt.split()
    if message.author == client.user:
        return

    elif message.content.startswith('1!'):
        gptprompt = message.content[2:]
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": gptprompt}],
        )  # Alternative model setting
        if gptprompt is not None:
            await message.channel.send(response)

    elif message.content.startswith('2!'):
        gptprompt = message.content[2:]
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": gptprompt}],
            stream=True,
        )
        bot_responses = []
        if gptprompt is not None:
            for gptmessage in response:
                bot_responses.append(gptmessage)
        if bot_responses:
            await message.channel.send(bot_responses[0])

    elif len(words) == 1 and (words[0] == "анекдот"):
        await message.channel.send(vocabulary.random_anecdote())
    elif len(words) == 1 and (words[0] == "мем"):
        await message.channel.send(vocabulary.sp_rec_reaction_memequotes())
    elif len(words) == 1 and (words[0] == "ауф"):
        await message.channel.send(vocabulary.sp_rec_reaction_auf())
    elif len(words) == 1 and (words[0] == "афоризм"):
        await message.channel.send(vocabulary.random_response_aphorism())
    elif len(words) == 1 and (words[0] == "стих"):
        await message.channel.send(vocabulary.random_rhymes())

# Запускаем бота
client.run(TOKEN)
