import re

fh = open("regex_sum_204935.txt")
content = fh.read()
nums = re.findall("[0-9]+", content)
print sum([int(num) for num in nums])