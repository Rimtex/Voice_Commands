import os
import discord
from discord.ext import commands
from concurrent.futures import ThreadPoolExecutor
from bot_config import *

from setup_config import create_shortcut
create_shortcut("testbot", os.path.abspath(__file__))

intents = discord.Intents.default()
intents.messages = True
intents.guild_messages = True
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channels = bot.get_all_channels()  # для всех каналов
    for channel in channels:
        if channel.type == discord.ChannelType.text:
            print(f'Connected to text channel: {channel}')

    # Устанавливаем статус "играет в:"
    await bot.change_presence(activity=discord.Game(default_role[:128]))

    # вывод сохраненного чата в консоль
    if not is_file_empty('messagesgpt.txt'):
        with open('messagesgpt.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            for key, value in item.items():
                print(f'"{key}": "{value}"')
            print()       

@bot.command(name='role')
async def role(ctx, *, role_content):
    if ctx.guild:
        await ctx.message.delete()
        
    with open("messagesgpt.txt", "w") as file:
        file.truncate(0)
    
    role_message = [{"role": "user", "content": f"!Твоя роль: {role_content}!"}]
    
    with open('gptrole.txt', 'w', encoding='utf-8') as filemessagesgpt:
        filemessagesgpt.write(f"{role_content}")   
    
    save_messages(role_message)
    default_role = read_default_role('gptrole.txt')
    
    await bot.change_presence(activity=discord.Game(default_role[:128]))















with open('token.txt', 'r') as token_file:  # токен Discord скопировать в token.txt
    token = token_file.readline()
bot.run(token)  # Запускаем бота

