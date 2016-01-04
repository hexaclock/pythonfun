#Daniel Vinakovsky
#CS-115 Homework 10
#28 November 2013
#I pledge my honor that I have abided by the Stevens Honor System


class Board:
	def __init__(self,width=7,height=6):
		'''Constructs a board object with a given width and height; defult is 7x6.'''
		self.width = width
		self.height = height
		self.createBoard()
		
	def __repr__(self):
		'''Method responsible for printing out the 2D array in a way that looks like a Connect4 board'''
		output = ''
		for row in range(self.height):
			for col in range(self.width+1):
				if col==self.width:
					output+= '\n'
				elif col==0:
					output+='|'+str(self.board[row][col])+'|'
				else:
					output+=str(self.board[row][col])+'|'
		output += ('-'*self.width*2)+'-'
		output += '\n'
		output += ' '
		for row in range(self.width):
			output+=str(row)+' '
		return str(output)
		
	def createOneRow(self):
		'''returns one row of zeros of width "width"
		You should use this in your
		createBoard(width, height) function'''
		row = []
		for col in range(self.width):
			row += [' ']
		return row
	
	def createBoard(self):
		'''returns a 2d array with "height" rows and "width" cols'''
		self.board = []
		for row in range(self.height):
			self.board += [self.createOneRow()]
		return self.board
		
	def allowsMove(self,col):
		'''Checks if a particular move is allowed (column is not full, column exists/is in possible range)'''
		emptyspots = 0
		columns = self.width
		if col>=columns or col<0:
			return False
		else:
			for row in range(self.height):
				if self.board[row][col] == ' ':
					emptyspots += 1
		if emptyspots == 0:
			return False
		else:
			return True
		
	def addMove(self,col,ox):
		'''Drops a given piece into a given column'''
		lowestSpot = 0
		for row in range(self.height):
			if self.board[row][col] == ' ':
				lowestSpot = row
		self.board[lowestSpot][col] = ox
		
	def setBoard(self,moveString):
		""" takes in a string of columns and places
			alternating checkers in those columns,
			starting with 'X'
			
			For example, call b.setBoard('012345')
			to see 'X's and 'O's alternate on the
			bottom row, or b.setBoard('000000') to
			see them alternate in the left column.

			moveString must be a string of integers
		"""
		nextCh = 'X'   # start by playing 'X'
		for colString in moveString:
			col = int(colString)
			if 0 <= col <= self.width:
				self.addMove(col, nextCh)
			if nextCh == 'X': nextCh = 'O'
			else: nextCh = 'X'
		
	def delMove(self,col):
		'''Removes the topmost piece in a given column'''
		highestSpot = 0
		columns = self.width
		for row in range(self.height):
			if self.board[row][col] != ' ':
				highestSpot = row
				break
		self.board[highestSpot][col] = ' '	
		
	def winsFor(self,ox):
		'''This method searches the entire board and checks if a particular player has won/gotten four in a row (vertically, horizontally, and either-way diagonally)'''
		#Horizontally
		for row in range(self.height):
			for col in range(self.width-3):
				if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] == ox:
					return True
		#Vertically	
		for col in range(self.width):
			for row in range(self.height-3):
				if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] == ox:
					return True
		#Diagonally, similar to y=x
		for row in range(self.height-3):
			for col in range(self.width-3):
				if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] == ox:
					return True
		#Diagonally, similar to y=-x
		for row in range(self.height-3):
			for col in range(3,self.width):
				if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] == ox:
					return True
		#If none of the above conditions, return False/no winner in the present situation
		return False
		
	def hostGame(self):
		'''Method responsible for the logical flow/progression of the Connect4 game; calls many of the methods above in a way that represents a realistic Connect4 game'''
		print "\n\nWelcome to Connect Four!\n\n"
		while True:
			print self
			
			userinx = input("\nX's choice:  ")
			print "\n"
			while self.allowsMove(userinx)==False:
				print "Not a valid move, please try again"
				userinx = input("\nX's choice:  ")
				print "\n"
			self.addMove(userinx,'X')
			if self.winsFor('X'):
				print "\n\nX wins -- Congratulations!\n\n"
				print self
				break
			else:
				print self
			
			userino = input("\nO's choice:  ")
			print "\n"
			while self.allowsMove(userino)==False:
				print "Not a valid move, please try again"
				userino = input("\nO's choice:  ")
				print "\n"
			self.addMove(userino,'O')
			if self.winsFor('O'):
				print "\n\nO wins -- Congratulations!\n\n"
				print self
				break