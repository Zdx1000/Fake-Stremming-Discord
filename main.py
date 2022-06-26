import discord
from discord.ext import commands, tasks
import asyncio
import time

TOKEN = "Coloque seu Token aqui"
PREFIXO = "!"

intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
  change_status.star()
  print(f"{bot.user} | {bot.user.id} | {time.strftime("%H:%M:%S")}")
  await bot.change_presence(
    activity=discord.Activity(type=discord.ActivityType.streaming, name"Black soy",
                              details=f"🌐 Main.py a base de tudo ⏳{time.strftime("%H:%M:%S")}",
                              url="https://www.twitch.tv/alanzoka"))
@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=discord.Streaming(name="Streaming 1", url="https://www.twitch.tv/alanzoka"))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Streaming(name="Streaming 2", url="https://www.twitch.tv/alanzoka"))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Streaming(name="Streaming 3", url="https://www.twitch.tv/alanzoka"))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Streaming(name="Streaming 4", url="https://www.twitch.tv/alanzoka"))
  await asyncio.sleep(5)
  
  bot.run(TOKEN, bot=False)
