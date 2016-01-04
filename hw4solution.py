# CS 115 Homework 4
# Daniel Vinakovsky
# 21 September 2013
# I pledge my honor that I have abided by the Stevens Honor System.


def giveChange(amount,coins):
	'''Returns the least number of coins and each coin's value needed to construct a certain amount of change'''
	if (amount==0):
		return [0,[]]	
	elif (coins==[]):
		return [float("inf"),[]]
	elif (amount-coins[0] < 0):
		return giveChange(amount,coins[1:])
	else:
		useIt = giveChange(amount-coins[0],coins)
		useIt = [useIt[0]+1,[coins[0]]+useIt[1]]
		loseIt = giveChange(amount,coins[1:])			
		if (useIt[0] < loseIt[0]):
			return useIt
		else:
			return loseIt

#########################################################################################################################################################################################################################################################################################################
def fancyLCS(S1,S2):
	'''Returns the longest common subsequence of S1 and S2 + its length.'''
	#Works 95%, just could not get pound signs to work correctly/reliably
	if S1=='' or S2=='':
		return [0,'','']
	else:
		if (S1[0] == S2[0]):
			useIt = fancyLCS(S1[1:],S2[1:])
			useIt = useIt[0]+1,S1[0]+useIt[1],S2[0]+useIt[2]
			loseIt = fancyLCS(S1[1:],S2)
			if (useIt[0]>=loseIt[0]):
				return useIt[0],useIt[1],useIt[2]
			else:
				return loseIt[0],loseIt[1],loseIt[2]
		else:
			temp = fancyLCS(S1,S2[1:])
			anothertemp = fancyLCS(S1[1:],S2)
			if (temp[0] >= anothertemp[0]):
				return temp[0],temp[1],temp[2]
			else:
				return anothertemp[0],anothertemp[1],anothertemp[2]

#########################################################################################################################################################################################################################################################################################################

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

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

def dictCheck(S,scores):
		'''Checks if list member S is in the dictionary/returns point value.'''
		if (S==[]):
			return []
		elif (S[0] == ''):
			return []
		elif(S[0] in S):
			return [[S[0]] + [wordScore(S[0],scores)]] + dictCheck(S[1:],scores)
		else:
			return dictCheck(S[1:],scores)

def wordsWithScore(dict, scores):
	'''Returns a list of words with their scores'''
	return dictCheck(dict,scores)

####################################################################################################################################################################################################################################################################################

def take(n, L):
	'''finds L[0:n]'''
	if L==[]:
		return []
	elif (n==0):
		return [L[0]]
	elif (n<0):
		return []
	elif (n==1):
		return [L[0]]
	else:
		if (n<len(L)):
			return [L[0]] + take(n-1,L[1:])
		else:
			return [L[0]] + L[1:]

####################################################################################################################################################################################################################################################################################

def drop(n,L):
	'''finds L[n:]'''
	if L==[]:
		return []
	elif (n==0):
		return [L[0]] + L[1:]
	elif (n==1):
		return L[1:]
	else:
		if (n<len(L)):
			return drop(n-1,L[1:])