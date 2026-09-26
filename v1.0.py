import os
from yt_dlp import YoutubeDL

folder = "downloads"
f = 0

n = input('Which language? ru/en:')
if n == 'ru':
    video = input("Ссылка на видео(Pornohub): ")
else:
    video = input('Link to video(Pornohub): ')
    f += 1

os.makedirs(folder, exist_ok = True)

options = {
    "format": "bestvideo*+bestaudio/best",
    "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
    "noplaylist": True,
    "extractor_args": {"generic": {"impersonate": ["chrome:windows-10"]}},
    "referer": "https://pornhub.com",
    "nocheckcertificate": True,
    "ignoreerrors": True,
}




with YoutubeDL(options) as ydl:
    ydl.download([video])

if f == 0:
    print('Готово!')
else:
    print('Ready!')
