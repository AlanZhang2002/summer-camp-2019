import random

#2048

class Minigame():
	def __init__(self):
		self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.score = 0
		self.gameState = 'not over'
		self.playState = 'y'

	def changeState(self):
		self.gameState = 'lose'
		for i in self.board:
			for j in i:
				if j == 0:
					self.gameState = 'not over'
				if j == 2048:
					self.gameState = 'win'

	def reset(self):
		self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.score = 0
		self.gameState = 'not over'
		a = random.randint(0, 15)
		b = random.randint(0, 15)
		while b == a:
			b = random.randint(0, 15)
		self.board[int(a / 4)][int(a % 4)] = 2
		self.board[int(b / 4)][int(b % 4)] = 2

	def printBoard(self):
		for i in self.board:
			for j in i:
				print(j, end = self.spacing(j))
			print()
		print("Score: " + str(self.score))

	# makes board spaced out nicely kinda
	def spacing(self, num):
		spaces = "      "
		return spaces[0:-len(str(num))]

	"""
	To correctly update board:
	shift, combine, shift
	"""

	def up(self):
		moved = False
		for i in range(1, 4): #shift
			for j in range(4):
				for temp in range(i, 0, -1):
					if self.board[temp-1][j] == 0 and self.board[temp][j] != 0:
						self.board[temp-1][j] = self.board[temp][j]
						self.board[temp][j] = 0
						moved = True
					else:
						break
		for i in range(3, 0, -1): #combine
			for j in range(4):
				if self.board[i-1][j] == self.board[i][j] and self.board[i][j] != 0:
					self.board[i-1][j] = 2*self.board[i][j]
					self.board[i][j] = 0
					self.score += self.board[i-1][j]
					moved = True
		for i in range(1, 4): #shift
			for j in range(4):
				if self.board[i-1][j] == 0 and self.board[i][j] != 0:
					self.board[i-1][j] = self.board[i][j]
					self.board[i][j] = 0
					moved = True
		return moved

	def down(self):
		moved = False
		for i in range(2, -1, -1): #shift
			for j in range(4):
				for temp in range(i, 3):
					if self.board[temp+1][j] == 0 and self.board[temp][j] != 0:
						self.board[temp+1][j] = self.board[temp][j]
						self.board[temp][j] = 0
						moved = True
					else:
						break
		for i in range(3): #combine
			for j in range(4):
				if self.board[i+1][j] == self.board[i][j] and self.board[i][j] != 0:
					self.board[i+1][j] = 2*self.board[i][j]
					self.board[i][j] = 0
					self.score += self.board[i+1][j]
					moved = True
		for i in range(2, -1, -1): #shift
			for j in range(4):
				if self.board[i+1][j] == 0 and self.board[i][j] != 0:
					self.board[i+1][j] = self.board[i][j]
					self.board[i][j] = 0
					moved = True
		return moved


	def left(self):
		moved = False
		for i in range(4): #shift
			for j in range(3, 0, -1):
				for temp in range(j, 4):
					if self.board[i][temp-1] == 0 and self.board[i][temp] != 0:
						self.board[i][temp-1] = self.board[i][temp]
						self.board[i][temp] = 0
						moved = True
					else:
						break
		for i in range(4): #combine
			for j in range(1, 4):
				if self.board[i][j-1] == self.board[i][j] and self.board[i][j] != 0:
					self.board[i][j-1] = 2*self.board[i][j]
					self.board[i][j] = 0
					self.score += self.board[i][j-1]
					moved = True
		for i in range(4): #shift
			for j in range(3, 0, -1):
				if self.board[i][j-1] == 0 and self.board[i][j] != 0:
					self.board[i][j-1] = self.board[i][j]
					self.board[i][j] = 0
					moved = True
		return moved

	def right(self):
		moved = False
		for i in range(4): #shift
			for j in range(3):
				for temp in range(j, -1, -1):
					if self.board[i][temp+1] == 0 and self.board[i][temp] != 0:
						self.board[i][temp+1] = self.board[i][temp]
						self.board[i][temp] = 0
						moved = True
					else:
						break
		for i in range(4): #combine
			for j in range(2, -1, -1):
				if self.board[i][j+1] == self.board[i][j] and self.board[i][j] != 0:
					self.board[i][j+1] = 2*self.board[i][j]
					self.board[i][j] = 0
					self.score += self.board[i][j+1]
					moved = True
		for i in range(4): #shift
			for j in range(3):
				if self.board[i][j+1] == 0 and self.board[i][j] != 0:
					self.board[i][j+1] = self.board[i][j]
					self.board[i][j] = 0
					moved = True
		return moved

	def move(self):
		move = input("Your move: ")
		moved = False
		if move == 'w':
			moved = self.up() #if moving doesn't change anything on board
		elif move == 'a':
			moved = self.left()
		elif move == 's':
			moved = self.down()
		elif move == 'd':
			moved = self.right()
		else:
			print("That's not a valid move!! To move, use wasd. ")
			self.move()
			return

		if not moved:
			print("That doesn't do anything! Try another move. ")
			self.printBoard()
			self.move()

	def addTwo(self):
		a = random.randint(0, 15)
		while self.board[int(a/4)][int(a%4)] != 0:
			a = random.randint(0, 15)
		self.board[int(a/4)][int(a%4)] = 2

	def playGame(self):
		while self.gameState == 'not over':
			self.printBoard()
			self.move()
			self.changeState()
			self.addTwo()
		if self.gameState == 'lose':
			print("You lost :(")
		else:
			print("You won!")
		self.gameState = 'not over'


	def start(self):
		while self.playState == 'y':
			self.reset()
			self.playGame()
			self.playState = input("Would you like to play again? y/n")
		

game = Minigame()
game.start()