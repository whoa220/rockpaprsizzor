import random
from markov import MarkovChain

print("\nRockPaprScizor Copyright (C) 2026 WalterFisher")
print("Don't come crying to me if this breaks, its under NO WARRANTY\n")

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
markvov_chain = MarkovChain(choices, n_states=4)

# actual gameplay
n_round = 1
while True:
	playerchoice = input("Choose rock, papr, scizzors, or dodechedreon (q to quit) ")
	aichoice = winningmoves[markvov_chain.predict()]
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

	markvov_chain.update(playerchoice)

	#printing final scores
	print("\n")
	print(result + " for round %s" % n_round)
	print("human: %s" % player)
	print("robot: %s" % aiplayer)
	print("\n")
	n_round += 1