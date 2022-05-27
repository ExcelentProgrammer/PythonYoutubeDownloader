from pytube import YouTube, Stream
import time

link = "https://www.youtube.com/watch?v=QC8iQqtG0hg"
video = YouTube(link).streams.filter(res="144p").first()
size = video.filesize
a = int(size/1000000)
if a > 0:
	print("ishladi")
if a < 0:
	print("sss")


