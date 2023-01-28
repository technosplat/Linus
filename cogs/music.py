import random
import discord
from discord.ext import commands
from discord import app_commands
from discord import voice_client
from youtube_dl import YoutubeDL
from requests import get
from youtube_search import YoutubeSearch
from pytube import YouTube
import os
from youtube_search import YoutubeSearch
class music(commands.Cog):
    def __init__(self, bot: commands.bot) -> None:
        self.bot = bot
    
    
        

    @app_commands.command(name='play', description='Plays a song!')
    async def play(self, interaction: discord.Interaction, search: str):
        if interaction.user.voice:
            results = YoutubeSearch(search_terms=search, max_results=10).to_dict()
            url = 'https://www.youtube.com/' + results[1]['url_suffix']

            yt = YouTube(str(url))
            
            video = yt.streams.filter(only_audio=True).first()
            
            destination = r'C:\Users\Nathan\Desktop\The coder\Linus\music'
            
            # download the file
            out_file = video.download(output_path=destination)
            
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        

            # play the file
            VoiceClient = await interaction.user.voice.channel.connect()
            media = new_file
            source = discord.FFmpegPCMAudio(source=media)
            
            
            VoiceClient.play(source=source)
            await interaction.response.send_message('Now playing: ' + yt.title)
            VoiceClient.stop()
            await VoiceClient.disconnect()
        else:
            await interaction.response.send_message('You must be in a voice channel to use this command. ')   
        
        

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(music(bot))