def main():
	print dot([1,2,3],[1,2,3])

def dot(L, K):
        if (L==[] or K==[]):
                return 0.0
        else:
                return ((L[0] * K[0]) + dot(L[1:],K[1:]))

def explode(S):
	if (S==''):
		return []
	else:
		return [S[0]] + explode(S[1:])

def ind(e, L):
        if (L==[]):
                return 0
        elif (L[0] == e):
                return 0
        else:
                return (ind(e,L[1:]) + 1)

def removeAll(e,L):
        if (L==[]):
                return []
        elif (L[0] != e):
                return [L[0]] + removeAll(e,L[1:])
        else:
                return [] + removeAll(e,L[1:])

def myFilter(func,L):
        if (L==[]):
                return []
        elif (func(L[0]) == True):
                return [L[0]] + myFilter(func,L[1:])
        else:
                return myFilter(func,L[1:])

def deepReverse(L):
        if (L==[]):
                return []
        elif (type(L[0]) == type([])):
                return deepReverse(L[1:]) + [deepReverse(L[0])]
        else:
                return deepReverse(L[1:]) + [L[0]]

#testing and helper functions#
def even(x):
        return x % 2 == 0

def length(L):
	if (L==[]):
		return 0
	else:
		return 1 + length(L[1:])


##from friday's class - 9/13/2013##

def prime(n):
#tests if number is prime
        possibleDivisors = range(2,n)
        divisors=filter(lambda X: n%X==0,possibleDivisors)
        return len(divisors)==0

def sieve(L):
        if L == []: return []
        else: return [L[0]] + sieve(filter(lambda X: X % L[0] != 0, L[1:]))

def primes(n):
        return sieve(range(2,n+1))

main()