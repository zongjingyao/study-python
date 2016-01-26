name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

dic = dict()
handle = open(name)
for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        dic[hour] = dic.get(hour, 0) + 1

for key, value in sorted(dic.items()):
    print key, value