import random

# start scores at 0
player = 0
aiplayer = 0

# actual gameplay
while True:
	# sets up the game for the end user and shit lmao, i WILL forget how this is made
	playerchoice = input("Rock, paper, dodecahedreon, or sizzor")
	choices = ["rock", "paper", "dodecahedreon", "sizzor"]
	aichoice = random.choice(choices)
	# prints result for person to see
	print("yo choice is " + choice + ". the robot chose " + aichoice + ".")

	# logic for scoring
	if playerchoice == aichoice: 
		print("Tie!")
	elif playerchoice == "paper":
		if aiplayer == "rock":
			print("victory")
			player += 1
		else:
			print("epic stewie fail, make the computer choose rock next time fool ;p")
			aiplayer += 1
	elif playerchoice == "rock":
		if aiplayer == "sizzor":
			print("good job!")
			player += 1
		else:
			print("womp womp womp wompppp~...")
			aiplayer += 1
	elif playerchoice == "sizzor":
		if aiplayer == "paper":
			print("ayyeeeee nice!")
			player += 1
		else:
			print("just get good...")
			aiplayer += 1
	elif playerchoice == "dodecahedreon":
		if aiplayer == "rock":
			print("why are you so bad at this game? SUPER F!!!")
			aiplayer += 20
		elif aiplayer == "paper":
			print("alas, you cannot make a dodecahedreon on a piece of paper, so YOU WIN!!!")
			player += 20
		else:
			print("you cant cut a dodecahedreon you clanker")
			player += 20

	#printing final scores
	print("human: " + player + " points")
	print("robot: " + aiplayer + " points")