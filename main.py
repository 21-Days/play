import time

global currentSection
global file

def read():
	temp=open("temp.txt", 'wb')
	file=open("storyline.txt", 'r')
	story=file.readlines()
	int=0
	while(True)
		line=story[int]
		if("INPUT" in line)
			foo=line.replace("INPUT ", "")
			lsts=foo.split(',', 1)
			while(var==""):
				var=input(lsts.get[0])
			temp.write(lsts.get[1]+"="+var)
		elif("SECTION:" in line):
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
			while(!jkl in jklm)
				jklm=temp.readline()
			lolls=jklm.replace(jkl+"=", "")
			loolls=line.replace("+ "+jkl+" +", lolls)
			input(loolls)
		elif("SPLIT " in line):
			k=line.replace("SPLIT ", "")
			f=open(k,'r')
			
		elif():
		else:
			input(line)
		int=int+1
	return "done"
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
