numlist = list()
while (True):
	usrinp = raw_input("Enter a number: ")
	if usrinp == "done" : break
	value = float(usrinp)
	numlist.append(value)

average = sum(numlist) / len(numlist)
print "Average:", average
