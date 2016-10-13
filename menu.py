def savegame(file, section):
	file=open("save.txt", "wb")
	file.write(file)
	file.seek(1,0)
	file.write(section)
	file.close()
def loadsave(savename):
	if("Y" in input("Would you like to load a game? (Y/N)").upper()):
		saveInfo
		os.path.exists("/Saves/autosave.txt")
		file=open("/Saves/save"+intg,"r")
		saves.add()
		intg=1
		for i in range(0, 4):
			if(os.path.exists("/Saves/save"+intg+".txt")==True):
				file=open("/Saves/save"+intg+".txt","r")
				save=file.readlines()
				saveInfo.add(save[1])
			else:
				saves.add("(empty)")
			intg+=1
		SaveFileChoices="""
Options:
	0. AutoSave-"""+saveinfo[0]+"""
	1. Save1-"""+saveInfo[1]+"""
	2. Save2-"""+saveInfo[2]+"""
	3. Save3-"""+saveInfo[3]+"""
	4. Save4-"""+saveInfo[4]+"""
	5. Exit"""
		file=open(savename+".txt", "r")
		listthing=file.readlines()
		currentfile=listthing[0]
		section=listthing[1]
		interpreter(currentfile,"", True,section)	
	else:
		print("Okay. I see you don't want to load a save. I respect your decision. :(")
def menu():
	input("This is the Menu.")
