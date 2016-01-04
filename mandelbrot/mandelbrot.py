# mandelbrot.py
# Lab 8
#
# Name: Daniel Vinakovsky

# keep this import line...
from cs5png import *

# start your Lab 8 functions here:

def mult(c,n):
	'''mult uses only a loop and addition to multiply c by the integer n'''
	result = 0
	for x in range(n):
		#update the value of result here in the loop
		result += c
	return result
	
def update(c,n):
	'''update starts with z=0 and runs z = z**2 + c
	for a total of n times. It returns the final z.'''
	z = 0
	for x in range(n):
		z = z**2 + c
	return z
	
def inMSet(c,n):
	'''takes in c for the update step of z = z**2 + c
		n, the maximum number of times to run that step
	Returns:
		False as soon as abs(z) gets larger than 2
		True if abs(z) never gets larger than 2 (for n iterations).'''
	z = 0
	for x in range(n):
		if abs(z) > 2:
			return False
		z = z**2 + c
	return True
	
def weWantThisPixel(col,row):
	'''a function that returns True if we want the pixel at col, row; False otherwise'''
	if col%10==0 and row%10==0:
		return True
	else:
		return False
		
def test():
	'''a function to demonstrate how to create and save a png image'''
	width = 300
	height = 200
	image = PNGImage(width,height)
	#create a loop in order to draw some pixels
	for col in range(width):
		for row in range(height):
			if weWantThisPixel(col,row) == True:
				image.plotPoint(col,row)
	#we looped through every image pixel; we now write the file
	image.saveFile()
	
def scale(pix,pixelMax,floatMin,floatMax):
	ratio = ((pix*1.0)/(pixelMax*1.0))
	range_pos = floatMax - floatMin
	return (ratio*range_pos) + floatMin
	
def mset():
	'''creates a 300x200 image of the Mandelbrot set'''
	numIterations = 75
	XMAX = 1.0
	XMIN = -2.0
	YMAX = 1.0
	YMIN = -1.0
	width = 1024
	height = 768
	image = PNGImage(width,height)
	for col in range(width):
		for row in range(height):
			x = scale(col,width,XMIN,XMAX)
			y = scale(row,height,YMIN,YMAX)
			c = x + y*1j
			if inMSet(c,numIterations) == True:
				image.plotPoint(col,row,(255,255,255))
			else:
				image.plotPoint(col,row,(0,0,0))
	#we looped through every image pixel; we now write the file
	image.saveFile()

mset()
	
#from class today
def fib(n):
	a = 0
	b = 1
	ret = 1
	for i in range(n-1):
		ret = a+b
		a = b
		b = ret
	return ret	
print fib(5)