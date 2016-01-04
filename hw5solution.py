# CS 115 Homework 5 Test
# Daniel Vinakovsky
# 7 October 2013
# I pledge my honor that I have abided by the Stevens Honor System.

import turtle

memo={}

def svTree(trunkLength, levels):
		'''Draws a tree given trunk length and number of levels/branches using recursion'''
		if (levels <= 1):
			return
		else:
			turtle.forward(trunkLength)
			turtle.right(45)
			svTree(trunkLength/2,levels-1)
			turtle.left(90)
			svTree(trunkLength/2,levels-1)
			turtle.right(45)
			turtle.forward(-1*trunkLength)
			return

def fastFib(N):
		'''Quickly calculates Nth term in the Fibonacci sequence using recursion with added memoization'''
		if N==0 or N==1:
				return N
		elif memo.has_key(N):
				return memo[N]
		else:
				fibber = (fastFib(N-1) + fastFib(N-2))
				memo[N] = fibber
				return fibber
				
def fib(N):
		'''Calculates Nth term in the Fibonacci sequence using only recursion.'''
		if N==0 or N==1: 
			return N
		else: 
			return fib(N-1) + fib(N-2)
		