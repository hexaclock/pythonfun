# CS 115 Homework 4 Tester
# Daniel Vinakovsky
# 21 September 2013
# I pledge my honor that I have abided by the Stevens Honor System.

from hw4solution import *

def main():
	print "Problem 0"
	print giveChange(48, [1, 5, 10, 25, 50]) == [6, [1, 1, 1, 10, 10, 25]]
	print giveChange(48, [1, 7, 24, 42]) == [2, [24, 24]]
	print giveChange(35, [1, 3, 16, 30, 50]) == [3, [3, 16, 16]]
	print giveChange(50, [1, 3, 16, 30, 50]) == [1,[50]]
	
	#Tests taken directly from https://www.cs.hmc.edu/twiki/bin/view/ModularCS1/SequenceAlignment!
	print "Problem 1"
	print fancyLCS("x", "y")
	print fancyLCS("spam", "")
	print fancyLCS("spa", "m")
	print fancyLCS("cat", "car")
	print fancyLCS("cat", "lca")
	print fancyLCS("human", "chimpanzee")

	print "Problem 2"
	print wordsWithScore(aDictionary,scrabbleScores) == [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]]
	
	print "Problem 3"
	testTake(1, ["not", "it", "works", "!"])
	testTake(2, ["not", "it", "works", "!"])
	testTake(3, ["not", "it", "works", "!"])
	testTake(4, ["not", "it", "works", "!"])
	
	print "Problem 4"
	testDrop(0, ["I", "am", "nearly", "done"])
	testDrop(1, ["I", "am", "nearly", "done"])
	testDrop(2, ["I", "am", "nearly", "done"])
	testDrop(3, ["I", "am", "nearly", "done"])
	
def testTake(n,L):
    '''computes L[0:n] using the function above and checks the answer'''
    if take(n,L)==L[0:n]:
        print "True"
    else: print "my test failed"
	
def testDrop(n,L):
    '''computes L[n:] using the function above and checks the answer'''
    if drop(n,L)==L[n:]:
        print "True"
    else: print "my test failed"

main()
