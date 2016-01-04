#lab1
import math

def inverse(n):
	return (1.0/n)

def add(x,y):
        return x+y

def e(n):
        denlist = range(1,n)
        factorials = map(math.factorial,denlist)
        invfactorials = map(inverse,factorials)
        answer = reduce(add,invfactorials)
        return answer + 1

def error(n):
        naturalnum = math.e
        return abs(e(n) - naturalnum)

def mult(x,y):
        return x*y

def factorial(n):
        numlist = range(1,n+1)
        factorial = reduce(mult,numlist)
        return factorial

def mean(L):
        length = len(L)
        added = (.0 + reduce(add,L))
        return (added/length)
