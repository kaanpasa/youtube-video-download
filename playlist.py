from pytube import YouTube
from pytube import Playlist

p = Playlist('PLAYLIST LINK')
PlayListLinks = p.video_urls
print(f'Downloading: {p.title}')

for i,link in enumerate(PlayListLinks):
    yt = YouTube(link)
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    d_video.download('DOWNLOAD PATH(Leave empty for current directory)')
    print(i+1, ' Video is Downloaded.')