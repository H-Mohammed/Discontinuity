'''
Title: Discontinuity
Author: Haamid Mohammed
Date Created: 2018/09/21
'''
import sys
import random
import time
import timeit
import pprint
import cursor

#cursor.hide()
start = 0
pick2 = 0
pick3 = 0
choice1 = 0
choice2 = 0
choice3 = 0
choice4 = 0
choice5 = 0

def ps(str):
	for letter in str:
			sys.stdout.write(letter)
			sys.stdout.flush()
			time.sleep(0.01)
	print("")

def intro():
	print("""
██████╗ ██╗███████╗ ██████╗ ██████╗ ███╗   ██╗████████╗██╗███╗   ██╗██╗   ██╗██╗████████╗██╗   ██╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██║   ██║██║╚══██╔══╝╚██╗ ██╔╝
██║  ██║██║███████╗██║     ██║   ██║██╔██╗ ██║   ██║   ██║██╔██╗ ██║██║   ██║██║   ██║    ╚████╔╝ 
██║  ██║██║╚════██║██║     ██║   ██║██║╚██╗██║   ██║   ██║██║╚██╗██║██║   ██║██║   ██║     ╚██╔╝  
██████╔╝██║███████║╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║██║ ╚████║╚██████╔╝██║   ██║      ██║   
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝   ╚═╝      ╚═╝   
""")
	print("This game is a choose you own adventure.")
	print("You have to make many different choices and your outcome will change depending on the choices you make.")
	print("There are many ways to play the game but there are good outcomes as well as bad ones")
	print("Lets see how you play the game.")
	start = input("Press enter to begin")
	

def R1(): # Room 1, Where you begin
	global choice1
    ps("You wake up and u see a spear next to you, and you hear a voice, it says, 'Complete the sword and beat the boss before time runs out'.")
    ps("You don't know  what that means, so you look around.")
    ps("You see a forest and an open field in front of you, in the open field you see some creatures that you have never seen before and behind you there is a mountain that is too tall and steep to climb.")
    ps("Now you have to make a choice, go to the forest, go to the open field, or try to climb the mountain.")
    choice1 = input("Forest, open field, or mountain? ")
    



def R2(): # Room 2, The forest
	global pick2
	global choice2
	global choice3
	global choice4
	global pick3
	ps("The forest is heavily dense so you cant see the sky from the bottom and there seem to be some type of bioluminescent flowers around to light up the forest")
	if pick2 == 0:
		ps("You look around the forest and see a peculear tree and you examine it, the tree has many fruit but only some seem to be ripe.")
		ps("You don't know if the fruit is poisonous or not")
		choice2 = input("Do you want to pick the fruit, (there are 3 that seem ripe) (Y/N): ")
		if choice2 == "Y" or choice2 == "y":
			ps("You hear a voice again, it says, 'This is a medicinal fruit, it will heal you in battle'")
			ps("You put the fruit in you pocket and go deeper into the forest")
			pick2 = 1
		else:
			ps("You leave the fruit and go deeper into the forest")
			pick2 = 0
	global pick3
	if pick3 == 0:
		ps("You see a large tree and you think it will be a good idea to climb it to get a better view.")
		choice3 = input("Do you wish to climb it? (Y/N): ")
		if choice3 == "Y" or choice3 == "y":
			ps("You climbed the tree")
			ps("You see a castle, the open field, the mountains, and the strange sun.")
			ps("There only seems to be 3/4 of the sun left, it's like someone cut a pizza slice out of the sun.")
			ps("You don't know what will happen when the sun dissapears so you now have to make a choice")
			ps("You climb down the tree and now you have to think about where to go.")
			ps("Go back to where you began, go to the open field, or to the castle")
			pick3 = 1
			choice4 = input("Go back, open field, or the castle")
			
		else:
			ps("You dont know where to go now since the forest seems to never end.")
			ps("Do you want to go back, keep going deeper into the forest or go to the open field")
			pick3 = 0
			choice4 = input("Go back, forest, or open field")
			
	else:
		ps("Go back to where you began, go to the open field, or to the castle")
		choice4 = input("Go back, forest, or open field")
	

def R3():
	global choice5
	ps("You are at the open field and you see some creatures, you dont know if they are hostile or not.")
	choice5 = input("Do you attack them (You have the spear), approach to talk to them, or go to one of the places you have discovered")



# Code starts here
intro()

while start == "":
	if location == "spawn":
		R1()
	if location == "forest":
		R2()
	if location == "plains":
		R3()
	if location == "castlef1":
		R4()
	if location == "castlef2":
		R5()
	if location == "boss":
		R6()






#cursor.show()











