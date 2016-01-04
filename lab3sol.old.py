def dot(L, K):
	if (L==[] or K==[]):
		return 0.0
	elif (length(L)!=length(K)):
		return 0.0
	else:
		#return ((L[0] * K[0]) + (dot(L[1:] * K[1:])))
		return (L[0] * K[0])

def length(L):
	if (L==[]):
		return 0
	else:
		return 1 + length(L[1:])
		
dot([1,2,3],[1,2,3])
