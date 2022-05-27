from pytube import YouTube
from pprint import pprint
def image_down(member_id):
	global formats
	formats = []
	try:
		image_link = open(f"{member_id}/link.txt","r+")
		link = image_link.read()
		link = str(link)
		image_link.close()
	except:
		pass
	try:
		video = YouTube(link)
		image_photo = video.thumbnail_url
		view = video.views
		second = video.length
		title = video.title
		publish_da = video.publish_date
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][1]["qualityLabel"]

			formats.append(s)
		except Exception as e:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][4]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][7]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][10]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][13]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][16]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][19]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][22]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][25]["qualityLabel"]

			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][28]["qualityLabel"]
			print(s)
			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][31]["qualityLabel"]
			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][34]["qualityLabel"]
			formats.append(s)
		except:
			pass
		try:
			s = video.vid_info["streamingData"]["adaptiveFormats"][37]["qualityLabel"]
			formats.append(s)
		except:
			pass
		print(formats)
		try:
			if len(formats) == 0:
				formats.append("360p")
				formats.append("144p")
			forr = []
			for f in formats:
				try:
					e = int(video.streams.filter(res=f).first().filesize/1000000)
					if e < 300:
						forr.append(f)
				except:
					print(1)
			print(forr)
			return {"image":image_photo,"title":title,"view":view,"second":second,"formats":forr,"data":publish_da}
		except Exception as e:
			print(e)
	except Exception as e:
		print(e)
