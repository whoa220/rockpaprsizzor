import random

# start scores at 0
player = 0
aiplayer = 0

# sets up the game for the end user and shit lmao, i WILL forget how this is made
choices = ["r", "p", "d", "s"]

winningmoves = {
	"r": "p",
	"p": "s",
	"s": "r",
	"p": "d",
	"d": "r",
	"d": "s"
}

# actual gameplay
while True:
	playerchoice = input("Choose rock, papr, scizzors, or dodechedreon (q to quit) ")
	aichoice = random.choice(choices)
	# prints result for person to see

	if playerchoice == "q":
		break
	elif playerchoice not in winningmoves:
		print("thats not a correct choice! try again")
		print("\n")
		continue
	else:
		print("yo choice is " + playerchoice + ". the robot chose " + aichoice + ".")

	# logic for scoring
	if playerchoice == aichoice:
		result = "tie"
	elif winningmoves[playerchoice] == aichoice:
		result = "ai wins"
		aiplayer += 1
	else:
		result = "player wins"
		player += 1

	#printing final scores
	print("\n")
	print(result)
	print("human: %s" % player)
	print("robot: %s" % aiplayer)
	print("\n")