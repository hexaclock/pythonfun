def gauss(x):
        squared = map(square,range(1,x+1))
        added = reduce(add,squared)
        return added
def add(x,y):
        return x+y

def square(x):
        return (x*x)
