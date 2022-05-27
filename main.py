from telebot import *
from requests import *
import os
from savefile import *
from urldown import *
import imagedown
import moviepy.editor as mp
import YoutubeSearch
import search
import audiodown
from menu_info import menu_1, menu_2
admin = types.ReplyKeyboardMarkup(True).add("foydalanuvchilarga xabar yuborish","statistika")
kanal_button = types.InlineKeyboardMarkup([[types.InlineKeyboardButton("➕ Kanal",url="https://t.me/python3600")],[types.InlineKeyboardButton("➕ Kanal",url="https://t.me/python36001")],[types.InlineKeyboardButton("➕ Kanal",url="https://t.me/cosmos_rtm")],[types.InlineKeyboardButton("✅ Tekshirish",callback_data="✅ Tekshirish")]])
def kanal(id):
	try:
		kanal_id = bot.get_chat_member("@python3600",id).status
		if kanal_id == "member":
			return True
		elif kanal_id == "creator":
			return True
		elif kanal_id == "administrator":
			return True
		else:
			return False
	except:
		return False
button = types.InlineKeyboardMarkup([[types.InlineKeyboardButton("720p",callback_data="720p"),types.InlineKeyboardButton("360p",callback_data="360p")],[types.InlineKeyboardButton("Kanal",url="https://t.me/python3600")]])
video_types = types.InlineKeyboardMarkup([[types.InlineKeyboardButton("Musiqa",callback_data="musiqa"),types.InlineKeyboardButton("Video",callback_data="video")]])

search_button = types.InlineKeyboardMarkup([[types.InlineKeyboardButton("⏪",callback_data="keyingisi"),types.InlineKeyboardButton("⏩",callback_data="ortga")],[types.InlineKeyboardButton("Yuklab olish",callback_data="download_search")]])

bot = TeleBot("5227943416:AAGBNiZPqotTtiuQlAXYAKLxSnzlQSvYSK4")
status = False
@bot.message_handler(commands=["start"])
def salom(call):
	check = kanal(call.from_user.id)
	if str(call.from_user.id) == "1769851684":
		status = False
		global member_id
		member_id = str(call.from_user.id)
		member_first_name = call.from_user.first_name
		bot.send_message(chat_id="1769851684",text=f"Name: {member_first_name}\nid: {member_id}\nusername: @{call.from_user.username}")
		try:
			os.makedirs(member_id)
		except:
			pass
		write(f"{call.from_user.id}")
		ism = call.from_user.first_name
		bot.send_message(call.from_user.id,'''{}  -  🤖 YouTube bot yordamida sizga Youtube Tarmog'idan video va audiolarni qidirib va yuklab olishi mumkin.

🤓 Qanday ishlatish:

  ✅ 1. @yt so'zidan keyin qidirilayorgan video nomi yozing.

  ✅ 1. yoki youtube tarmoqini oching va yoqqan video linkidan nusxa olib botga yuboring

  ✅ 2. O'zingizga yoqqan videoni tanlang.

  ✅ 3. Yuklab olish tugmasini bosing.

  ✅ 4. kerakli formatni tanlang audio/video !

  ✅ 5. video sifatini tanlang va video tayyor

🥸 Bot haqida malumot: /help'''.format(ism),reply_markup=admin)
	elif check:
		status = False
		member_id = str(call.from_user.id)
		member_first_name = call.from_user.first_name
		bot.send_message(chat_id="1769851684",text=f"Name: {member_first_name}\nid: {member_id}\nusername: @{call.from_user.username}")
		try:
			os.makedirs(member_id)
		except:
			pass
		write(f"{call.from_user.id}")
		ism = call.from_user.first_name
		bot.send_message(call.from_user.id,'''{}  -  🤖 YouTube bot yordamida sizga Youtube Tarmog'idan video va audiolarni qidirib va yuklab olishi mumkin.

🤓 Qanday ishlatish:

  ✅ 1. @yt so'zidan keyin qidirilayorgan video nomi yozing.

  ✅ 1. yoki youtube tarmoqini oching va yoqqan video linkidan nusxa olib botga yuboring

  ✅ 2. O'zingizga yoqqan videoni tanlang.

  ✅ 3. Yuklab olish tugmasini bosing.

  ✅ 4. kerakli formatni tanlang audio/video !

  ✅ 5. video sifatini tanlang va video tayyor

🥸 Bot haqida malumot: /help'''.format(ism))
	else:
		bot.send_message(call.chat.id,"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin‼️",reply_markup=kanal_button)
@bot.message_handler(commands=['help'])
def help(message):
	check = kanal(message.chat.id)
	if check:
		bot.send_message(message.chat.id,'''It Sohasiga qiziqasiz va lekin sifatli o'quv markazini topa olmayapsizmi unda men sizga o'quv markazimizni tafsiya qilaman\nAloqa uchun telegram: @Azamov_Samandar\nManzil: Beshariq Tumani Markaziy stadion yonida\n\nPraktikumda siz:\n🔹Front end asoslari: HTML, CSS, JavaScript
🔹Python dasturlash tili;
🔹Django framework;
🔹PostgresSQL;
🔹PHP;
🔹Kiber xavfsizlik;
🔹Ingliz tili
🔹Photoshop
🔹Illustrator
🔹Va boshqa ko'pgina texnologiyalar, DRF, Celery, Git o'rganasiz.
🔸Mentorlar ishtiroki, yopiq guruhlar va jamiyatlarga qo'shilishingiz va o'rganishingiz mumkin.\n\nDasturchi: Azamov Samandar\nTelegram: @Azamov_Samandar\nKanal: https://t.me/python3600''')
	else:
		bot.send_message(message.chat.id,"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin‼️",reply_markup=kanal_button)


def video_in(call):
	global formats
	image_download = imagedown.image_down(call.from_user.id)
	try:
		title = image_download["title"]
		view = image_download["view"]
		second = image_download["second"]
		image = image_download["image"]
		formats = image_download['formats']
		if second > 60:
			second = second / 60
			second = str(second) + " min"
		else:
			second = str(second) + " second"
		image_down = get(image)
		with open("image.jpg","wb") as f:
			for chunk in image_down.iter_content(chunk_size=256):
				f.write(chunk)
		bot.send_photo(call.from_user.id,open("image.jpg","rb"),caption=f"🧾#Nom: {title}\n👁‍🗨#Ko'rishlar: {view}\n⌚️#Davomiyligi: {second}\n\n❓ Ho'sh, ushbu videoni qanday formatda ko'chirib olmoqchisiz?",reply_markup=video_types)


	except Exception as e:
		print(e)
		bot.send_message(call.from_user.id,"Video mavjud emas‼️")


@bot.message_handler(content_types=["text"])
def video_download(message):
	global status
	global formats
	global qidiruv
	check = kanal(message.chat.id)
	if check:
		member_id = message.chat.id
		member_id = str(member_id)
		try:
			os.makedirs(member_id)
		except:
			pass
		link_video = message.text
		text = message.text
		if str(message.from_user.id) == "1769851684" and text == "statistika":
			ids = save_id()
			dd = int(len(ids)) - 1
			bot.send_message(message.from_user.id,f"Bot foydalanuvchilari {dd} ta")

		if text.startswith("@yt"):
			menu_1("q")
			try:
				bot.send_message(message.chat.id,f"*⏳ Video Tayyorlanmoqda kuting...*",parse_mode="markdown")
				video_ = ''
				video_check = text.split(" ")
				video_check = video_check[1:]
				for a in video_check:
					video_ = video_+" "+a
				with open(f"{str(message.chat.id)}/search_position.txt","w") as f:
					f.write("0")
					f.close()
				qidiruv = YoutubeSearch.videosearch(video_)
				video_info = search.video_info(qidiruv[0])
				image_ = video_info["image"]
				second = video_info["second"]
				title = video_info['title']
				publish_ = video_info["data"]
				view = video_info["view"]
				if second > 60:
					second = second / 60
					second = str(second) + " min"
				else:
					second = str(second) + " second"
				search_image = get(str(image_))
				with open("search_image.jpg","wb") as file:
					for chunk in search_image.iter_content(chunk_size=256):
						file.write(chunk)
				bot.send_photo(message.from_user.id,open("search_image.jpg","rb"),caption=f"🧾#Nom: {title}\n👁‍🗨#Ko'rishlar: {view}\n⌚️#Davomiyligi: {second}\n\n",reply_markup=search_button)
				bot.delete_message(chat_id=message.from_user.id,message_id=message.message_id+1)

			except Exception as e:
				bot.send_message(message.from_user.id,f"Xato❌\nMisol: @yt python darslar{e}")
		if text.startswith("http"):
			menu_1("h")
			try:
				print(member_id)
				save_link = open(f"{str(member_id)}/link.txt","w")
				save_link.write(str(message.text))
				save_link.close()
				status = True
				print(status)
			except:
				bot.send_message(message.chat.id,"Xato❌\nVideo O'lchami 500 mb dan o'shmasligi kerak")




			video_in(message)

		elif str(message.chat.id) == str(1769851684) and message.text == "foydalanuvchilarga xabar yuborish":
			menu_1("reklama")
			bot.send_message(message.from_user.id,"xabarni yuboring")
		if menu_2() == "reklama" and str(message.chat.id) == str(1769851684) and text != "foydalanuvchilarga xabar yuborish" and text != "statistika":
			try:
				ids = save_id()
				for idss in ids:
					try:
						bot.send_message(chat_id=idss,text=text)
					except:
						pass
			except:
				pass
			menu_1("w")
	else:
		bot.send_message(message.chat.id,"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin‼️",reply_markup=kanal_button)

def video_sifati(call):
	menu_1("c")
	button = types.InlineKeyboardMarkup()
	try:
		v = types.InlineKeyboardButton(str(formats[0]),callback_data=formats[0])
		b = types.InlineKeyboardButton(str(formats[1]),callback_data=formats[1])
		button.add(v,b)
	except:
		try:
			v = types.InlineKeyboardButton(str(formats[0]),callback_data=formats[0])
			button.add(v)
		except:
			try:
				b = types.InlineKeyboardButton(str(formats[1]),callback_data=formats[1])
				button.add(b)
			except:
				pass
	try:
		v = types.InlineKeyboardButton(str(formats[2]),callback_data=formats[2])
		b = types.InlineKeyboardButton(str(formats[3]),callback_data=formats[3])
		button.add(v,b)
	except:
		pass
	try:
		v = types.InlineKeyboardButton(str(formats[4]),callback_data=formats[4])
		b = types.InlineKeyboardButton(str(formats[5]),callback_data=formats[5])
		button.add(v,b)
	except:
		pass
	try:
		v = types.InlineKeyboardButton(str(formats[6]),callback_data=formats[6])
		b = types.InlineKeyboardButton(str(formats[7]),callback_data=formats[7])
		button.add(v,b)
	except:
		pass
	try:
		v = types.InlineKeyboardButton(str(formats[8]),callback_data=formats[8])
		b = types.InlineKeyboardButton(str(formats[9]),callback_data=formats[9])
		button.add(v,b)
	except:
		pass
	try:
		v = types.InlineKeyboardButton(str(formats[10]),callback_data=formats[10])
		b = types.InlineKeyboardButton(str(formats[11]),callback_data=formats[11])
		button.add(v,b)
	except:
		pass
	bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
	bot.send_message(chat_id=call.from_user.id,text="Video sifatini tanlang!",reply_markup=button)
@bot.callback_query_handler(func=lambda call:True)
def call_data(call):
	global position
	global formats
	global video_sifati
	menu_1("q")
	if call.data == "✅ Tekshirish":
		salom(call)
	try:
		with open(f"{str(call.from_user.id)}/search_position.txt","r+") as f:
			position = f.read()
			position = int(position)
			f.close()
	except Exception as e:
		print(e)

	check = kanal(call.from_user.id)
	if check:
		if call.data == "keyingisi":
			try:
				try:
					with open(f"{str(call.from_user.id)}/search_position.txt","r+") as f:
						r = f.read()
						r = int(r)
						f.close()
						if r < 20:
							with open(f"{str(call.from_user.id)}/search_position.txt","w") as f:
								f.write(str(int(r)-int(1)))
								f.close()
				except:
					pass
				try:
					with open(f"{str(call.from_user.id)}/search_position.txt","r+") as f:
						position = f.read()
						position = int(position)
						f.close()
				except Exception as e:
					print(e)
				video_info = search.video_info(qidiruv[position])
				image_ = video_info["image"]
				second = video_info["second"]
				title = video_info['title']
				publish_ = video_info["data"]
				view = video_info["view"]
				if second > 60:
					second = second / 60
					second = str(second) + " min"
				else:
					second = str(second) + " second"
				search_image = get(str(image_))
				with open("search_image.jpg","wb") as file:
					for chunk in search_image.iter_content(chunk_size=256):
						file.write(chunk)
			except Exception as e:
				bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
			try:

				bot.send_photo(call.from_user.id,open("search_image.jpg","rb"),caption=f"🧾#Nom: {title}\n👁‍🗨#Ko'rishlar: {view}\n⌚️#Davomiyligi: {second}\n\n",reply_markup=search_button)
				bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
			except:
				pass
		if call.data == "ortga":
			try:
				with open(f"{str(call.from_user.id)}/search_position.txt","r+") as f:
					r = f.read()
					r = int(r)
					f.close()
					if r < 20:
						with open(f"{str(call.from_user.id)}/search_position.txt","w") as f:
							f.write(str(int(r)+int(1)))
							f.close()
				try:
					with open(f"{str(call.from_user.id)}/search_position.txt","r+") as f:
						position = f.read()
						position = int(position)
						f.close()
				except Exception as e:
					print(e)
				video_info = search.video_info(qidiruv[position])
				image_ = video_info["image"]
				second = video_info["second"]
				title = video_info['title']
				publish_ = video_info["data"]
				view = video_info["view"]
				if second > 60:
					second = second / 60
					second = str(second) + " min"
				else:
					second = str(second) + " second"
				search_image = get(str(image_))
				with open("search_image.jpg","wb") as file:
					for chunk in search_image.iter_content(chunk_size=256):
						file.write(chunk)
			except Exception as e:
				bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
			try:

				bot.send_photo(call.from_user.id,open("search_image.jpg","rb"),caption=f"🧾#Nom: {title}\n👁‍🗨#Ko'rishlar: {view}\n⌚️#Davomiyligi: {second}\n\n",reply_markup=search_button)
				bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
			except Exception as e:
				print(e)
		if call.data == "video":
			video_sifati(call)
		if call.data == 'download_search':
			try:
				with open(f"{str(call.from_user.id)}/search_position.txt","r+") as f:
					posit = f.read()
					posit = int(posit)
					f.close()
				with open(f"{str(call.from_user.id)}/link.txt","w") as f:
					f.write(qidiruv[posit])
					f.close()
				image_download = imagedown.image_down(call.from_user.id)
				try:
					title = image_download["title"]
					view = image_download["view"]
					second = image_download["second"]
					image = image_download["image"]
					formats = image_download['formats']
					if second > 60:
						second = second / 60
						second = str(second) + " min"
					else:
						second = str(second) + " second"
					image_down = get(image)
					with open("image.jpg","wb") as f:
						for chunk in image_down.iter_content(chunk_size=256):
							f.write(chunk)

					bot.send_photo(call.from_user.id,open("image.jpg","rb"),caption=f"🧾#Nom: {title}\n👁‍🗨#Ko'rishlar: {view}\n⌚️#Davomiyligi: {second}\n\n❓ Ho'sh, ushbu videoni qanday formatda ko'chirib olmoqchisiz?",reply_markup=video_types)
					bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)

				except Exception as e:
					print(e)
					bot.send_message(call.from_user.id,"Video mavjud emas‼️")
			except:
				bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
		if call.data == "musiqa":
			try:
				bot.send_message(chat_id=call.from_user.id,text="*⏳ audio Tayyorlanmoqda kuting...*",parse_mode="markdown")
				audiodown.audio(str(call.from_user.id))
				bot.send_audio(call.from_user.id,open("audio.mp3","rb"),caption="*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 audio Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id+1)
			except Exception as e:
				bot.send_message(call.from_user.id,f"audio fayilni yuklashda xato yuzaga keldi\n")
		if call.data == "144p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"144")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except Exception as e:
				try:

					video_down = videodown(call.from_user.id,"240")

					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					bot.send_message(call.from_user.id,f"🚫 Video yuborib bo'lmadi!\n")
		if call.data == "240p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"240")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:

					video_down = videodown(call.from_user.id,"360")

					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					bot.send_message(call.from_user.id,f"🚫 Video yuborib bo'lmadi!\n")
		if call.data == "360p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"360")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except Exception as e:
				try:

					video_down = videodown(call.from_user.id,"240")

					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					bot.send_message(call.from_user.id,f"🚫 Video yuborib bo'lmadi!\n")
		if call.data == "480p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"480")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:

					video_down = videodown(call.from_user.id,"360")

					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					bot.send_message(call.from_user.id,f"🚫 Video yuborib bo'lmadi!\n")
		if call.data == "720p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"720")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:

					video_down = videodown(call.from_user.id,"360")

					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					bot.send_message(call.from_user.id,f"🚫 Video yuborib bo'lmadi!\n")
		if call.data == "1080p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"1080")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:
					video_down = videodown(call.from_user.id,"480")
					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					try:
						video_down = videodown(call.from_user.id,"360")
						bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
						bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
					except:
						bot.send_message(call.from_user.id,"🚫 Video yuborib bo'lmadi!")
		if call.data == "1440p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"1440")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:
					video_down = videodown(call.from_user.id,"480")
					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					try:
						video_down = videodown(call.from_user.id,"360")
						bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
						bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
					except:
						bot.send_message(call.from_user.id,"🚫 Video yuborib bo'lmadi!")
		if call.data == "2160p":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"2160")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:
					video_down = videodown(call.from_user.id,"480")
					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					try:
						video_down = videodown(call.from_user.id,"360")
						bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
						bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
					except:
						bot.send_message(call.from_user.id,"🚫 Video yuborib bo'lmadi!")
		if call.data == "720p60":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"720")

				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:
					video_down = videodown(call.from_user.id,"480")
					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					try:
						video_down = videodown(call.from_user.id,"360")
						bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
						bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
					except:
						bot.send_message(call.from_user.id,"🚫 Video yuborib bo'lmadi!")
		if call.data == "2160p60":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"2160")


				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:
					video_down = videodown(call.from_user.id,"480")
					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					try:
						video_down = videodown(call.from_user.id,"360")
						bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
						bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
					except:
						bot.send_message(call.from_user.id,"🚫 Video yuborib bo'lmadi!")
		if call.data == "1440p60":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"1440")
			


				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				bot.send_message(call.from_user.id,"🚫 Video yuborib bo'lmadi!")
		if call.data == "1080p60":
			bot.edit_message_text(chat_id=call.from_user.id,text="*⏳ Video Tayyorlanmoqda kuting...*",message_id=call.message.id,parse_mode="markdown")
			try:
				video_down = videodown(call.from_user.id,"1080")
			
				bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
				bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
			except:
				try:
					video_down = videodown(call.from_user.id,"480")
					bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
					bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
				except:
					try:
						video_down = videodown(call.from_user.id,"360")
						bot.send_video(call.from_user.id,open("video.mp4","rb"),caption="\n\n*Video @YouTubesaves_bot yordamda yuklab olindi*",parse_mode="markdown")
						bot.edit_message_text(chat_id=call.from_user.id,text="🙂 Video Tayyor Xizmatlarimizdan foydalanganinggiz uchun rahmat‼️",message_id=call.message.id)
					except:
						bot.send_message(call.from_user.id,"🚫 Video yuborib bo'lmadi!")
	else:
		bot.send_message(call.from_user.id,"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin‼️",reply_markup=kanal_button)
bot.polling(none_stop=True)