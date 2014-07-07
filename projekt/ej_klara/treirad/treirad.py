#main file for 3 i rad
#flow: how many players, initiative, human or computer move till game is won or full, ask for new game or quit.
#At each step, print board layout with pieces. 
class Player:
	"""docstring for player"""
	def __init__(self, namn):
		self.namn = namn

	def placePiece(self):
		#player places a piece
		pass 

	def skrivut(self):
		print("Namnet är: ", self.namn)

if __name__ == "__main__":
	#Initialize, board|player|game|AI
	titel = input("Var god och ange ert namn: ")
	spelare = Player(titel)
	spelare.skrivut()
	#ask for name

	#Initiative roll

	#Playloop till not True, aka game is won or board full.

	#Ask for a new game or quit.

	#Specificerar spelar klassen och dess definitioner