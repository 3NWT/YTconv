from __future__ import unicode_literals
import youtube_dl

urllinkshit = input("Please enter url: ")        

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([(urllinkshit)])
    quit()

