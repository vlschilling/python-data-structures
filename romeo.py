fname = raw_input("Enter file name: ")
fhand = open(fname)


#fhand = open("romeo.txt")
x = list()

#count = 0
for line in fhand:
	words = line.split()
	for t in range(len(words)) :
		if words[t] not in x :
			x.append(words[t])
	#print words
x.sort()
print x
