import yt_dlp

url = "https://www.youtube.com/watch?v=yeMQq_GoMZs"

ydl_opts = {
    'format':'best',
    'outtmpl':'inputs/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])