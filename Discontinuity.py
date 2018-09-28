'''
Title: Discontinuity
Author: Haamid Mohammed
Date Created: 2018/09/21
'''
import sys
import random
import time

play = True
start = 0
location = "spawn"
pick2 = 0
pick3 = 0
pick4 = 0
pick5 = 0
time1 = 10
choice1 = 0
choice2 = 0
choice3 = 0
choice4 = 0
choice5 = 0
choice6 = 0
choice7 = 0
choice6 = 0
choice9 = 0
choice10 = 0
choice11 = 0
choice12 = 0
choice13 = 0
choice14 = 0
s1 = 0
power = 0
	


def ps(str): # Subroutine to Print Slowly
	for x in str:
			sys.stdout.write(x)
			sys.stdout.flush()
			time.sleep(0.01)
	print("") 

def intro(): # The Intro
	global start
	print("""
 __     __   __   __       ___               ___     
|  \\ | /__` /  ` /  \\ |\\ |  |  | |\\ | |  | |  |  \\ / 
|__/ | .__/ \\__, \\__/ | \\|  |  | | \\| \\__/ |  |   |                                                      

""")
	print("This game is a choose you own adventure.")
	print("You have to make many different choices and your outcome will change depending on the choices you make.")
	print("There are many ways to play the game but there are good outcomes as well as bad ones")
	print("Lets see how you play the game.")
	
	while not start == "":
		start = input("Press enter to begin")
	

def R1(): # Location 1, Where you begin
	global location
	global time1
	global s1
	

	if s1 == 0:
		ps("You wake up and u see a spear next to you, and you hear a voice, it says, 'Complete the sword and beat the boss before time runs out'.")
		ps("You don't know  what that means, so you look around.")
		ps("You see a forest and an open field in front of you, in the open field you see some creatures that you have never seen before and behind you there is a mountain that is too tall and steep to climb.")
		s1 = 1
	ps("Now you have to make a choice, go to the forest, go to the open field, or try to climb the mountain.")
	

	while location == "spawn":
		choice1 = input("Forest, open field, or mountain: ")
		

		if choice1 == "Forest" or choice1 == "forest":
			location = "forest"
		

		elif choice1 == "Mountain" or choice1 == "mountain":
			ps("You tried to climb the mountain but failed to even get quarter of the way and because of that you wasted time")
			#ps("Now you have wasted time climbing the mountain where do you want to go, the forest or the open field")
			time1 -= 1
		

		elif choice1 == "open field" or choice1 == "Open Field" or choice1 == "open Field" or choice1 == "Open field" or choice1 == "field" or choice1 == "Field":
			location = "plains"
	
    


def R2(): # Location 2, The forest
	global pick2
	global location
	global time1
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
	

	if pick3 == 0:
		ps("You see a large tree and you think it will be a good idea to climb it to get a better view.")
		choice3 = input("Do you wish to climb it? (Y/N): ")
		

		if choice3 == "Y" or choice3 == "y":
			ps("You climbed the tree")
			ps("You see a castle, the open field, the mountains, and the strange sun.")
			ps("There only seems to be only a portion of the sun left, it's like someone cut a pizza slice out of the sun.")
			ps("You don't know what will happen when the sun dissapears so you now have to make a choice")
			ps("You climb down the tree and now you have to think about where to go.")
			ps("Go back to where you began, go to the open field, or to the castle")
			pick3 = 1
		

			while location == "forest":
				choice4 = input("Go back, open field, or the castle: ")
		

				if choice4 == "castle" or choice4 == "Castle" or choice4 == "The Castle" or choice4 == "the castle" or choice4 == "The castle" or choice4 == "the Castle":
					location = "castleout"
		

				elif choice4 == "Go Back" or choice4 == "go back" or choice4 == "back" or choice4 == "Back":
					location = "spawn"
		

				elif choice4 == "open field" or choice4 == "Open Field" or choice4 == "open Field" or choice4 == "Open field" or choice4 == "field" or choice4 == "Field":
					location = "plains"
			
		
		else:
			ps("You dont know where to go now since the forest seems to never end.")
			ps("Do you want to go back, keep going deeper into the forest or go to the open field")
			pick3 = 0
			
			while location == "forest":
				choice4 = input("Go back, forest, or open field: ")
				

				if choice4 == "forest" or choice4 == "Forest" :
					ps("You go deeper into the forest and you seem to have left from the other side of the forest.")
					location = "castleout"
				

				elif choice4 == "Go Back" or choice4 == "go back" or choice4 == "back" or choice4 == "Back":
					location = "spawn"
				

				elif choice4 == "open field" or choice4 == "Open Field" or choice4 == "open Field" or choice4 == "Open field" or choice4 == "field" or choice4 == "Field":
					location = "plains"
			
	else:
		ps("Go back to where you began, go to the open field, or to the castle")
		
		while location == "forest":
			choice4 = input("Go back, the castle, or open field: ")


			if choice4 == "forest" or choice4 == "Forest" :
				ps("You go deeper into the forest and you seem to have left from the other side of the forest.")
				location = "castleout"
			

			elif choice4 == "Go Back" or choice4 == "go back" or choice4 == "back" or choice4 == "Back":
				location = "spawn"
			

			elif choice4 == "open field" or choice4 == "Open Field" or choice4 == "open Field" or choice4 == "Open field" or choice4 == "field" or choice4 == "Field":
				location = "plains"


	

def R3(): # Location 3, The plains
	global location
	global time1
	global power
	global start
	global pick5
	if pick5 == 0:
		ps("You are at the open field and you see some creatures, you dont know if they are hostile or not.")
		ps("Do you attack them (You have the spear), approach to talk to them, or go to one of the places you have discovered")
		choice5 = input("attack, talk or leave: ")


		if choice5 == "attack" or choice5 == "attack them":
			ps("You attacked them without holding anything back.")
			ps("You kill the creatures and some sort of power flows into you empowering you")
			ps("You try to summon this new power and you think that having a sword would be nice.")
			ps("A sword suddenly appears in your hand, the sword has no weight but it is sharper than any sword you have used before.")
			ps("You think of it becoming a bow and it slowly chapes into a bow.")
			ps("You think this is a great power to have and it will be useful in the future if you have to fight anything else.")
			power = 1
			variable = 1
			pick5 = 1


		elif choice5 == "talk" or choice5 == "Talk":
			ps("They attack you, do you want to run away or fight them?")
			choice6  = input("Run or Fight: ")
		

			if choice6 == "fight" or choice6 == "Fight":
				ps("You attacked them without holding anything back.")
				ps("You kill the creatures and some sort of power flows into you empowering you")
				ps("You try to summon this new power and you think that having a sword would be nice.")
				ps("A sword suddenly appears in your hand, the sword has no weight but it is sharper than any sword you have used before.")
				ps("You think of it becoming a bow and it slowly chapes into a bow.")
				ps("You think this is a great power to have and it will be useful in the future if you have to fight anything else.")
				power = 1
				variable = 1
				pick5 = 1


			elif choice6 == "Run" or choice6 == "run":
				choice7 = input("The forest or the mountains: ")
		

				if choice7 == "The Forest" or choice7 == "The forest" or choice7 == "Forest" or choice7 == "forest":
					ps("You lose the creatures in the forest and they go back to where they were.")
					ps("You got lucky that they arn't that smart or you wouldn't have gotten away")
					ps("You now go back to the open field ")
					R3()


				elif choice7 == "Mountains" or choice7 == "Mountain" or choice7 == "mountains" or choice7 == "mountain" or choice7 == "The Mountains" or choice7 == "The Mountain" or choice7 == "The mountains" or choice7 == "The mountain" or choice7 == "the Mountains" or choice7 == "the Mountain" or choice7 == "the mountains" or choice7 == "the mountain":
					ps("You run out of places to run and the creatures catch up with you and kill you.")
					start = 0


		elif choice5 == "leave" or choice5 == "Leave":
			choice7 == input("Where do you go.(Forest or Mountains): ")
		

			if choice7 == "forest" or choice7 == "Forest":
				location = "forest"
		

			elif choice7 == "Mountains" or choice7 == "Mountain" or choice7 == "mountains" or choice7 == "mountain":
				location == "spawn"
	

	elif pick5 == 1 and pick3 == 1:
		ps("You think that you should probably go to the castle now")
		choice9 = input("Do you go to the castle or to another place (Castle, Forest, Mountains): ")
		

		if choice9 == "Castle" or choice9 == "castle":
			location = "castleout"


		elif choice9 == "Forest" or choice9 == "forest":
			location = "forest"


		elif choice9 == "Mountains" or choice9 == "Mountain" or choice9 == "mountains" or choice9 == "mountain":
			location = "spawn"


	elif pick5 == 1 and pick3 == 0:
		ps("You think that you should probably get a better view of the landscape by headding into the forest")
		choice9 = input("Do you go to the forest or the mountains (Forest, Mountains): ")
		

		if choice9 == "Forest" or choice9 == "forest":
			location = "forest"


		elif choice9 == "Mountains" or choice9 == "Mountain" or choice9 == "mountains" or choice9 == "mountain":
			location = "spawn"


	if variable == 1 and pick3 == 1:
		ps("You think that you should probably go to the castle now")
		choice9 = input("Do you go to the castle or to another place (Castle, Forest, Mountains): ")
		

		if choice9 == "Castle" or choice9 == "castle":
			location = "castleout"


		elif choice9 == "Forest" or choice9 == "forest":
			location = "forest"


		elif choice9 == "Mountains" or choice9 == "Mountain" or choice9 == "mountains" or choice9 == "mountain":
			location = "spawn"


	elif variable == 1 and pick3 == 0:
		ps("You think that you should probably get a better view of the landscape by headding into the forest")
		choice9 = input("Do you go to the forest or the mountains (Forest, Mountains): ")
		

		if choice9 == "Forest" or choice9 == "forest":
			location = "forest"


		elif choice9 == "Mountains" or choice9 == "Mountain" or choice9 == "mountains" or choice9 == "mountain":
			location = "spawn"




def R4(): # Location 4, outside the castle
	global location
	ps("You see a huge castle that has only one way to get to the doors")
	ps("There is a bridge to get to the doors but the bridge has really powerful defences")
	

	if power == 1:
		ps("You use the power you gained to create a bow and arrows.")
		ps("Using the bow and arrows you slowly disarm the defences until you reach the entrance to the castle.")
		choice10 = input("Do you wish to enter the castle? (Y/N): ")
		

		if choice10 == "Y" or choice10 == "y":
			location = "boss"
		

		elif choice10 == "N" or choice10 == "n":
			choice11 == input("Where do you want to go? (Forest or Open field): ")
		

			if choice11 == "Forest" or choice11 == "forest":
				location = "forest"
	

			elif choice11 == "open field" or choice11 == "Open Field" or choice11 == "open Field" or choice11 == "Open field" or choice11 == "field" or choice11 == "Field":
				location = "plains"
	

	elif power == 0:
		ps("Seems like you need a ranged weapon to get past this bridge and your spear isnt enough to destroy the defences")
		ps("Where do you go now?")
		choice8 = input("Forest or Open field")


		if choice8 == "Forest" or choice8 == "forest":
			location = "forest"
	

		elif choice8 == "open field" or choice8 == "Open Field" or choice8 == "open Field" or choice8 == "Open field" or choice8 == "field" or choice8 == "Field":
			location = "plains"




def R5(): # Location 5, Boss room
	ps("You enter the castle and you hear the voice again and it says, 'This is the boss room'.")
	ps("You see a huge open space with the boss on the other end of the room waiting for you")
	ps("The boss asks you 'Are you ready to fight me?'")
	choice13 = input("What is your answer to the boss's question? (Y/N)")


	if (choice13 == "y" or choice13 == "Y") and pick3 == 0:
		ps("You attack the boss, and after a long and hard fought fight, you beat the boss but at a cost.")
		ps("You lost one of your arms and you are mortally wounded")
		ps("Unluckily you have no way to heal yourself so you perish from internal dammage and bloodloss.")
		start = 0


	elif (choice13 == "y" or choice13 == "Y") and pick3 == 1:
		ps("You attack the boss, and after a long and hard fought fight, you beat the boss but at a cost.")
		ps("You lost one of your arms and you are mortally wounded")
		ps("Then you remember that you have the medicinal fruit that can heal you.")
		ps("You eat one, you have 2 left, it completely heals you and even regrows your arm.")
		ps("Suddenly a portal appears near the entrance and the voice says 'You have cleared this floor, take this portal to the next floor when you are ready'")
		choice12 = input("Go through the portal or stay until you are ready?(Stay or Leave): ")


		if choice12 == "stay" or choice12 == "Stay" or choice12 == "leave" or choice12 == "Leave":
			ps("This is the end of part 1, stay tuned for the release of part 2")
			ps("Thankyou for playing Discontinuity!")
			sys.exit()


	elif choice13 == "n" or choice13 == "N":
		ps("You answer the boss that you are not ready to fight him yet.")
		ps("The boss says 'Come back when you are ready'.")
		ps("You leave the castle and cross the bridge and it seems that the defences are active again.")
		choice14 == input("Where do you want to go? (Forest or Open field): ")
	

		if choice14 == "Forest" or choice14 == "forest":
			location = "forest"
	

		elif choice14 == "open field" or choice14 == "Open Field" or choice14 == "open Field" or choice14 == "Open field" or choice14 == "field" or choice14 == "Field":
			location = "plains"



# Code starts here
while play:
	intro()

	while start == "":
		if location == "spawn":
			R1()
		elif location == "forest":
			R2()
		elif location == "plains":
			R3()
		elif location == "castleout":
			R4()
		elif location == "boss":
			R5()
		if time1 <= 0:
			ps("You hear the voice again and it says 'Time is up, the shadow soldiers have been released'.")
			ps("Immidiately you see many shadow creatures surround you and they can manipulate their bodies like whips.")
			ps("They attack you and eveytime they hit you, it gives you a really bad burn.")
			ps("You slowly die of excruciating pain, it feels like getting burned alive.")
			start = 0
		time1 -= 1
	restart = input("Do you wish to try again? (Y/N): ")
	if restart == "Y" or restart == "y" or restart == "": #resets all variables
		start = 0
		location = "spawn"
		pick2 = 0
		pick3 = 0
		pick4 = 0
		pick5 = 0
		time1 = 10
		choice1 = 0
		choice2 = 0
		choice3 = 0
		choice4 = 0
		choice5 = 0
		choice6 = 0
		choice7 = 0
		choice6 = 0
		choice9 = 0
		choice10 = 0
		choice11 = 0
		choice12 = 0
		choice13 = 0
		choice14 = 0
		s1 = 0
		power = 0

	else:
		ps("Thankyou for playing Discontinuity!")
		sys.exit()