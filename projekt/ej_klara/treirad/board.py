#Defines dimensions of the board.
#Place def, checks for won game, full board, print status of board, new board

class Board(self, x, y):
	"""docstring for Board"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.field = {"1": "(0,0)", "2": "(1,0)","3": "(2,0)",
					  "4": "(0,1)", "5": "(1,1)","6": "(2,1)",
					  "7": "(0,2)", "8": "(1,2)","9": "(2,2)"}

	def place():
		#place the tokens
	def move():
		#move tokens if needed
	def delete():
		#Delete one+ token
	def isFull():
		#check if board is full, return True/False
	def print_board():
		#Print graphical Interface to show user the current status
	def findX():
		#Find X tokens of same value adjacent eachother that forms a line.
		#Breakpoint is 3, that is a win.
	def isWin():
		#Check if current status results in a win for a player/computer