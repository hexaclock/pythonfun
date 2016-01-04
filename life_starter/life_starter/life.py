#
# life.py - Game of Life lab
#
# Name:
#

import random
import sys

def createOneRow(width):
	""" returns one row of zeros of width "width"...  
	You should use this in your
	createBoard(width, height) function """
	row = []
	for col in range(width):
		row += [0]
	return row
	
def createBoard(width,height):
	""" returns a 2d array with "height" rows and "width" cols """
	A = []
	for row in range(height):
		A += [createOneRow(width)]
	return A
	
def printBoard(A):
	'''this function prints the 2d list-of-lists A
		without spaces (using sys.stdout.write)'''
	for row in A:
		for col in row:
			sys.stdout.write(str(col))
		sys.stdout.write('\n')
		
def diagonalize(width,height):
	'''creates an empty board and then modifies it
	so that it has a diagonal strip of "on" cells.
	'''
	A = createBoard(width,height)
	
	for row in range(height):
		for col in range(width):
			if row == col:
				A[row][col] = 1
			else:
				A[row][col] = 0
	return A
		
def innerCells(w,h):
	A = createBoard(w,h)
	
	for row in range(h):
		for col in range(w):
			if row == 0 or col == 0:
				A[row][col] = 0
			elif row == (h-1) or col == (w-1):
				A[row][col] = 0
			else:
				A[row][col] = 1
	return A

def randomCells(w,h):
	A = createBoard(w,h)
	
	for row in range(h):
		for col in range(w):
			if row == 0 or col == 0:
				A[row][col] = 0
			elif row == (h-1) or col == (w-1):
				A[row][col] = 0
			else:
				A[row][col] = random.choice([0,1])
	return A
	
def copy(A):
	copied = createBoard(len(A[0]),len(A))
	
	for row in range(len(A)):
		for col in range(len(A[0])):
			copied[row][col] = (A[row][col])
	return copied
	
def innerReverse(A):
	reversed = copy(A)
	for row in range(len(A)):
		for col in range(len(A[0])):
			if row == 0 or col==0:
				reversed[row][col] = 0
			elif row == (len(A)-1) or col == (len(A[0])-1):
				reversed[row][col] = 0
			else:
				if reversed[row][col] == 1:
					reversed[row][col] = 0
				elif reversed[row][col] == 0:
					reversed[row][col] = 1
	return reversed

def next_life_generation(A):
	'''makes a copy of A and then advances one
		generation of Conway's game of life within
		the *inner cells* of that copy.
		The outer edge always stays 0.
	'''
	newA = copy(A)
	for row in range(1,len(A)-1):
		for col in range(1,len(A[0])-1):
			if countNeighbors(row,col,A) < 2:
				newA[row][col] = 0
			elif countNeighbors(row,col,A) > 3:
				newA[row][col] = 0
			elif countNeighbors(row,col,A) == 3 and A[row][col]==0:
				newA[row][col] = 1
	return newA

def countNeighbors(row,col,A):
	'''returns the number of live neighbors for a cell in the board A at a particular row and col.'''
	x=0
	if A[row-1][col]==1: x+=1
	if A[row+1][col]==1: x+=1
	if A[row][col-1]==1: x+=1
	if A[row][col+1]==1: x+=1
	if A[row-1][col-1]==1: x+=1
	if A[row-1][col+1]==1: x+=1
	if A[row+1][col-1]==1: x+=1
	if A[row+1][col+1]==1: x+=1
	return x
	
#Old functions#	
def old_next_life_generation(A):
	'''makes a copy of A and then advances one
		generation of Conway's game of life within
		the *inner cells* of that copy.
		The outer edge always stays 0.
	'''
	newA = copy(A)
	for row in range(len(A)):
		for col in range(len(A[0])):
			if row == 0 or col == 0:
				newA[row][col] = 0
			elif row == (len(A)-1) or col == (len(A[0])-1):
				newA[row][col] = 0
			else:
				if countNeighbors(row,col,A) < 2:
					newA[row][col] = 0
				elif countNeighbors(row,col,A) > 3:
					newA[row][col] = 0
				elif countNeighbors(row,col,A) == 3 and A[row][col]==0:
					newA[row][col] = 1
	return newA