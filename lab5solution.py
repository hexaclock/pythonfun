import time

memo = {}
file = open("3esl.txt")
contents = file.read()
words = contents.split("\n")
userIn = raw_input("spell check> ")
HITS=10

def spam():
        if userIn == "quitbitch":
                quit()
        elif userIn in words:
                print "Correct"
                global userIn
                userIn = raw_input("spell check> ")
                spam()
        else:
                startTime=time.time()
                x = map(auxiliary,words[0:])
                x.sort()
                print "Suggested alternatives:"
                extracted = (map(printer,extractSecond(x[0:HITS])))
                endTime=time.time()
                print "Computation time: ", endTime-startTime
                global userIn
                userIn = raw_input("spell check> ")
                spam()
		
def printer(n):
	print n
		
def extractSecond(x):
	if (x==[]):
		return x
	elif (x[0]==''):
		return x
	else:
		return [x[0][1]] + extractSecond(x[1:])

def auxiliary(dictword):
        points = fastED(userIn,dictword)
        return (points,dictword)

def fastED(first, second):
        return ED(first, second)

def ED(first, second):
	if first == '':
		return len(second)
	elif second == '':
		return len(first)
	elif memo.has_key((first,second)):
		return memo[(first,second)]
	elif first[0] == second[0]:
		return ED(first[1:],second[1:])
	else:
		sub = 1 + ED(first[1:],second[1:])
		delete = 1 + ED(first[1:],second)
		ins = 1 + ED(first,second[1:])
		ineedvar = min(sub,delete,ins)
		memo[(first,second)]=ineedvar
		return ineedvar

spam()

'''print ED("spam", "xsam")
print ED("foo", "")
print ED("foo", "bar")
print ED("hello", "below")
print ED("yes", "yelp")
print ED("extraordinary", "originality")
print ED("antidisestablishment", "antiquities")
print ED("xylophone", "yellow")
print ED("follow", "yellow")
print ED("lower", "hover")'''
	  

