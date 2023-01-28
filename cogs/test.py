from youtube_dl import YoutubeDL
from requests import get
from youtube_search import YoutubeSearch
from pytube import YouTube
import os
search = 'despacito'
results = YoutubeSearch(search_terms=search, max_results=10).to_dict()
url = 'https://www.youtube.com/' + results[1]['url_suffix']

yt = YouTube(str(url))
  
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
destination = r'C:\Users\Nathan\Desktop\The coder\Linus\music'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")