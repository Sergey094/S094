import re

s = input()
c = input()

d = re.findall(re.escape(c), s)

print(len(d))
