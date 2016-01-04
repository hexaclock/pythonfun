def short(List):
#returns true if list has len <= 2
	return len(List) <= 2

#filter(func,list)
#filter(even,[1,2,3,4,5,6])
###[2,4,6]

def divides(n):
	def div(k):
		return n % k == 0
	return div

#f = divides(10)
#f
###function f at some_mem_addr
#f(2)
##10/2 has a remainder of 0
###true

listOfFunctions = [divides(10),divides(20)]
listOfFunctions[0](2)