import yt_dlp

url = input("YouTubeのURLを入力: ")

ydl_opts = {
    'format':'best',
    'outtmpl':'inputs/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
