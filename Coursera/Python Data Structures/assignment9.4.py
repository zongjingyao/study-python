name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
emails = dict()
for line in fh :
    if line.startswith("From ") :
        words = line.split()
        key = words[1]
        emails[key] = emails.get(key, 0) + 1

maxEmail = None
maxCount = None
for key in emails :
    if maxCount is None or maxCount < emails[key] :
        maxCount = emails[key]
        maxEmail = key
print maxEmail, maxCount