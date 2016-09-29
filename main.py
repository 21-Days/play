import time
import intro
from Chapter1 import s1o1
from Chapter1 import s2o1
from Chapter1 import s3o1

def reader():


def start():
    print("21 DAYS")
    time.sleep(4)
    print("A GAME MADE BY WILL JOHNSON AND JONATHAN ZHANG")
    print("SPECIAL THANKS TO ERIC NIE")
    time.sleep(3)
    print("CHAPTER 1, SCENE 1, OPTION 0")
    time.sleep(3)
    intro.part1()
    name = response = input("What's your name?")
    while name == "":
        name = response = input("What's your name?")
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
