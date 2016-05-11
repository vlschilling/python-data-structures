total = 0
count = 0

while (True):
	usrinp = raw_input("Enter a number: ")
	if usrinp == 'done' : break
	value = float(usrinp)
	total = total+value
	count = count+1

average = total/count
print "Average:", average