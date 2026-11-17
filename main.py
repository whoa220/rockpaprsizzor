from markov import MarkovChain
import subprocess, platform

if platform.system()=="Windows":
    if platform.release() in {"10", "11"}:
        subprocess.run("", shell=True) 
        print("\033c", end="")
    else:
        subprocess.run(["cls"])
else: # The Tux and 'ac
    print("\033c", end="")

print("\nRockPaprScizor Copyright (C) 2026 WalterFisher")
print("Don't come crying to me if this breaks, its under NO WARRANTY")

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

# establishes a system for the markov chain
markvov_chain = MarkovChain(choices, n_states=4)

# actual gameplay
n_round = 0
while True:
	playerchoice = input("Choose rock (r), paper (p), scissors (s), or dodechedreon (d). (q to quit) ")
	aichoice = winningmoves[markvov_chain.predict()]
	
	# tell the shit to destroy the file
	if playerchoice == "q":
		print("\033c", end="")
		break
	# tell the player to get smarter
	elif playerchoice not in winningmoves:
		print("Thats not a correct choice! It's case sensitive lowercase. Try Again\n")
		continue
	# Tell them if its ok
	else:
		print("\nYour choice is " + playerchoice + ". The robot chose " + aichoice + ".")

	# logic for scoring
	if playerchoice == aichoice:
		result = "Its a Tie"
		# crank the round counter up by one
		n_round += 1
	elif winningmoves[playerchoice] == aichoice:
		result = "AI won"
		aiplayer += 1
		n_round += 1
	else:
		result = "You won"
		player += 1
		n_round += 1

	markvov_chain.update(playerchoice)

	#printing final scores
	print("\n" + result + " for round %s" % n_round)
	print("\n")
	print("human: %s" % player)
	print("robot: %s" % aiplayer)
	print("\n")


	nextchoice = ["c", "q"]
	countermove = input("Do you want to continue or quit (q)? ")
	if countermove == "q":
		print("\033c", end="")
		break
	else:
		print("\033c", end="")

