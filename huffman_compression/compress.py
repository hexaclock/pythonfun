#Daniel Vinakovsky
#November 12, 2013
#I pledge my honor that I have abided by the Stevens Honor System
#Huffman compression as implemented in Python2.7
#compress.py

def main():
	filename = raw_input("Enter name of file to be compressed: ")
	huff2 = open(filename, "rb")
	huffstring = huff2.read()
	huff2.close()
	print "Original file:  "+filename
	print "Distinct characters: "+str(len(countFreq(huffstring)))
	print "Total bytes: "+str(len(huffstring))
	print "Frequencies: "+str(countFreq(huffstring))
	print "Most frequent: "+(str(mostFrequent(huffstring)))
	
	
def encodingTree(sortedfreqs):
	#Need to implement correctly, below is broken
	if sortedfreqs == []:
		return sortedfreqs
	else:
		length = len(sortedfreqs)
		if length%2==0:
			return [0]+encodingTree(sortedfreqs[1:])
		elif length%2!=0:
			return [1]+encodingTree(sortedfreqs[1:])
	
def tupleSort(strg):
	#selection sort for tuples
	Frequencies = countFreq(strg)
	items = Frequencies.items()
	for i in range(len(items)):
		maxm = i
		for x in range(i+1,len(items)):
			if items[x][1] > items[maxm][1]:
				maxm = x
		swap = items[i]
		items[i] = items[maxm]
		items[maxm] = swap
	return items

def countFreq(strg):
	Frequencies = {}
	for i in range(len(strg)):
		if Frequencies.has_key(strg[i]):
			value = Frequencies[strg[i]]
			newVal = value + 1
			Frequencies[strg[i]] = newVal
		else:
			Frequencies[strg[i]] = 1
	return Frequencies

#if __name__ == "__main__":
 #   main() 
	
print tupleSort("thisisAAanexaAAmpleAAofahuffAAmantree")
