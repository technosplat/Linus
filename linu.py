# bot.py
import random
import discord
from discord.ext import commands
from discord import app_commands
from discord import voice_client
import os
import cv2
import time
import json
import numpy as np
from numba import jit
import aiohttp
TOKEN = 'ODc0MTM2ODg3MjUyNjM5Nzc1.GOhlUR.0ON5Xx2Gq8wsdlEkpLMXecVE2Nesh2_xRPis9I'



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