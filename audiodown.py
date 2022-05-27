from pytube import YouTube
def audio(member_id):
	global i
	try:
		link_file = open(f"{str(member_id)}/link.txt","r+")
		link = link_file.read()
		link = str(link)
		print(link)
	except:
		pass
	v = YouTube(link)

	v = v.streams.filter(only_audio=True).first().download(output_path="",filename='audio.mp3')
