import time

global currentSection
global file

def interpreter(fille, split):
	
	if(split!=""):
		if(split.upper()=="WAY0" or split.upper()=="WAY 0")
			file=open(fille+"0.txt",r)
		elif(split.upper()=="WAY1" or split.upper()=="WAY 1")
			file=open(fille+"1.txt",r)
		else:
			input("ERROR")
			exit()
	else:
		file=open(fille, 'r')
	temp=open("temp.txt", 'wb')
	story=file.readlines()
	int=0
	while(True)
		line=story[int]
		if("INPUT" in line)
			foo=line.upper().replace("INPUT ", "")
			lsts=foo.split(',', 1)
			while(var==""):
				var=input(lsts.get[0])
			temp.seek(0, 2)
			temp.write(lsts.get[1]+"="+var)
			elif("SECTION:" in line.upper()):
			cu=line.replace("SECTION: ", "")
			cus=cu.replace(".", " ")
			currS=cus.split(' ', 1)
			chapter=currS.get[0]
			scene=currS.get[1]
			option=currS.get[2]
			print("CHAPTER "+chapter+", SCENE "+scene+", OPTION "+option)
			time.wait(3)
		elif("+ " and " +" in line):
			j=line.split(' + ', 1)
			j.pop(0)
			j.pop(1)
			jkl=j.get[0]
			jklm=temp.readline()
			while(jkl not in jklm)
				jklm=temp.readline()
				if(jklm="")
					input("ERROR! FILE COULD NOT BE READ!")
					exit()
			lolls=jklm.replace(jkl+"=", "")
			loolls=line.replace("+ "+jkl+" +", lolls)
			input(loolls)
		elif("SPLIT " in line):
			jklomp=line.replace("SPLIT ", "")
			jollo=jklomp.split(',' ,1)
			jol=jollo.get[0]
			llo=jollo.get[1]
			interpreter(jol, llo)
		elif("SKIP" in line):
			lomlom=line.replace("SKIP ", "")
			ple=Int(lomlom)
			file.seek(ple, 0)
		elif(line=="*START*"):
		elif(line=="*END*"):
			print()
		else:
			input(line)
		int=int+1
	input("THANKS FOR PLAYING")
	temp.close()
	file.close()
def start():
	print("21 DAYS")
	time.sleep(4)
	print("A GAME MADE BY WILL JOHNSON AND JONATHAN ZHANG")
	print("SPECIAL THANKS TO ERIC NIE")
	intro.part1()
	name = input("What's your name?")
	while name == "":
		name = input("What's your name?")
	intro.part2(name)
	ahead = response = input('Are you sure you want her to go ahead?')
	while ahead.upper() != 'YES' and ahead.upper() != 'Y' and ahead.upper() != 'NO' and ahead.upper() != 'N':
		ahead = response = input('Are you sure you want her to go ahead?')
	if (ahead.upper() == 'YES' or ahead.upper() == 'Y'):
		assert isinstance(name, object)
		s1o1.way0(name)
	if ahead.upper() == 'NO' or ahead.upper() == 'N':
		direction = s1o1.way1(name)
		while direction.contains().upper() != 'C' and direction.contains().upper() != 'S':
			direction = response = input("Which way will you go?")
		if direction.upper() == 'CITY' or direction.lower() == 'city':
			s2o1.way1()
		else:
			s2o1.way2()
class main():
	start()
