def ifElse(condition, t, f):
	'''condition is a boolean and t and f are arbitrary expressions. Returns the value of expression t if the condition is true and
	other returns the value of expression f.'''
	if condition: return t
	else: return f
	
def fold(RNA):
	condition = RNA[0]+RNA[-1]=='AU' or RNA[0]+RNA[-1]=='UA' or RNA[0]+RNA[-1]=='GC' or RNA[0]+RNA[-1]=='CG'
	first_last = ifElse(condition,True,False)
	if (RNA == '' or RNA[-1]=='' or RNA[0]==''):
		return 0
	elif len(RNA) == 2:
		if ifElse(condition,True,False): return 1
		else: return 0
	elif (first_last == True):
		use = 1 + fold(RNA[1:-1])
		lose = fold(RNA[0:-1])
		return max(use,lose)
	else:
		return fold(RNA[0:-1])

		
print fold("ACCCCCU")
print fold("ACCCCGU")		
print fold("AAUUGCGC")
		