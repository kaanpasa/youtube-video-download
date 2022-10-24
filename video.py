from pytube import Youtube
yt = YouTube('VIDEO LINK')
print(f'Downloading: {yt.title}')
stream = yt.streams.get_by_itag(22)#For 720p
stream.download()
print('Video is downloaded.')