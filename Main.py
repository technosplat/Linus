# bot.py
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import aiohttp
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
class Linus(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = '!', intents=discord.Intents.all(), application_id=874136887252639775)
        
        

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        extensions = [f"cogs.tantalized", f"cogs.quotes", f"cogs.music"]
        for ext in extensions:
            await self.load_extension(ext)
        
        await bot.tree.sync()
    
    async def on_ready(self):
        print("Linus is now online!")


bot = Linus()


@bot.command()
async def reload(ctx):
    await Linus().setup_hook()
    print('cogs reloaded')
bot.run(TOKEN)