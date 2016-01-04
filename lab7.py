def isOdd(n):
	if n%2 == 0: return False
	else: return True

#42 in base 10 = 101010 in base 2

#An odd base 10 number will have a 1 for the rightmost bit in its base-2 representation, whereas an even base 10 number will have a 0 in the same place. The reason for this is because the least
#significant bit is 2^0, or 1. The rest of the bits are all even numbers (2^2,2^3,2^4). Any even number added to another even number is always even, and a 1 added to any even number automatically makes it odd.
#Thus, all even numbers have a 0 for the last bit, all odd numbers have a 1 for the last bit in binary.

#Eliminating the last bit in 1010 (so eliminating the last 0), gives us 101. This causes a shift to the right, and results in an integer division by 2.

#In the case that N is even, we'll need to append a zero at the right. In the case that N is odd, we'll need to append a one at the right.

#Binary functions

def numToBinary(N):
	if (N==0): return ''
	else: return numToBinary(N/2)+str(N%2)

def binaryToNum(S):
	bits = len(S)
	if (S==''):	return 0
	elif (S[0] == '0'): return binaryToNum(S[1:])
	elif (S[0] == '1'):	return ((2**(bits-1))) + binaryToNum(S[1:])
	
def increment(S):
	if (S == '11111111'):	return ('0'*8)
	baseten = binaryToNum(S)
	incremented = baseten
	ibinary = numToBinary(incremented)
	len_ibinary = len(ibinary)
	return ('0'*(8-len_ibinary)) + ibinary
	
def count(S, n):
	if n<0: return
	else:
		print S
		count(increment(S),n-1)
		
#################################################################################################################################################################################################
'''59 in decimal notation/base 10 is represented as 2012 in ternary/base 3.'''

#Ternary functions

def numToTernary(N):
	if (N==0): return ''
	else: return numToTernary(N/3)+str(N%3)

def ternaryToNum(S):
	return None

#Balanced ternary functions#
	
def balancedTernaryToNum(S):
	return None
	
def numToBalancedTernary(N):
	if (N==0): return ''
	else:
		if N%3==0: return numToBalancedTernary(N/3)+'0'
		elif N%3==1: return numToBalancedTernary(N/3)+'+'
		elif N%3==2: return numToBalancedTernary((N/3)+1)+'-'
			
#count('11111110',5)
print increment('11010')