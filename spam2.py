fname = raw_input('Enter the file name: ')
if fname=="na na boo boo":
	print "NA NA BOO BOO TO YOU - You have been punk'd!"
	exit()
else:
	try:
		fhand = open(fname)
	except:
		print 'File cannot be opened:', fname
		exit()

count = 0
total = 0.0

for line in fhand:
	line = line.rstrip()
	### Skip 'uninteresting lines'
	if not line.startswith('X-DSPAM-Confidence:') :
		continue

	### Process our 'interesting' line
	### print the lines to see what they look like
#	print line
	first = line.find(':')
#	print first

	### get the number on the X-DSPAM-Confidence line
	num = float(line[first+1:])
#	print num

	### count the lines
	count = count + 1
#	print count
	
	### sum the floats
	total = total + num
#	print total
	
### average the floats
avg = total / count

print 'Average spam confidence: ', avg
### ----- END -----



