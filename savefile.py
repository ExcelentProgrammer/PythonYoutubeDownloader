def write(x):
	print("s")
	try:
		a=open("data.txt","a")
		print("file o'childi")
		a.close()
	except:
		print("file mavjud")
	v = open("data.txt","r+")
	if not x in v.read():
		v.write(" "+x)
def save_id():
	id = open("data.txt","r+")
	ids = id.readline()
	ids = ids.split(" ")
	return ids
