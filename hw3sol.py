#Daniel Vinakovsky
#CS 115 Homework 3
#September 16, 2013
#I pledge my honor that I have abided by the Stevens Honor System

#Allow more recursions
import sys
sys.setrecursionlimit(10000)

#Import big dictionary
#from dict import *

#Globals#
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"] 

def bestWord(Rack):
		'''Returns the best word with the highest point value in the list obtained from scoreList'''
		return highestPts(scoreList(Rack))

def scoreList(Rack):
		'''Returns list of words with their point value as per scrabbleScores'''
		goodwords = wordTest(Rack,Dictionary)
		return dictCheck(goodwords)

#Helper functions#
def length(L):
		'''Returns the length of a list L'''
		if (L==[]):
			return 0
		else:
			return 1 + length(L[1:])

def highestPts(L):
		'''Returns the best word/word with highest point value given a list formatted like output from scoreList'''
		if (length(L)==1):
			return L[0]
		elif (L[0][1] > L[1][1]):
			L[1] = L[0]
			return highestPts(L[1:])
		else:
			L[0] = L[1]
			return highestPts(L[1:])

def wordTest(Rack,L):
		'''Tries each word in dictionary against rack and sees if string is possible to create from rack'''
		if (L==[]):
			return L
		elif ('0' not in rackCheck(Rack,L[0])):
			return [L[0]] + wordTest(Rack,L[1:])
		else:
			return wordTest(Rack,L[1:])
	
def remove(e,L):
		'''Removes the first occurrence of search term in list'''
		if (L==[]):
			return []
		elif (L[0] != e):
			return [L[0]] + remove(e,L[1:])
		elif (L[0] == e):
			return L[1:]

def letterScore(letter, scorelist):
		'''Returns the score for a single letter by looking it up in the provided scorelist'''
		if (scorelist==[]):
			return 0
		elif (scorelist[0] == letter):
			return scorelist[1]
		elif (type(scorelist[0]) == type([])):
			return letterScore(letter,scorelist[1:]) + letterScore(letter,scorelist[0])
		else:
			return (letterScore(letter,scorelist[1:]))

def wordScore(S,scorelist):
		'''Returns the score for an entire word/string by splitting it by letter, and calling letterScore on each letter. Adds up scores, returns number'''
		if (S==''):
			return 0
		elif ((letterScore(S[0],scorelist))):
			return (letterScore(S[0],scorelist)) + wordScore(S[1:],scorelist)

def dictCheck(S):
		'''Checks if list member S is in the dictionary/returns point value.'''
		if (S==[]):
			return []
		elif (S[0] == ''):
			return []
		elif(S[0] in Dictionary):
			return [[S[0]] + [wordScore(S[0],scrabbleScores)]] + dictCheck(S[1:])
		else:
			return dictCheck(S[1:])
			
def rackCheck(Rack,S):
		'''Checks if string S can be made up from letters in list Rack'''
		if (S==''):
			return ''
		elif (S[0] in Rack):
			NewRack = remove(S[0],Rack)
			n = rackCheck(NewRack,S[1:])
			return (S[0] + n)
		else:
			return '0'