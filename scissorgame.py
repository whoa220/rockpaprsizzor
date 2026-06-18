import random

# start scores at 0
player = 0
aiplayer = 0

# actual gameplay
while True:
	# sets up the game for the end user and shit lmao, i WILL forget how this is made
	playerchoice = input("rock (r), paper (p), dodecahedreon (d), or scizzors (s) (press q to quit) ")
	choices = ["r", "p", "d", "s"]
	aichoice = random.choice(choices)
	# prints result for person to see
	print("yo choice is " + playerchoice + ". the robot chose " + aichoice + ".")

	# logic for scoring
	if playerchoice == aichoice: 
		print("Tie!")
	elif playerchoice == "p":
		if aichoice == "r":
			print("victory")
			player += 1
		else:
			print("epic stewie fail, make the computer choose r next time fool ;p")
			aiplayer += 1
	elif playerchoice == "r":
		if aichoice == "s":
			print("good job!")
			player += 1
		else:
			print("womp womp womp wompppp~...")
			aiplayer += 1
	elif playerchoice == "s":
		if aichoice == "p":
			print("ayyeeeee nice!")
			player += 1
		else:
			print("just get good...")
			aiplayer += 1
	elif playerchoice == "d":
		if aichoice == "r":
			print("why are you so bad at this game? SUPER F!!!")
			aiplayer += 20
		elif aichoice == "p":
			print("alas, you cannot make a dodecahedreon on a piece of p, so YOU WIN!!!")
			player += 20
		if aichoice == "s":
			print("you cant cut a dodecahedreon you clanker")
			player += 20
	# in case they want to ragequit
	elif playerchoice == "q":
		break

	#printing final scores
	print("human: %s" % player)
	print("robot: %s" % aiplayer)
	print("																				")