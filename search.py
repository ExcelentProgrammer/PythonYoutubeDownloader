from pytube import YouTube
def video_info(link):
	try:
		video = YouTube(link)
		image_photo = video.thumbnail_url
		view = video.views
		second = video.length
		title = video.title
		publish_da = video.publish_date
		return {"image":image_photo,"view":view,"second":second,"title":title,"data":publish_da}
	except:
		print("Xato")