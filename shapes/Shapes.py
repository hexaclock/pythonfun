#Daniel Vinakovsky
#CS-115 - Homework 11
#10 December 2013
#I pledge my honor that I have abided by the Stevens Honor System

import math
import turtle

from Matrix import *
from Vector import *

class Shape:
	def __init__(self):
		self.points = []
		
	def render(self):
		"""Use turtle graphics to render shape"""
		turtle.penup()
		turtle.setposition(self.points[0].x, self.points[0].y)
		turtle.pendown()
		turtle.fillcolor(self.color)
		turtle.pencolor(self.color)
		turtle.begin_fill()
		for vector in self.points[1:]:
			turtle.setposition(vector.x, vector.y)
		turtle.setposition(self.points[0].x, self.points[0].y)
		turtle.end_fill()

	def erase(self):
		"""Draw shape in white to effectively erase it from screen"""
		temp = self.color
		self.color = "white"
		self.render()
		self.color = temp
	
	def rotate(self, theta):
		"""Rotate shape by theta degrees """
		theta = math.radians(theta)  # THIS IS CORRECT!
		# Python's trig functions expect input in radians
		# so this function converts from degrees into radians.
		RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))
		NewPoints = []
		for vector in self.points:
			newvector = RotationMatrix * vector
			NewPoints.append(newvector)
		self.points = NewPoints
		
	def rotate2(self, theta):
		"""Rotate shape by theta radians """
		RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))
		NewPoints = []
		for vector in self.points:
			newvector = RotationMatrix * vector
			NewPoints.append(newvector)
		self.points = NewPoints
		
	def flip(self,pta,ptb):
		'''Flips a vector over a line (two vectors pta, ptb)'''
		hypdist = math.sqrt(((ptb.x-pta.x)**2)+((ptb.y-pta.y)**2))
		basedist = ptb.x-pta.x
		self.rotate2(math.acos(basedist/hypdist))
		NewPoints = []
		for point in self.points:
			newvector = Vector(point.x,-1*point.y)
			NewPoints.append(newvector)
		self.points = NewPoints
		
	def scale(self,s):
		'''Scales a shape s times by creating a Vector(S,S) and multiplying each vector/point by that vector.'''
		self.translate(Vector(0,0))
		scalevect = Vector(s,s)
		NewPoints = []
		for vector in self.points:
			newvector = scalevect*vector
			NewPoints.append(newvector)
		self.points = NewPoints
		
		self.translate(self.center)
	
	def rotateAbout(self,v,theta):
		'''Rotates a shape about a given point, and by theta degrees. v is a vector, theta is a number'''
		self.translate(Vector(0,0))
		self.rotate(theta)
		self.translate(v)
	
	def translate(self,v):
		'''Translates an object by vector v amount'''
		NewPoints=[]
		for i in self.points:
			newvector = i+v
			NewPoints.append(newvector)
		self.points = NewPoints
		
class Rectangle(Shape):
	def __init__(self, width, height, center = Vector(0, 0), color = "black"):
		self.center = center
		SW = Vector(center.x - width/2.0, center.y - height/2.0)
		NW = Vector(center.x - width/2.0, center.y + height/2.0)
		NE = Vector(center.x + width/2.0, center.y + height/2.0)
		SE = Vector(center.x + width/2.0, center.y - height/2.0)
		self.points = [SW, NW, NE, SE]
		self.color = color

class Square(Rectangle):
	def __init__(self, width, center=Vector(0, 0), color = "black"):
		self.center = center
		Rectangle.__init__(self, width, width, center, color)
		
class Circle(Shape):
	def __init__(self, center = Vector(0, 0), radius = 10, color = "black"):
		self.center = center
		self.radius = radius
		self.color = color
		self.points = []

	def render(self):
		turtle.penup()
		turtle.setposition(self.center.x, self.center.y)
		turtle.right(90)
		turtle.forward(self.radius)
		turtle.left(90)
		turtle.pendown()
		turtle.fillcolor(self.color)
		turtle.pencolor(self.color)
		turtle.begin_fill()
		turtle.circle(self.radius)
		turtle.end_fill()
	
	def translate(self,v):
		'''Translates a circle by changing its center, requires a vector as an input'''
		self.center = v

	def rotate(self, theta):
		""" theta is in degrees """
		theta = math.radians(theta)
		RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))        
		self.center = RotationMatrix * self.center
		
	def scale(self,s):
		'''Scales a circle by simply enlarging its radius s times. s is a float'''
		self.translate(Vector(0,0))
		self.radius = self.radius*s
		self.translate(self.center)
	
class rTriangle(Shape):
	def __init__(self,base,height,center=Vector(0,0),color="black"):
		'''Creates a right triangle given a base and a height'''
		self.center = center
		SW = Vector(center.x - base/3.0, center.y - height/3.0)
		N = Vector(center.x - base/3.0, center.y + height/3.0)
		SE = Vector(center.x + base/3.0, center.y - height/3.0)
		self.points = [SW,N,SE]
		self.color = color

		
		
