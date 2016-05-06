
### Using startswith ###
#fhand=open('mbox-short.txt')
#for line in fhand:
#	line = line.rstrip()
#	#skip uninteresting lines
#	if not line.startswith('From:'):
#		continue
#	#process the interesting lines	
#	print line
###


### Using find ###
#fhand=open('mbox-short.txt')
#for line in fhand:
#	line = line.rstrip()
#	if line.find('@uct.ac.za') == -1:
#		continue
#	print line
###


### User input of file name ###
#fname=raw_input("Enter the filename: ")
#fhand=open(fname)
#count = 0
#for line in fhand:
#	if line.startswith("Subject:"):
#		count = count+1
#print "There were", count, "subject lines in", fname
###


### User input of file name, catching exceptions ###
fname=raw_input("Enter the filename: ")
try:
	fhand=open(fname)
except:
	print "File cannot be opened:", fname
	exit()

count = 0
for line in fhand:
	if line.startswith("Subject:"):
		count = count+1
print "There were", count, "subject lines in", fname
###


























