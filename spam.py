fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

count = 0

for line in fhand:
     line = line.rstrip()
# Skip 'uninteresting lines'
     if not line.startswith('X-DSPAM-Confidence:') :
		continue

# Process our 'interesting' line
# print the lines to see what they look like
print line
first = line.find(':')
# not sure if I need to designate an end character or not -- no
# last = line.find(' ',first).  <----- not needed
num = float(line[first+1:last])

# count the lines
count = count + 1

# sum the floats
total =????

# average the floats
???? = total \ count

print 'Average spam confidence: ',?????
# ----- END -----

# random code bits as examples
print 'Line Count:', count

fhand = open('mbox.txt')
count = 0
for line in fhand:
count = count + 1
print 'Line Count:', count

python open.py
Line Count: 132045


text from grader window:
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    first = line.find(':')
    num = float(line[first+1:])
    #print num
    count = count + 1
    #print count
    #num = sum(num)   <--- ????
    #print num
    total = sum(num) / count     <------ change to this?
    print total
print "Done"
