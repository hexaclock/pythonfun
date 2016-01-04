def combs(n):
	'''Returns a list of all lists of n bits, in binary numerical order. In other words, finds + returns all of the combinations you can make with n bits'''
	if n==1: return [[0],[1]]		
	else:
		var = combs(n-1)
		return map(lambda item: [0]+item, var) +  map(lambda item: [1]+item, var)

def func0(x,y,z): return x and (y or z)

def func0table():
	'''Returns the list [([0,0,0], 0), ([0,0,1], 0), ... , ([1,1,1], 1)] which represents the truth table for func0. In other words, lists all of the tuples ([x,y,z], func0(x,y,z)).'''
	combos = combs(3)
	truth = map(lambda args: func0(*args), combos)
	return map(merge,combos,truth)

def merge(a,b):
	'''Combines two variables into a tuple'''
	return a,b
	
def showTable(lst):
    '''Assume lst is in the format returned by func0table(). Print it.'''
    if lst == []: return None
    else:
        print lst[0][0], lst[0][1]
        showTable(lst[1:])

def func0alt(x,y,z):
	return ((x and not y and z)
			or (x and y and not z)
			or (x and y and z))

def func0test():
	'''Applies func0 and func0alt to all possible inputs.  Returns True if they agree in every case, otherwise False.'''
	combos = combs(3)
	truth = map(lambda args: func0(*args), combos)
	alttruth = map(lambda args: (func0alt(*args)), combos)
	return truth==alttruth

def func1(x,y): return x or (y and x)

def func1table():
	'''Return a table of values of func1, so they can be displayed using showTable.'''
	combos = combs(2)
	truth = map(lambda args: func1(*args), combos)
	return map(merge,combos,truth)

def func1alt(x,y):
    '''Return func1(x,y), computed based on the minterm principle.'''
	#Need to finish this function.
    return ((x and not y)
			or (x and y))

def func1test():
	'''Apply func1 and func1alt to all possible inputs.  Return True or False depending on whether they agree in every case.'''
	combos = combs(2)
	truth = map(lambda args: func1(*args), combos)
	alttruth = map(lambda args: (func1alt(*args)), combos)
	return truth==alttruth


print func1test()