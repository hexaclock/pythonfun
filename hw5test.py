# CS 115 Homework 5
# Daniel Vinakovsky
# 7 October 2013
# I pledge my honor that I have abided by the Stevens Honor System.

from hw5solution import *

def myTest():
	'''Tests fastFib, should return all true.'''
	print fastFib(5)==5==fib(5)
	print fastFib(6)==8==fib(6)
	print fastFib(7)==13==fib(7)
	print fastFib(8)==21==fib(8)
	print fastFib(9)==34==fib(9)
	print fastFib(10)==55==fib(10)
	print fastFib(15)==610==fib(15)
	print fastFib(20)==6765==fib(20)
	#Did not include test against fib(N) here because that would take millions of years.#
	print fastFib(42)==267914296
	print fastFib(43)==433494437
	print fastFib(54)==86267571272
	
myTest()