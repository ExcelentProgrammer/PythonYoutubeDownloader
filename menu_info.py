def menu_1(x):
	with open("menu_info.txt","w") as file:
		file.write(x)
def menu_2():
	with open("menu_info.txt","r+") as file:
		a = file.read()
		a = str(a)
		return a