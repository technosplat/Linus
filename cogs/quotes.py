import random
import discord
from discord.ext import commands
from discord import app_commands
from discord import voice_client
import json

class quotes(commands.Cog):
    def __init__(self, bot: commands.bot) -> None:
        self.bot = bot

    @app_commands.command(name='quote', description='quotebook for nbt/clownmotel')

    async def quotes(self, interaction: discord.Interaction):
        if interaction.guild_id == 748953344973996172:
            path = r'C:\Users\Nathan\Desktop\The coder\Linus\quotes_clown.json'
        else:
            path = r'C:\Users\Nathan\Desktop\The coder\Linus\quotes.json'
        
        with open(path, 'r') as j:
            data = json.loads(j.read())
        quote = random.choice(data)

        await interaction.response.send_message(quote)

    @app_commands.command(name='quoteadd', description='Add a quote to the quote book')

    async def quoteadd(self, interaction: discord.Interaction, newquote: str):
        if interaction.guild_id == 748953344973996172:
            path = r'C:\Users\Nathan\Desktop\The coder\Linus\quotes_clown.json'
        else:
            path = r'C:\Users\Nathan\Desktop\The coder\Linus\quotes.json'

        with open(path, 'r') as j:
            data = json.loads(j.read())
        data.append(newquote)
        with open(path, "w") as outfile:
            json.dump(data, outfile)

        await interaction.response.send_message("Added the quote: " + newquote)




async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(quotes(bot))