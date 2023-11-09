from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=53rFzBGA41k&list=PL-wEE8VmWaJ3BoPk-jxOrjOp711iP_Oqg&pp=iAQB')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
	try:
		video.streams.filter(res="720p").first().download()
	except:
		pass
	#video.streams.filter(res="720p").first().download()
"""
from pytube import Playlist
#yt.streams.filter(res="720p").first().download()
playlist = Playlist('https://www.youtube.com/watch?v=58PpYacL-VQ&list=UUd6MoB9NC6uYN2grvUNT-Zg')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
playlist.filter(res="720p").download_all()
"""

