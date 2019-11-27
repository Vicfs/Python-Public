import discord
import os
import yaml
import random

from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from os import system

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
BOT_PREFIX = "!"
# content from .yaml to commands_dict
with open("commands.yaml", encoding="utf8") as infile:
    commands_dict = yaml.safe_load(infile)

bot = commands.Bot(command_prefix=BOT_PREFIX)
# pre-defined message
async def send_callback(ctx):
    if ctx.author == bot.user:
        return
    await ctx.channel.send(commands_dict[ctx.command.qualified_name]["text"])
# random message within choices
async def random_send_callback(ctx):
    if ctx.author == bot.user:
        return
    await ctx.channel.send(random.choice(commands_dict[ctx.command.qualified_name]["choices"]))
# plays mp3 file (same name as ctx)
async def audio_callback(ctx):
    if ctx.message.author.voice == None:
        return
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")
    voice = get(bot.voice_clients, guild=ctx.guild)

    voice.play(
        discord.FFmpegPCMAudio(
            commands_dict[ctx.command.qualified_name]["file"]),
            after=lambda e: print("finished playing")
    )
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.3
    while voice.is_playing() == True:
        continue
    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
    if ctx.author == bot.user:
        return

# build all commands from dict & add to bot
for command_name in commands_dict:
    if commands_dict[command_name]["type"] == "send":
        func = send_callback
    elif commands_dict[command_name]["type"] == "audio":
        func = audio_callback
    elif commands_dict[command_name]["type"] == "random_choice":
        func = random_send_callback
    else:
        break

    c = commands.Command(
            func,
            name=command_name,
            help=commands_dict[command_name]["help"]
    )
    bot.add_command(c)

# shows when the bot is connected to discord
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


bot.run(TOKEN)