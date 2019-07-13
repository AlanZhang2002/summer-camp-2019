import random

finished = False

def numChecker(x, target):
	return target - x

def startingPrompt():
	print()
	play = input("Would you like to play a game? Say yes if you do: ")
	if play == "yes":
		print("Great! I'll think of a number...")
		return True
	else:
		return False

def endGame():
	print()
	print("Wow! You guessed my number!")
	if startingPrompt():
		playGame()


def playTurn(target):
	global finished
	print ("Guess a number from 1 to 100: ")
	guess = input()
	print()
	if not guess.isdigit():
		print("That's not a number! Please guess a number next time.")
		return
	guessNum = int(guess)
	if numChecker(guessNum, target) == 0:
		finished = True
	elif numChecker(guessNum, target) < 0:
		print("My number is smaller than " + guess + ", but good guess!")
		print("Try again!")
	else:
		print("My number is larger than " + guess + ", but good guess!")
		print("Try again!")


def playGame():
	global finished
	finished = False
	target = random.randint(1, 100)
	while not finished:
		playTurn(target)
		print()
	endGame()


print ("Welcome to my Number Guessing Game!")
if startingPrompt():
	playGame()
