
from requests import *
import requests
from time import *
from pytube import YouTube
import smdo
def videodown(member_id,format):
	print(format)
	global i
	try:
		link_file = open(f"{str(member_id)}/link.txt","r+")
		link = link_file.read()
		link = str(link)
		print(link)
	except:
		pass
	format = str(format) + "p"
	v = YouTube(link)
	try:
		a = v.streams.filter(res=format).first()
		size = int(a.filesize/1000000)
		if size > 300:
			return size  
		elif size <= 300:
			a.download(output_path="",filename='video.mp4')
			return "t"
	except:
		try:

			a = v.streams.filter(res="480p").first()
			size = int(a.filesize/1000000)
			if size > 300:
				return size  
			elif size <= 300:
				a.download(output_path="",filename='video.mp4')
				return "t"
		except:
			try:
				a = v.streams.filter(res="360p").first()
				size = int(a.filesize/1000000)
				if size > 300:
					return size  
				elif size <= 300:
					a.download(output_path="",filename='video.mp4')		
					return "t"	
			except:
				a = v.streams.filter(res="240p").first()
				size = int(a.filesize/1000000)
				if size > 300:
					return size  
				elif size <= 300:
					a.download(output_path="",filename='video.mp4')
					return "t"