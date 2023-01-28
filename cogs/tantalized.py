import random
import discord
from discord.ext import commands
from discord import app_commands
from discord import voice_client
import time
class tantalized(commands.Cog):
    def __init__(self, bot: commands.bot) -> None:
        self.bot = bot
    
    @app_commands.command(name='tantalized', description='im so funny im literally the funniest please tell me how funny i am')
    async def tantalized(self, interaction: discord.Interaction):
        if interaction.user.voice:

            VoiceClient = await interaction.user.voice.channel.connect()
            media = r'C:\Users\Nathan\Desktop\The coder\Linus\Media.mp3'
            source = discord.FFmpegPCMAudio(source=media)
            
            VoiceClient.play(source=source)
            await interaction.response.send_message('Tantalized!')
            time.sleep(16)
            VoiceClient.stop()
            await VoiceClient.disconnect()
        else:
            await interaction.response.send_message('You must be in a voice channel to use this command. ')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(tantalized(bot))
