#author: hpgross
#this is a simple script to give you a random setup for FFXII: The Zodiac Age
#it allows you to say whether or not to specify each character and randomly assign job pairs for 1 to 6 characters
#there's really no error checking, so don't input other stuff besides "Y" or "N" for the first question and a number from 1 to 6 for the second question

import random
jobs = ["Uhlan","Bushi","Machinist","Shikari","White Mage","Red Battlemage","Monk","Foebreaker","Archer","Knight","Time Battlemage","Black Mage"]
characters = ["Vaan","Penelo","Balthier","Fran","Ashe","Basch"]

def randomList(a): 
	b = [] 
	for i in range(len(a)): 
		element = random.choice(a) 
		a.remove(element) 
		b.append(element) 
	return b

jobs = randomList(jobs)
characters = randomList(characters)

characterOption = input("Assign specific character: Y/N? ");
numberCharacters = input("Enter a number of characters from 1 to 6. ");

if characterOption.upper() == "Y":
	for i in range(0,int(numberCharacters)):
		print (characters[i] + " is assigned the jobs " + jobs[2*i] + " and " + jobs[2*i + 1])
elif characterOption.upper() == "N":
	for i in range(0,int(numberCharacters)):
		print ("Character " + str(i) + " is assigned the jobs " + jobs[2*i] + " and " + jobs[2*i + 1])
else:
	exit
