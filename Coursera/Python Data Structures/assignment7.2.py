# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(":")
    total = total + float(line[pos + 1:])
    count = count + 1    
ave = total / count
print "Average spam confidence:", ave