# CS 115 Homework 6
# Daniel Vinakovsky
# 17 October 2013
# I pledge my honor that I have abided by the Stevens Honor System.

#Bit constant
k = 8

#Main functions#
def compress(S):
	'''Returns the run-length compressed form of an inputted binary string'''
	splitgroup = splitGroup(S)
	csstolist = cssToList(splitgroup)
	lgth = map(length,csstolist)
	if '1' in csstolist[0]: lgth = [0] + lgth
	numtobinary = map(numToBinary,lgth)
	prefixed = map(prefixZeroes,numtobinary)
	compressedstr = reduce(concatenate,prefixed)
	return compressedstr
	
def uncompress(C):
	'''Returns the uncompressed form of a compressed binary string C'''
	list = separate(C)
	basetenlist = map(binaryToNum,list)
	return convert(basetenlist)

def compression(S):
	'''Returns the compression ratio of compressed_string:uncompressed_string'''
	return (len(compress(S))*1.0) / (len(S)*1.0)

#Helper functions#
def convert(L):
	'''Taking a list of decimal numbers that represent the number of 0s and 1s (ex: [5,2,3,4] means five 0s, two 1s, three 0s, four 1s), and returns the corresponding/uncompressed string.'''
	if len(L)==1: return ('0'*L[0])
	elif len(L)==2: return ('0'*L[0]) + ('1'*L[1])
	else: return ('0'*L[0])+('1'*L[1])+convert(L[2:])
	
def separate(S):
	'''Cuts a string into k bit substrings, and puts each substring into a list as an element'''
	if S=='': return []
	else: return [S[0:k]] + separate(S[k:])

def concatenate(stra,strb):
	'''Return the concatentation of two strings'''
	return stra+strb

def numToBinary(N):
	'''Converts a decimal number to binary/base2'''
	if (N==0): return ''
	else: return numToBinary(N/2)+str(N%2)

def binaryToNum(S):
	'''Converts a binary string to a decimal number'''
	bits = len(S)
	if (S==''):	return 0
	elif (S[0] == '0'): return binaryToNum(S[1:])
	elif (S[0] == '1'):	return ((2**(bits-1))) + binaryToNum(S[1:])
	
def prefixZeroes(S):
	'''Prefixes zeroes to a binary string to make it into a standard 8 bit binary string'''
	binary = S
	len_binary = len(binary)
	return ('0'*(k-len_binary)) + binary

def length(L):
	'''Returns the length of a string or list'''
	return len(L)

def splitGroup(S):
	'''Splits an inputted string by 1s and 0s. Ex: 01110101001 --> 0,111,0,1,0,1,00,1'''
	if len(S)==1: return S[0]
	else:
		if S[0]==S[1]: return S[0]+splitGroup(S[1:])
		else: return S[0]+','+splitGroup(S[1:])
		
def cssToList(S):
	'''A homemade "split" function; takes a comma-separated string and turns it into a list'''
	index = ind(',',S)
	if S=='': return []
	else: return [S[0:index]] + cssToList(S[index+1:])
	
def ind(e, L):
	'''Returns the index of the first element matching 'e' found in list L'''
	if (L==''): return 0
	elif (L[0] == e): return 0
	elif (L[0] != e): return (ind(e,L[1:]) + 1)
