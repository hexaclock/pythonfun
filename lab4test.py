from lab4sol import *

def testing():
	print change(48, [1, 5, 10, 25, 50]) == 6
	print change(48, [1, 7, 24, 42]) == 2
	print change(35, [40, 3, 16, 35, 50]) == 1
	print change(12 , [5]) == float("inf")

testing()